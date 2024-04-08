import cv2
import numpy as np

def main():
    # Load the video
    cap = cv2.VideoCapture('video.mp4')

    #also applicable for live video
    

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        # Resize the frame to fit your screen
        frame = cv2.resize(frame, (1280, 720))  # Adjust width and height as needed

        # Convert the frame to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define range of green color in HSV
        lower_green = np.array([45, 50, 50])
        upper_green = np.array([60, 255, 255])

        # Threshold the HSV image to get only green colors
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Find contours in the mask
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Draw a bounding box around the largest contour (presumably the ball)
        if contours:
            max_contour = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(max_contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the frame
        cv2.imshow('Frame', frame)

        # Press 'q' to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
