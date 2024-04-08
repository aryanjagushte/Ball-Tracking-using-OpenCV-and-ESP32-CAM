import cv2

def main():
    range_filter = 'HSV'  # Using HSV color space

    camera = cv2.VideoCapture(0)  # Open webcam

    cv2.namedWindow("Trackbars", 0)

    for i in ["MIN", "MAX"]:
        v = 0 if i == "MIN" else 255
        for j in range_filter:
            cv2.createTrackbar("%s_%s" % (j, i), "Trackbars", v, 255, lambda x: None)

    while True:
        ret, image = camera.read()
        if not ret:
            break

        frame_to_thresh = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        v1_min = cv2.getTrackbarPos("H_MIN", "Trackbars")
        v2_min = cv2.getTrackbarPos("S_MIN", "Trackbars")
        v3_min = cv2.getTrackbarPos("V_MIN", "Trackbars")
        v1_max = cv2.getTrackbarPos("H_MAX", "Trackbars")
        v2_max = cv2.getTrackbarPos("S_MAX", "Trackbars")
        v3_max = cv2.getTrackbarPos("V_MAX", "Trackbars")

        thresh = cv2.inRange(frame_to_thresh, (v1_min, v2_min, v3_min), (v1_max, v2_max, v3_max))

        preview = cv2.bitwise_and(image, image, mask=thresh)
        cv2.imshow("Preview", preview)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
