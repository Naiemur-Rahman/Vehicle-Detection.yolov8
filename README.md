🚦 Traffic Vehicle Detection with YOLOv8
This project implements real-time vehicle detection using the YOLOv8 (You Only Look Once) architecture. It is designed to identify and classify various vehicle types (Ambulance, Bus, CNG, etc.) from static images and live YouTube streams.
🛠️ Prerequisites
Python 3.10+ (Recommended)
Hardware: AMD Ryzen 5 5500 (CPU-based inference)
RAM: 16GB
🚀 Step-by-Step Setup
1. Project Organization
Place your data.yaml, train/, and test/ folders in the root directory. Ensure your data.yaml points to the correct local paths:
-----------yaml---------------
path: C:/Your/Project/Path
train: train/images
val: train/images
Use code with caution.

2. Environment Setup
To avoid system-wide conflicts, always use a Virtual Environment:
-----------powershell-----------
# Create the environment
python -m venv venv

# Enable script execution (if blocked)
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Activate the environment
.\venv\Scripts\activate
Use code with caution.

3. Installation
Install the Ultralytics engine and YouTube support:
-------------powershell--------------
pip install ultralytics yt-dlp
Use code with caution.

4. Running Detection
Create a file named start_train.py and run it:
--------------python-----------------
from ultralytics import YOLO

model = YOLO('yolov8n.pt') 
model.predict(source='https://www.youtube.com', show=True, save=True)
Use code with caution.

⚠️ Challenges & Solutions
During the development of this project, I encountered several critical system errors. Here is how they were resolved:
1. System Crash & File Corruption
Problem: My PC restarted during the initial pip install. This caused a SyntaxError: source code string cannot contain null bytes because the internal library files were only half-written.
Solution: I created a Virtual Environment (venv). This bypassed the corrupted system files and allowed me to install a "clean" copy of the libraries in an isolated folder.
2. PowerShell Security Restrictions
Problem: I received an UnauthorizedAccess error when trying to activate my environment (activate.ps1 cannot be loaded).
Solution: I used Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process to temporarily allow script running for my development session.
3. 'yolo' Command Not Recognized
Problem: The terminal didn't recognize the yolo shortcut even after installation.
Solution: I switched to using python -m ultralytics or running direct Python scripts, which is more reliable on Windows systems.
4. CPU Limitations
Problem: I do not have a dedicated Nvidia GPU, leading to slow processing.
Solution: I used the yolov8n.pt (Nano) model and specified device='cpu' to ensure the project runs smoothly on my Ryzen 5 processor.
📊 Results
The processed videos are saved in runs/detect/predict/. The model successfully identifies 11 different classes of vehicles common in traffic environments.


