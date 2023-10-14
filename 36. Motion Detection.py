import cv2
import numpy as np

# Initialize video capture from your webcam (0 for default webcam)
cap = cv2.VideoCapture(0)

# Create a background subtractor object
bg_subtractor = cv2.createBackgroundSubtractorMOG2()

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    
    # Apply the background subtractor to the frame
    fg_mask = bg_subtractor.apply(frame)
    
    # Find contours in the foreground mask
    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Ignore small contours (noise)
        if cv2.contourArea(contour) < 200:
            continue
        
        # Draw a bounding box around moving objects
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Display the original frame with motion detection
    cv2.imshow("Motion Detection", frame)
    
    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
