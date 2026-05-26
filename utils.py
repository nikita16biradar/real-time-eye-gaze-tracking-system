import numpy as np
import cv2

# ------------------------------------------------------------
# EAR = Eye Aspect Ratio
# Used to detect BLINKS
# Formula: (vertical distances) / (horizontal distance)
# When eye is open  → EAR ≈ 0.25–0.30
# When eye is closed → EAR < 0.20  → BLINK detected
# ------------------------------------------------------------
def eye_aspect_ratio(eye_landmarks, frame_w, frame_h):
    # eye_landmarks: list of (x,y) normalized coords from MediaPipe
    # We convert to pixel coords first
    pts = [(int(p.x * frame_w), int(p.y * frame_h)) for p in eye_landmarks]

    # Vertical distances (top-bottom pairs)
    A = np.linalg.norm(np.array(pts[1]) - np.array(pts[5]))
    B = np.linalg.norm(np.array(pts[2]) - np.array(pts[4]))

    # Horizontal distance (left-right)
    C = np.linalg.norm(np.array(pts[0]) - np.array(pts[3]))

    ear = (A + B) / (2.0 * C)
    return ear


# ------------------------------------------------------------
# Draw a colored circle on the iris center
# and a crosshair for gaze direction
# ------------------------------------------------------------
def draw_iris(frame, iris_center, color=(0, 255, 255), radius=3):
    cx, cy = iris_center
    cv2.circle(frame, (cx, cy), radius, color, -1)           # filled dot
    cv2.circle(frame, (cx, cy), radius + 4, color, 1)        # outer ring


def draw_gaze_arrow(frame, eye_center, direction, length=40):
    # direction is a unit vector (dx, dy)
    ex, ey = eye_center
    dx, dy = direction
    end_x = int(ex + dx * length)
    end_y = int(ey + dy * length)
    cv2.arrowedLine(frame, (ex, ey), (end_x, end_y),
                    (0, 200, 255), 2, tipLength=0.35)


def put_label(frame, text, pos, color=(255, 255, 255), scale=0.6):
    cv2.putText(frame, text, pos,
                cv2.FONT_HERSHEY_SIMPLEX, scale, color, 2, cv2.LINE_AA)