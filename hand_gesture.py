from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import mediapipe as mp

# Load hand model
base_options = python.BaseOptions(
    model_asset_path="models/hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)


def detect_gesture(image):
    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=image
    )

    result = detector.detect(mp_image)

    if not result.hand_landmarks:
        return "NONE"

    lm = result.hand_landmarks[0]

    fingers = []

    # Check fingers (tip vs pip)
    for tip, pip in [(8, 6), (12, 10), (16, 14), (20, 18)]:
        if lm[tip].y < lm[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    total = sum(fingers)

    if total == 0:
        return "FIST"
    elif total == 4:
        return "PALM"
    else:
        return "UNKNOWN"