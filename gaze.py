import numpy as np

# MediaPipe FaceMesh gives 478 landmarks (468 face + 10 iris)
# Iris landmark indices:
#   LEFT  iris center = 468,  LEFT  iris edge pts = 469,470,471,472
#   RIGHT iris center = 473,  RIGHT iris edge pts = 474,475,476,477
#
# Eye OUTLINE landmark indices (used for EAR blink detection):
LEFT_EYE_IDX  = [362, 385, 387, 263, 373, 380]
RIGHT_EYE_IDX = [33,  160, 158, 133, 153, 144]

LEFT_IRIS_IDX  = [468, 469, 470, 471, 472]
RIGHT_IRIS_IDX = [473, 474, 475, 476, 477]


def get_iris_center(landmarks, iris_indices, frame_w, frame_h):
    """
    Average position of the 5 iris landmarks = iris center in pixels.
    """
    xs = [landmarks[i].x * frame_w for i in iris_indices]
    ys = [landmarks[i].y * frame_h for i in iris_indices]
    return int(np.mean(xs)), int(np.mean(ys))


def get_eye_box(landmarks, eye_indices, frame_w, frame_h):
    """
    Bounding box of the eye region — used to normalize iris position.
    Returns: (x_min, y_min, x_max, y_max)
    """
    xs = [landmarks[i].x * frame_w for i in eye_indices]
    ys = [landmarks[i].y * frame_h for i in eye_indices]
    return int(min(xs)), int(min(ys)), int(max(xs)), int(max(ys))


def compute_gaze_direction(iris_center, eye_box):
    """
    Where is the iris relative to the eye box center?
    Returns a normalized offset:
      +x = looking RIGHT,  -x = looking LEFT
      +y = looking DOWN,   -y = looking UP
    Value range: roughly -1.0 to +1.0
    """
    ix, iy = iris_center
    x_min, y_min, x_max, y_max = eye_box

    eye_cx = (x_min + x_max) / 2.0
    eye_cy = (y_min + y_max) / 2.0
    eye_w  = x_max - x_min
    eye_h  = y_max - y_min

    # Avoid division by zero
    if eye_w == 0 or eye_h == 0:
        return 0.0, 0.0

    # Normalize: -1 = far left/up, +1 = far right/down
    offset_x = (ix - eye_cx) / (eye_w / 2.0)
    offset_y = (iy - eye_cy) / (eye_h / 2.0)

    return offset_x, offset_y


def classify_gaze(offset_x, offset_y, threshold=0.25):
    """
    Converts numeric offset to a human-readable direction.
    threshold: how far the iris must move before we call a direction.
    """
    label = "Center"

    if offset_x < -threshold:
        label = "Left"
    elif offset_x > threshold:
        label = "Right"

    if offset_y < -threshold:
        label = "Up" if label == "Center" else label + "-Up"
    elif offset_y > threshold:
        label = "Down" if label == "Center" else label + "-Down"

    return label