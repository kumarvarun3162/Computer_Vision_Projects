import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize MediaPipe and OpenCV
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Set up webcam
cap = cv2.VideoCapture(0)

screen_width, screen_height = pyautogui.size()

# Define distance thresholds for each action
CLICK_THRESHOLD = 40
RIGHT_CLICK_THRESHOLD = 50
CLOSE_WINDOW_THRESHOLD = 50

def calculate_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return np.hypot(x2 - x1, y2 - y1)

def perform_click_action(index_x, index_y, thumb_x, thumb_y):
    """Perform a left-click if the index and thumb are close enough."""
    if calculate_distance(index_x, index_y, thumb_x, thumb_y) < CLICK_THRESHOLD:
        pyautogui.click()

def perform_right_click_action(index_x, index_y, middle_x, middle_y):
    """Perform a right-click if the index and middle fingers are close enough."""
    if calculate_distance(index_x, index_y, middle_x, middle_y) < RIGHT_CLICK_THRESHOLD:
        pyautogui.rightClick()

def perform_close_window_action(thumb_x, thumb_y, pinky_x, pinky_y):
    """Close the window if the thumb and pinky fingers are close enough."""
    if calculate_distance(thumb_x, thumb_y, pinky_x, pinky_y) < CLOSE_WINDOW_THRESHOLD:
        pyautogui.hotkey('alt', 'f4')

# Get time limit from the user
time_limit = int(input("Enter the time limit (in seconds) to run the virtual mouse: "))
start_time = time.time()

while cap.isOpened():
    success, image = cap.read()
    if not success:
        break
 
    # Check if the time limit has been reached
    elapsed_time = time.time() - start_time
    if elapsed_time > time_limit:
        print("Time limit reached. Exiting...")
        break

    # Flip the image horizontally for a later selfie-view display
    image = cv2.flip(image, 1)
    # Convert the BGR image to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Process the image and detect hands
    results = hands.process(image_rgb)

    # Draw hand annotations on the image and control the mouse
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            # Draw hand landmarks

            # Get landmark coordinates for relevant fingers
            index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            middle_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
            pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

            # Convert coordinates to screen size
            index_x, index_y = int(index_finger_tip.x * screen_width), int(index_finger_tip.y * screen_height)
            thumb_x, thumb_y = int(thumb_tip.x * screen_width), int(thumb_tip.y * screen_height)
            middle_x, middle_y = int(middle_finger_tip.x * screen_width), int(middle_finger_tip.y * screen_height)
            pinky_x, pinky_y = int(pinky_tip.x * screen_width), int(pinky_tip.y * screen_height)

            # Move mouse to index finger position
            pyautogui.moveTo(index_x, index_y)

            # Perform actions based on finger distances
            perform_click_action(index_x, index_y, thumb_x, thumb_y)
            perform_right_click_action(index_x, index_y, middle_x, middle_y)
            perform_close_window_action(thumb_x, thumb_y, pinky_x, pinky_y)

    # Display the webcam feed
    cv2.imshow("Virtual Mouse", image)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
