# Hand Detection and Tracking with OpenCV and MediaPipe

This project implements real-time hand detection and tracking using OpenCV and MediaPipe. The application captures video from your webcam, detects hands, and draws landmarks for key points on the hand using MediaPipe's hand tracking solution.

## 1. Features

* Real-time Hand Detection: Detects up to 2 hands in the video stream.
* Landmark Drawing: Draws hand landmarks and connections between key points.
* Customizable: You can modify detection and tracking confidence, hand count, and more.
* FPS Display: Shows the frames per second (FPS) for real-time performance monitoring.
* Hand Count: Displays the number of detected hands on the screen.

### Requirements


* Python 3.x
* OpenCV (opencv-python)
* MediaPipe (mediapipe)

Install the required dependencies:

```bash
pip install opencv-python mediapipe
```

### How to Use

1. Clone this repository to your local machine:
```bash
git clone https://github.com/your-username/hand-detection-tracking.git
```
2. Navigate to the project directory:
```bash
cd hand-detection-tracking
```
3. Run the hand_detection.py file:
```bash
python hand_detection.py
```

### Code Explanation

**Class**: handDetection
This class is used to initialize and manage the hand detection model using MediaPipe and OpenCV.

**init(self, mode=False, maxHands=2, model=1, minDetection=0.5, minTracking=0.5):**

* mode: Static image mode or video mode.
* maxHands: Maximum number of hands to detect.
* model: Hand tracking model type.
* minDetection: Minimum confidence threshold for detection.
* minTracking: Minimum confidence threshold for tracking hands.

**findHand(self, frame, draw=True):**

This method processes the video frame, detects hands, and optionally draws landmarks on the hands.

**findPosition(self, frame, draw=True):**

This method returns the position of key hand landmarks. The IDs for landmarks like the thumb, index finger, etc., are recorded.

**Main Function:**

The main() function initializes the video capture, detects hands in real time, and displays the frame with drawn landmarks and hand count.

**FPS Display:**

Real-time FPS is displayed on the screen to monitor the performance of the hand detection.

**Hand Count:**

Displays the total number of hands detected at any given time.

## Example Usage

When you run the program, it captures live video from your webcam, detects hands in the frame, and draws landmarks on each detected hand.

## Customization

You can easily modify the parameters in the handDetection class to:

* Change the number of hands to detect.
* Ajust detection and tracking confidence thresholds.
* Customize the drawing of landmarks.

## Contributing

Feel free to fork the repository and submit pull requests if you would like to improve the project or add new features.

## License

This project is open-source and available under the MIT License.
