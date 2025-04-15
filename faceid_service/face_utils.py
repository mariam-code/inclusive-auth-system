import face_recognition
import os

def load_known_face(path):
    image = face_recognition.load_image_file(path)
    encodings = face_recognition.face_encodings(image)
    return encodings[0] if encodings else None

def compare_faces(known_encoding, uploaded_image_path):
    unknown_image = face_recognition.load_image_file(uploaded_image_path)
    unknown_encodings = face_recognition.face_encodings(unknown_image)

    print(f"[DEBUG] Number of encodings in uploaded image: {len(unknown_encodings)}")

    if not unknown_encodings:
        return False

    match_result = face_recognition.compare_faces([known_encoding], unknown_encodings[0])[0]
    print(f"[DEBUG] Match result: {match_result}")
    return match_result

