from flask import Flask, request, jsonify
import os
from face_utils import load_known_face, compare_faces

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load known encoding (once at startup)
known_face_path = os.path.join("known_faces", "user1.jpg")
known_encoding = load_known_face(known_face_path)

@app.route('/verify-face', methods=['POST'])
def verify_face():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(path)

    if compare_faces(known_encoding, path):
        return jsonify({"match": True}), 200
    else:
        return jsonify({"match": False}), 401

if __name__ == '__main__':
    app.run(port=5003, debug=True)
