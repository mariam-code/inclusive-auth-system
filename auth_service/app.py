import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail, Message
import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
from models import db, User
from utils import generate_otp, log_event  # Added log_event
from werkzeug.security import generate_password_hash


load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Mail config
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

db.init_app(app)
bcrypt = Bcrypt(app)
mail = Mail(app)

# Create DB
with app.app_context():
    db.create_all()

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    hashed_pw = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(email=data['email'], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    log_event(f"User registered: {data['email']}")  # Log registration
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and bcrypt.check_password_hash(user.password, data['password']):
        otp = generate_otp()
        user.otp = otp
        db.session.commit()

        msg = Message('Your OTP Code', recipients=[user.email])
        msg.html = render_template('otp_email.html', otp=otp)
        mail.send(msg)

        log_event(f"OTP sent to {user.email}")  # Log OTP send
        return jsonify({'message': 'OTP sent to email'}), 200

    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/verify-otp', methods=['POST'])
def verify_otp():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if user and user.otp == data['otp']:
        token = jwt.encode(
            {'user_id': user.id, 'exp': datetime.utcnow() + timedelta(minutes=30)},
            os.getenv('JWT_SECRET'),
            algorithm='HS256'
        )
        user.otp = None  # Invalidate OTP after use
        db.session.commit()
        log_event(f"OTP verified for {user.email}")  # Log successful OTP
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid or expired OTP'}), 401

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    hashed_pw = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_pw)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@app.route('/delete-user', methods=['POST'])
def delete_user():
    data = request.get_json()
    email = data.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        return jsonify({'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': f'User {email} deleted successfully'}), 200

if __name__ == '__main__':
    app.run(port=5001, debug=True)


