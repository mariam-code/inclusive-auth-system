from flask_cors import CORS
from flask import Flask, request, jsonify
from datetime import datetime
from PIL import Image
import os
from face_utils import load_known_face, compare_faces

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/verify-face', methods=['POST'])
def verify_face():
    email = request.args.get('email')
    print(f"\n🔍 [DEBUG] Verifying face for: {email}")

    if not email:
        return jsonify({"error": "Missing email"}), 400

    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    image = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(path)
    print(f"[INFO] Uploaded image saved to: {path}")

    #  Attempt to check EXIF timestamp
    try:
        img = Image.open(path)
        exif = img._getexif()
        if exif and 36867 in exif:
            ts = exif[36867]
            taken_time = datetime.strptime(ts, '%Y:%m:%d %H:%M:%S')
            age_seconds = (datetime.now() - taken_time).total_seconds()
            print(f"[INFO] Image timestamp age: {age_seconds:.1f} seconds")
            if age_seconds > 60:
                print("[ERROR] Image too old for verification")
                return jsonify({"match": False, "reason": "Image too old"}), 403
        else:
            print("[WARN] No EXIF timestamp found — skipping freshness check")
    except Exception as e:
        print(f"[WARN] Timestamp check failed: {e}")

    known_face_path = os.path.join("known_faces", f"{email}.jpg")
    print(f"[INFO] Looking for known face at: {known_face_path}")

    if not os.path.exists(known_face_path):
        return jsonify({"match": False, "reason": "No stored face"}), 404

    known_encoding = load_known_face(known_face_path)
    if known_encoding is None:
        return jsonify({"match": False, "reason": "Encoding failed"}), 500

    match = compare_faces(known_encoding, path)
    print(f"[RESULT] Match result: {match}")

    if match:
       return jsonify({"match": True}), 200
    else:
       return jsonify({"match": False}), 401


@app.route('/register-face', methods=['POST'])
def register_face():
    email = request.args.get('email')
    image_file = request.files.get('image')

    if not email or not image_file:
        return jsonify({'message': 'Missing email or image'}), 400

    save_path = os.path.join("known_faces", f"{email}.jpg")

    try:
        img = Image.open(image_file.stream)
        img.verify()
        image_file.stream.seek(0)
        image_file.save(save_path)

        # Confirm encoding is valid
        encoding = load_known_face(save_path)
        if encoding is None:
            return jsonify({'message': 'Saved image has no detectable face'}), 400

        print(f"[INFO] Face saved for {email}")
        return jsonify({'message': 'Face image saved'}), 200

    except Exception as e:
        print(f"[ERROR] Failed to process image: {e}")
        return jsonify({'message': 'Invalid image'}), 400

@app.route('/check-encoding', methods=['POST'])
def check_encoding():
    image = request.files['image']
    path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
    image.save(path)

    encoding = load_known_face(path)
    if encoding is None:
        return jsonify({"valid": False}), 400

    return jsonify({"valid": True}), 200

if __name__ == '__main__':
    app.run(port=5003, debug=True)

