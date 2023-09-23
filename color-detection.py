import cv2
import numpy as np
import time  

color_ranges = {
    "red": ((0, 100, 100), (10, 255, 255)),
    "orange": ((11, 100, 100), (20, 255, 255)),
    "yellow": ((21, 100, 100), (30, 255, 255)),
    "green": ((31, 100, 100), (85, 255, 255)),
    "blue": ((86, 100, 100), (130, 255, 255)),
    "purple": ((131, 100, 100), (160, 255, 255)),
    "pink": ((161, 100, 100), (179, 255, 255)),
    "white": ((0, 0, 200), (179, 30, 255)),
    "black": ((0, 0, 0), (179, 255, 30)),
}

def get_color_name(hsv_color):
    for color_name, (lower, upper) in color_ranges.items():
        if lower[0] <= hsv_color[0] <= upper[0] \
            and lower[1] <= hsv_color[1] <= upper[1] \
            and lower[2] <= hsv_color[2] <= upper[2]:
            return color_name
    return "unknown"


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
last_color = "unknown"  

while True:

    ret, frame = cap.read()
    if not ret:
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mean_color = cv2.mean(hsv_frame)[:3]

    color_name = get_color_name(mean_color)

    
    if color_name != last_color:
        print("Detected Color:", color_name)
        last_color = color_name

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
