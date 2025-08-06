# 🖱️ Virtual Mouse Using Hand Gestures

Control your computer mouse with just your hand movements! This project uses **OpenCV**, **MediaPipe**, and **PyAutoGUI** to turn your webcam into a virtual mouse controller using real-time hand gesture recognition.

---

## ✨ Features

- 🎯 **Move Cursor**: Control the mouse pointer with your index finger.
- 👆 **Left Click**: Bring your thumb and index finger close together to simulate a left click.
- 🤜 **Right Click**: Bring your index and middle fingers together for a right click.
- ❌ **Close Window**: Touch your thumb and pinky finger to trigger `Alt + F4` and close the active window.
- ⏱️ **Time Control**: Set a time limit for how long the virtual mouse should run.

---


## 🛠️ Tech Stack

| Tool        | Purpose                             |
|-------------|-------------------------------------|
| `OpenCV`    | Video capture and image processing  |
| `MediaPipe` | Hand tracking and landmarks         |
| `PyAutoGUI` | Control mouse & keyboard actions    |
| `NumPy`     | Distance calculations               |

---

## 🧠 How It Works

1. Captures webcam feed using OpenCV.
2. Detects hand landmarks using MediaPipe.
3. Tracks fingers in real-time and performs actions:
   - Moves cursor to index finger location.
   - Clicks or closes window based on finger distances.
4. Stops execution after user-defined time or on pressing `q`.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kumarvarun3162/virtual-mouse-hand-gesture.git
cd virtual-mouse-hand-gesture

```

### 2. Run tha app
```bash
python app.py
