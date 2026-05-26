import cv2
import time
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

from gaze import (
    LEFT_EYE_IDX, RIGHT_EYE_IDX,
    LEFT_IRIS_IDX, RIGHT_IRIS_IDX,
    get_iris_center, get_eye_box,
    compute_gaze_direction, classify_gaze
)

from utils import eye_aspect_ratio, draw_iris, draw_gaze_arrow, put_label
from hand_gesture import detect_gesture
from robot_control import decide_action

print("Camera started...")

# ── LOAD MODELS ─────────────────────────────
face_base = python.BaseOptions(
    model_asset_path="models/face_landmarker.task"
)

face_options = vision.FaceLandmarkerOptions(
    base_options=face_base,
    num_faces=1
)

face_detector = vision.FaceLandmarker.create_from_options(face_options)

# ── CAMERA ─────────────────────────────
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Camera not working ❌")
    exit()

# ── BLINK ─────────────────────────────
EAR_THRESHOLD = 0.20
CONSEC_FRAMES = 2
blink_counter = 0
frame_counter = 0

prev_time = 0

print("Press Q to quit")

# ── MAIN LOOP ─────────────────────────────
while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    h, w = frame.shape[:2]

    # Convert to MediaPipe image
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=frame
    )

    gaze_label = "Center"
    gesture = "NONE"
    action = "IDLE"

    # ── FACE DETECTION ─────────────────
    face_result = face_detector.detect(mp_image)

    if face_result.face_landmarks:
        lm = face_result.face_landmarks[0]

        # GAZE
        l_iris = get_iris_center(lm, LEFT_IRIS_IDX, w, h)
        l_box = get_eye_box(lm, LEFT_EYE_IDX, w, h)
        l_off_x, l_off_y = compute_gaze_direction(l_iris, l_box)

        r_iris = get_iris_center(lm, RIGHT_IRIS_IDX, w, h)
        r_box = get_eye_box(lm, RIGHT_EYE_IDX, w, h)
        r_off_x, r_off_y = compute_gaze_direction(r_iris, r_box)

        avg_x = (l_off_x + r_off_x) / 2.0
        avg_y = (l_off_y + r_off_y) / 2.0

        gaze_label = classify_gaze(avg_x, avg_y)

        # BLINK
        l_eye_pts = [lm[i] for i in LEFT_EYE_IDX]
        r_eye_pts = [lm[i] for i in RIGHT_EYE_IDX]

        avg_ear = (
            eye_aspect_ratio(l_eye_pts, w, h) +
            eye_aspect_ratio(r_eye_pts, w, h)
        ) / 2.0

        if avg_ear < EAR_THRESHOLD:
            frame_counter += 1
        else:
            if frame_counter >= CONSEC_FRAMES:
                blink_counter += 1
            frame_counter = 0

        # DRAW
        draw_iris(frame, l_iris)
        draw_iris(frame, r_iris)

        draw_gaze_arrow(frame, l_iris, (avg_x, avg_y))
        draw_gaze_arrow(frame, r_iris, (avg_x, avg_y))

    else:
        put_label(frame, "No face detected", (20, 40), (0, 0, 255))

    # ── HAND GESTURE ─────────────────
    gesture = detect_gesture(frame)

    # ── ROBOT ACTION ─────────────────
    action = decide_action(gesture, gaze_label)

    # ── DISPLAY ─────────────────────
    put_label(frame, f"Gaze: {gaze_label}", (20, 40))
    put_label(frame, f"Blinks: {blink_counter}", (20, 70))
    put_label(frame, f"Gesture: {gesture}", (20, 110))
    put_label(frame, f"Action: {action}", (20, 140))

    # FPS
    curr_time = time.time()
    fps = 1 / (curr_time - prev_time + 1e-6)
    prev_time = curr_time
    put_label(frame, f"FPS: {int(fps)}", (w - 100, h - 20))

    # SHOW WINDOW
    cv2.imshow("Gesture + Gaze Robot Control", frame)

    # EXIT
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ── CLEANUP ─────────────────────────
cap.release()
cv2.destroyAllWindows()