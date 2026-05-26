import cv2
import numpy as np

# Selected landmark indices (important facial points)
# Nose tip, Chin, Left eye corner, Right eye corner, Left mouth, Right mouth
LANDMARK_IDS = [1, 152, 33, 263, 61, 291]

def get_head_pose(landmarks, frame_w, frame_h):
    # 2D image points
    image_points = []
    for idx in LANDMARK_IDS:
        x = int(landmarks[idx].x * frame_w)
        y = int(landmarks[idx].y * frame_h)
        image_points.append((x, y))

    image_points = np.array(image_points, dtype="double")

    # 3D model points (generic face model)
    model_points = np.array([
        (0.0, 0.0, 0.0),        # Nose tip
        (0.0, -63.6, -12.5),    # Chin
        (-43.3, 32.7, -26.0),   # Left eye left corner
        (43.3, 32.7, -26.0),    # Right eye right corner
        (-28.9, -28.9, -24.1),  # Left mouth corner
        (28.9, -28.9, -24.1)    # Right mouth corner
    ])

    # Camera matrix
    focal_length = frame_w
    center = (frame_w / 2, frame_h / 2)
    camera_matrix = np.array([
        [focal_length, 0, center[0]],
        [0, focal_length, center[1]],
        [0, 0, 1]
    ], dtype="double")

    dist_coeffs = np.zeros((4, 1))  # no distortion

    # Solve PnP
    success, rotation_vec, translation_vec = cv2.solvePnP(
        model_points, image_points, camera_matrix, dist_coeffs
    )

    # Convert rotation to angles
    rmat, _ = cv2.Rodrigues(rotation_vec)
    angles, _, _, _, _, _ = cv2.RQDecomp3x3(rmat)

    pitch, yaw, roll = angles

    return pitch, yaw, roll