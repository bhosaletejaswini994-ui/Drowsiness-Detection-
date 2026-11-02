# 😴 Drowsiness Detection System Using Python

## 📌 Project Overview

The **Drowsiness Detection System** is a real-time computer vision application developed using Python, OpenCV, and MediaPipe. It detects whether a person's eyes are closed for a specific duration and identifies possible signs of drowsiness.

The system uses facial landmarks to calculate the Eye Aspect Ratio (EAR). If the eyes remain closed for more than 2 seconds, an audio alarm is triggered to alert the person and help prevent accidents.

## 🎯 Project Objectives

- Detect a person's face using MediaPipe Face Mesh.
- Track eye movements using facial landmarks.
- Calculate the Eye Aspect Ratio (EAR).
- Identify prolonged eye closure.
- Trigger an automatic sound alarm when drowsiness is detected.
- Monitor eye activity in real time using a webcam.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **OpenCV** – Real-time video capture and image processing.
- **MediaPipe** – Facial landmark detection and eye tracking.
- **Math** – Calculate distances between eye landmarks.
- **Time** – Measure how long the eyes remain closed.
- **Threading** – Run the alarm in the background.
- **Winsound** – Generate an audio alert on Windows.

## ⚙️ How It Works

1. The webcam captures live video.
2. MediaPipe Face Mesh detects facial landmarks.
3. The system identifies specific points around both eyes.
4. Eye Aspect Ratio (EAR) is calculated using the distance between eye landmarks.
5. If the EAR falls below `0.22`, the system considers the eyes closed.
6. It checks whether the eyes remain closed for at least 2 seconds.
7. If prolonged eye closure is detected, an audio alarm starts.
8. When the eyes open again, the alarm stops and the status changes to **AWAKE**.

## 📊 Eye Aspect Ratio (EAR)

The Eye Aspect Ratio helps determine whether the eyes are open or closed.

**Formula:**

EAR = (Vertical Distance 1 + Vertical Distance 2) / (2 × Horizontal Distance)

- Higher EAR value: Eyes are generally open.
- Lower EAR value: Eyes are generally closed.

## 📂 Project Structure

```text
Drowsiness-Detection/
│
├── DrowsinessDetection.py
│
├── README.md
│
└── requirements.txt
```

## 📦 Installation

**Step 1: Clone the repository**

```bash
git clone https://github.com/your-username/Drowsiness-Detection.git
```

**Step 2: Open the project folder**

```bash
cd Drowsiness-Detection
```

**Step 3: Install required libraries**

```bash
pip install opencv-python mediapipe
```

**Step 4: Run the Python application**

```bash
python DrowsinessDetection.py
```

## 🎮 Controls

- **Q** – Press Q to close the application.
- **Webcam** – Used for real-time face and eye detection.
- **Audio Alarm** – Automatically activates when prolonged eye closure is detected.

## 🏢 Real-World Applications

This project demonstrates a concept that can be useful in:

- 🚗 Driver Drowsiness Monitoring Systems
- 🚛 Transportation and Logistics Companies
- 🏭 Industrial Worker Safety Monitoring
- 🚌 Public Transport Safety Systems
- 🖥️ Workplace Alertness Monitoring

## 🚀 Future Improvements

- Add face detection for multiple people.
- Create a graphical user interface using CustomTkinter.
- Add a drowsiness detection history and report.
- Display a warning when the face is not visible for a long time.
- Improve detection accuracy under different lighting conditions.
- Add an option to customize the alarm duration.

## ⚠️ Limitations

- Requires a working webcam.
- Performance may vary depending on lighting and camera quality.
- Eye closure alone cannot reliably determine whether someone is asleep or medically drowsy.
- This is an educational prototype and should not be used as the sole safety system in vehicles or industrial environments.

## 👩‍💻 Author

**Tejaswini Bhosale**

Python | Computer Vision | OpenCV | MediaPipe

## ⭐ Acknowledgement

This project was developed as a practical learning project to understand computer vision, facial landmark detection, eye tracking, and real-time alert systems using Python.

If you find this project interesting, don't forget to give it a ⭐ on GitHub!
