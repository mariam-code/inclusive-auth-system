from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_babel import Babel, gettext
import requests
import re

app = Flask(__name__)
app.secret_key = 'supersecure'

# Supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['LANGUAGES'] = ['en', 'fr', 'es', 'ar', 'yo', 'hi', 'bn', 'pl', 'zh']

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.args.get('lang') or 'en'

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        response = requests.post('http://localhost:5001/login', json={
            'email': email,
            'password': password
        })
        if response.ok:
            flash(gettext('OTP sent to your email.'))
            return redirect(url_for('verify_otp', email=email, lang=get_locale()))
        else:
            flash(gettext('Login failed.'))
    return render_template('login.html')

@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    email = request.args.get('email')
    if request.method == 'POST':
        otp = request.form['otp']
        response = requests.post('http://localhost:5001/verify-otp', json={
            'email': email,
            'otp': otp
        })
        if response.ok:
            token = response.json()['token']
            session['token'] = token
            flash(gettext('Authenticated.'))
            return redirect(url_for('face', email=email, lang=get_locale()))
        else:
            flash(gettext('Invalid OTP.'))
    return render_template('verify.html', email=email)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.clear()
    flash(gettext('You have been logged out.'))
    return redirect(url_for('login', lang=get_locale()))

@app.route('/face')
def face():
    email = request.args.get('email')
    return render_template('face.html', email=email)

@app.route('/verify-face', methods=['POST'])
def verify_face():
    image_data = request.files['image']
    email = request.args.get('email')

    try:
        response = requests.post(
            f'http://localhost:5003/verify-face?email={email}',
            files={'image': (image_data.filename, image_data.stream, 'image/jpeg')}
        )

        if response.status_code == 200:
            result = response.json()
            if result.get('match'):
                flash(gettext('✅ Face matched. Access granted.'))
                return redirect(url_for('home', lang=get_locale()))
            else:
                flash(gettext('❌ Face not recognized.'))
                return redirect(url_for('face', email=email, lang=get_locale()))

        elif response.status_code == 403:
            flash(gettext('⏰ Face too old. Please upload a recent image taken within the last 60 seconds.'))
            return redirect(url_for('face', email=email, lang=get_locale()))

        else:
            flash(gettext('❌ Face not recognized.'))
            return redirect(url_for('face', email=email, lang=get_locale()))

    except Exception as e:
        print(f"[ERROR] Face verification exception: {e}")
        flash(gettext('Error verifying face.'))
        return redirect(url_for('face', email=email, lang=get_locale()))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        face_image = request.files.get('face')
        timestamp_str = request.form.get('timestamp')

        # Check if image was captured within 1 minute
        try:
            image_time = datetime.fromisoformat(timestamp_str)
            if datetime.utcnow() - image_time > timedelta(minutes=1):
                flash(gettext('Image must be taken within the last minute for security reasons.'))
                return render_template('register.html')
        except Exception:
            flash(gettext('Invalid timestamp. Please re-upload the image.'))
            return render_template('register.html')

        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
        if not re.match(pattern, password):
            flash(gettext('Password must be at least 8 characters long and include a number, uppercase, lowercase, and special character.'))
            return render_template('register.html')

        response = requests.post('http://localhost:5001/register', json={
            'name': name,
            'email': email,
            'password': password
        })

        if response.ok:
            if face_image:
                files = {'image': (face_image.filename, face_image.stream, 'image/jpeg')}

                check_response = requests.post('http://localhost:5003/check-encoding', files=files)
                if check_response.status_code != 200:
                    flash(gettext('Face not clear. Please upload a clearer image.'))
                    return render_template('register.html')

                face_image.stream.seek(0)
                save_response = requests.post(f'http://localhost:5003/register-face?email={email}', files=files)

                if save_response.ok:
                    flash(gettext('Registration successful. Face saved. Please log in.'))
                else:
                    flash(gettext('Registration successful but face not saved.'))
            else:
                flash(gettext('Registration successful.'))

            return redirect(url_for('face', email=email, lang=get_locale()))
        else:
            flash(gettext('User already exists or registration failed.'))

    return render_template('register.html')

@app.context_processor
def inject_locale():
    return {'get_locale': get_locale}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

