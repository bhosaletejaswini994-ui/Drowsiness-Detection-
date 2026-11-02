
import cv2
import mediapipe as mp
import time
import math
import threading
import winsound

# Initialize Face Mesh
mp_face = mp.solutions.face_mesh

face_mesh = mp_face.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True
)

# Eye landmark points
LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]

# Settings
closed_start = None
sleep_time = 2
alarm_running = False


# Calculate eye opening
def eye_ratio(landmarks, eye_points, width, height):

    points = []

    for index in eye_points:
        x = int(landmarks[index].x * width)
        y = int(landmarks[index].y * height)
        points.append((x, y))

    vertical1 = math.dist(points[1], points[5])
    vertical2 = math.dist(points[2], points[4])
    horizontal = math.dist(points[0], points[3])

    return (vertical1 + vertical2) / (2 * horizontal)


# Alarm function
def start_alarm():

    global alarm_running

    while alarm_running:
        winsound.Beep(2500, 500)


# Open webcam
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not camera.isOpened():
    print("Camera not found!")
    raise SystemExit

print("Drowsiness Detection Started!")
print("Press Q to exit.")

try:

    while True:

        success, frame = camera.read()

        if not success:
            break

        frame = cv2.flip(frame, 1)

        height, width = frame.shape[:2]

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = face_mesh.process(rgb)

        if results.multi_face_landmarks:

            for face in results.multi_face_landmarks:

                landmarks = face.landmark

                left = eye_ratio(
                    landmarks, LEFT_EYE, width, height
                )

                right = eye_ratio(
                    landmarks, RIGHT_EYE, width, height
                )

                ear = (left + right) / 2

                # Detect closed eyes
                if ear < 0.22:

                    if closed_start is None:
                        closed_start = time.time()

                    elapsed = time.time() - closed_start

                    if elapsed >= sleep_time:

                        cv2.putText(
                            frame,
                            "WAKE UP! YOU ARE SLEEPY!",
                            (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 0, 255),
                            2
                        )

                        if not alarm_running:

                            alarm_running = True

                            threading.Thread(
                                target=start_alarm,
                                daemon=True
                            ).start()

                    else:

                        cv2.putText(
                            frame,
                            "Eyes Closing...",
                            (30, 50),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.8,
                            (0, 255, 255),
                            2
                        )

                else:

                    closed_start = None
                    alarm_running = False

                    cv2.putText(
                        frame,
                        "AWAKE",
                        (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 0),
                        2
                    )

                cv2.putText(
                    frame,
                    f"Eye Ratio: {ear:.2f}",
                    (30, 90),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 255, 0),
                    2
                )

        else:

            closed_start = None
            alarm_running = False

            cv2.putText(
                frame,
                "Face Not Detected",
                (30, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        cv2.imshow("Drowsiness Detection System", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

finally:

    alarm_running = False
    camera.release()
    face_mesh.close()
    cv2.destroyAllWindows()

    print("Camera stopped!")
