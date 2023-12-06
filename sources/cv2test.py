import cv2

# Start the camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Camera could not be opened.")
    exit()

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Press 'q' or 'Q' to exit the loop
        if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == ord('Q'):
            break
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # When everything is done, release the capture
    cap.release()
    cv2.destroyAllWindows()
