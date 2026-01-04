# Fire Detector System

**Developed by:** Divyanshu Yadav

### 📖 Description
This project is a real-time **Fire Detection System** built using Python. It utilizes the webcam to detect flames (specifically lighter flames) by analyzing color and brightness levels in the video feed.

Unlike simple color detectors that trigger on any yellow object, this system uses a smart logic: it looks for a **bright white core inside a yellow halo**, which mimics the actual structure of a flame. It features a graphical user interface (GUI) to start the application and plays an audio alarm upon detection.

### ✨ Features
* **Interactive GUI:** A dark-themed welcome screen with a "Start Detection" button.
* **Smart Detection:** Reduces false alarms by distinguishing between static yellow objects and actual glowing flames.
* **Audio Alert:** Plays an alarm sound (`alarm.mp3`) immediately when a flame is detected.
* **High Resolution:** Runs the camera feed at **1024x768** resolution for better clarity.
* **On-Screen Branding:** Displays the developer's name on the live camera feed.

### 🛠️ Tech Stack
* **Language:** Python
* **Libraries:**
  * `OpenCV` (Computer Vision)
  * `NumPy` (Data processing)
  * `Pygame` (Audio playback)
  * `Tkinter` (GUI)

### ⚙️ Prerequisites
Before running the script, ensure you have Python installed. Then, install the required libraries using pip:

```bash
pip install opencv-python numpy pygame
```

🚀 How to Run
**Download the Code**: Save the main Python script (main.py) in a folder.

**Add Audio File**: Place an audio file named alarm.mp3 in the same folder.

**Run the Script**: Open your terminal or command prompt and run:

```Bash

python main.py
```
**Start**: Click the "START DETECTION" button on the window that appears.

**Exit**: Press q to stop the camera and close the application.

### 🧠 How It Works
The system processes the video feed in three steps:

* Yellow Mask: It identifies yellow and orange colors in the frame (the outer part of a flame).

* White Mask: It identifies extremely bright/white pixels (the hot core of a flame).

* Combination Logic: It only triggers the alarm if the White Core is found overlapping or inside the Yellow Area.

👨‍💻 Author
Divyanshu Yadav B.Tech (CSE - AI)

