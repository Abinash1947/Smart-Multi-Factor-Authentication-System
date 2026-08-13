import face_recognization
import cv2
import os

FACE_DB = "faces/user.jpg"

def register_face():
    cam = cv2.VideoCapture(0)
    print("Press 's' to save face")

    while True:
        ret, frame = cam.read()
        cv2.imshow("Register Face", frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(FACE_DB, frame)
            break

    cam.release()
    cv2.destroyAllWindows()

def verify_face():
    if not os.path.exists(FACE_DB):
        return False

    known_image = face_recognition.load_image_file(FACE_DB)
    known_encoding = face_recognition.face_encodings(known_image)[0]

    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    rgb = frame[:, :, ::-1]
    encodings = face_recognition.face_encodings(rgb)

    if not encodings:
        return False

    return face_recognition.compare_faces(
        [known_encoding], encodings[0]
    )[0]
