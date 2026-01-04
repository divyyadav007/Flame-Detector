import cv2
import numpy as np
import pygame

# 1. Initialize Audio
pygame.mixer.init()
alarm_file = "flame.mp3"

def play_alarm():
    if not pygame.mixer.music.get_busy():
        try:
            pygame.mixer.music.load(alarm_file)
            pygame.mixer.music.play()
            print("!!! LIGHTER FLAME DETECTED !!!")
        except Exception as e:
            print(f"Error: {e}")

cap = cv2.VideoCapture(0)

print("Advance Flame Detection Started...")
print("Logic: Looking for WHITE core inside YELLOW flame.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    # 1. Blur to remove noise
    blur = cv2.GaussianBlur(frame, (15, 15), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    
    # --- STEP 1: Detect the YELLOW/ORANGE Halo (Flame body) ---
    lower_fire = np.array([18, 50, 50], dtype="uint8")
    upper_fire = np.array([35, 255, 255], dtype="uint8")
    mask_yellow = cv2.inRange(hsv, lower_fire, upper_fire)
    
    # --- STEP 2: Detect the WHITE Core (The hot center) ---
    # High Brightness (Value > 240) and Low Saturation (White has low color)
    lower_white = np.array([0, 0, 240], dtype="uint8")
    upper_white = np.array([180, 50, 255], dtype="uint8")
    mask_white = cv2.inRange(hsv, lower_white, upper_white)
    
    # --- STEP 3: Logic - Fire exists if White is INSIDE Yellow ---
    # Hum yellow mask ko thoda expand (dilate) karte hain taki connection check ho sake
    kernel = np.ones((5, 5), np.uint8)
    mask_yellow_dilated = cv2.dilate(mask_yellow, kernel, iterations=3)
    
    # Check intersection: Jahan White aur Yellow overlap/touch kar rahe hain
    mask_combined = cv2.bitwise_and(mask_white, mask_yellow_dilated)
    
    # Contours check karo combined mask par
    contours, _ = cv2.findContours(mask_combined, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    flame_detected = False
    
    for contour in contours:
        area = cv2.contourArea(contour)
        
        # Area filter: Lighter ki flame ka white core chota hota hai (e.g., 20-500 pixels)
        # Agar torch hai to wo bada hoga, agar noise hai to < 10 hoga.
        if 10 < area < 500: 
            x, y, w, h = cv2.boundingRect(contour)
            
            # Draw rectangle around the white core
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            flame_detected = True
            
    if flame_detected:
        play_alarm()
        cv2.putText(frame, "FLAME ON", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Original", frame)
    # Aap debugging ke liye niche wali lines uncomment kar sakte hain:
    # cv2.imshow("Yellow Mask", mask_yellow)
    # cv2.imshow("White Mask", mask_white)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()