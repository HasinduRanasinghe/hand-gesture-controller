"""
Configuration file for Hand Gesture Controller
"""

class Config:
    # Camera Settings
    CAMERA_INDEX = 0  # 0 for default camera, 1 for external camera
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480
    
    # Hand Detection Settings
    MAX_HANDS = 1  # Number of hands to detect (1 or 2)
    MIN_DETECTION_CONFIDENCE = 0.7  # 0.0 to 1.0 (higher = more strict)
    MIN_TRACKING_CONFIDENCE = 0.7   # 0.0 to 1.0 (higher = more strict)
    
    # Gesture Control Settings
    GESTURE_COOLDOWN = 0.5  # Seconds between gesture actions
    CURSOR_SMOOTHING = 7    # Higher = smoother but slower cursor (1-15)
    
    # Gesture Sensitivity Thresholds
    PINCH_THRESHOLD = 30    # Distance for pinch gesture (pixels)
    VERTICAL_MOVE_THRESHOLD = 20  # Minimum vertical movement for scroll
    HORIZONTAL_MOVE_THRESHOLD = 50  # Minimum horizontal movement for tab switch
    
    # Scroll Settings
    SCROLL_AMOUNT = 25  # Pixels to scroll per gesture
    
    # Display Settings
    SHOW_FPS = True
    SHOW_HAND_LANDMARKS = True
    SHOW_GESTURE_INFO = True
    WINDOW_NAME = "Hand Gesture Controller"
    
    # Colors (BGR format)
    TEXT_COLOR = (0, 255, 0)
    LANDMARK_COLOR = (0, 255, 0)
    CONNECTION_COLOR = (255, 0, 0)
    
    # Performance Settings
    ENABLE_GPU = False  # Set to True if you have compatible GPU
    
    # Gesture Enable/Disable
    ENABLE_CURSOR_MOVE = True
    ENABLE_LEFT_CLICK = True
    ENABLE_RIGHT_CLICK = True
    ENABLE_SCROLL = True
    ENABLE_VOLUME_CONTROL = True
    ENABLE_MEDIA_CONTROL = True
    ENABLE_TAB_SWITCH = True
    ENABLE_GESTURE_MODE = True  # Open palm to toggle gesture recognition on/off