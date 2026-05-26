def decide_action(gesture, gaze):
    """
    Combine gesture + gaze → robot action
    """

    # STOP condition
    if gesture == "PALM":
        return "STOP"

    # MOVE condition
    if gesture == "FIST":
        if gaze == "Left":
            return "FORWARD LEFT"
        elif gaze == "Right":
            return "FORWARD RIGHT"
        elif gaze == "Up":
            return "FORWARD"
        elif gaze == "Down":
            return "BACKWARD"
        else:
            return "FORWARD"

    return "IDLE"