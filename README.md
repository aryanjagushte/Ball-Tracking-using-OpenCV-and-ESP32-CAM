# Ball-Tracking-using-OpenCV-and-ESP32-CAM


# 1. Ball detection

## Introduction
This Python script detects and tracks objects of a specific color in a video stream or a recorded video file. It utilizes the OpenCV library for computer vision tasks.

## Requirements
- Python 3.x
- OpenCV library
- Numpy library

## Usage
1. Clone or download the repository to your local machine.
2. Ensure that you have Python installed on your system.
3. Install the required libraries using pip:
4. Place the video file in the same directory as the Python script (if using a recorded video, download here https://www.pexels.com/video/a-boy-playing-tennis-8224589/).
5. Run the Python script using the following command:
6. Press the 'q' key to exit the program.

## Customization
- Adjust the HSV color range in the code to detect objects of different colors.
- Modify the resize dimensions to fit your screen resolution.

This principle is fundamental in robotic perception systems as it allows the robot to identify objects of interest based on their color characteristics. By defining appropriate color ranges, the robot can differentiate between objects and background, and can be used in various tasks such as object detection, tracking, and localization.



# 2. ESP32-CAM ball detection in Live

## Introduction
This Python script detects and tracks a green ball in a live video stream from an IP camera. It utilizes the OpenCV library for computer vision tasks.

## Requirements
- Python 3.x
- OpenCV library
- Numpy library

## Usage
1. Ensure that you have Python installed on your system.
2. Install the required libraries using pip:
3. Replace the `url` variable in the script with the URL of your IP camera's stream.
4. Run the Python script using the following command:
5. Press the 'q' key to exit the program.

## Customization
- Adjust the HSV color range in the code to detect objects of different colors.
- Modify the minimum contour area threshold to detect smaller or larger objects.

It is essential for robots to interact with their surroundings in real-time. By detecting and tracking objects of interest, such as balls, obstacles, or targets, the robot can navigate autonomously, manipulate objects, or perform specific tasks. 


# 3. Tracker Bar Ball Detection

## Introduction
This Python script allows users to select a color range using trackbars in the HSV color space for object detection in a live video feed from a webcam. It utilizes OpenCV for image processing tasks.

## Requirements
- Python 3.x
- OpenCV library

## Usage
1. Ensure that you have Python installed on your system.
2. Install the OpenCV library using pip:
3. Run the Python script using the following command:
4. Adjust the trackbars to select the desired color range.
5. Press the 'q' key to exit the program.

## Customization
- Modify the range_filter variable to switch between different color spaces (e.g., 'HSV', 'RGB', etc.).
- Adjust the trackbars to select the desired color range for object detection.

This feature enhances the flexibility of robotic perception systems, enabling them to operate effectively in diverse environments and lighting conditions. By adjusting the color range parameters in real-time, the robot can adapt its object detection capabilities to different scenarios, ensuring robust performance across varying contexts.


