import uuid
import cv2
import os

uuid.uuid1()

VER_PATH = os.path.join('controllers','FaceId','application_data', 'input_image_lawyer')

# Establish a connection to the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    # Check if frame is None
    if not ret:
        print("Failed to capture frame from the webcam")
        break
    
    # Cut down frame to 250x250px
    frame = frame[120:120+250, 200:200+250, :]
    
    cv2.imshow('Press "v" to input face', frame)
    key = cv2.waitKey(1)
    
    # Collect anchor
    if key & 0xFF == ord('v'):
        imgname = os.path.join(VER_PATH, '{}.jpg'.format(uuid.uuid1()))
        cv2.imwrite(imgname, frame)
        break

# Release webcam
cap.release()

# Close the image show frame
cv2.destroyAllWindows()
