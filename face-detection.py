import threading
import cv2
from deepface import DeepFace
import uuid  

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

counter = 0
face_match = False
reference_img_path = "dharshan.jpg"
lock = threading.Lock()

def check_face(frame_path):
    global face_match
    try:
        result = DeepFace.verify(frame_path, reference_img_path)
        with lock:
            face_match = result['verified']
    except Exception as e:
        print(f"Error verifying face: {str(e)}")

while True:
    ret, frame = cap.read()

    if ret:
        if counter % 30 == 0:
            try:
                frame_filename = f"frame_{uuid.uuid4()}.jpg"  
                cv2.imwrite(frame_filename, frame)  
                threading.Thread(target=check_face, args=(frame_filename,)).start()
            except Exception as e:
                print(f"Error capturing frame: {str(e)}")

        counter += 1

        with lock:
            if face_match:
                cv2.putText(frame, "Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)
            else:
                cv2.putText(frame, "No Match", (20, 450), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 3)

        cv2.imshow("Video", frame)

        key = cv2.waitKey(1)
        if key == ord("q"):
            break

cv2.destroyAllWindows()
cap.release()
