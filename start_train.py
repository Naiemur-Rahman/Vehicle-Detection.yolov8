from ultralytics import YOLO

# 1. Load the model
model = YOLO('yolov8n.pt') 

# 2. Run prediction, show it live, AND save the output
# Replace the URL with a specific traffic video link
model.predict(
    source='https://www.youtube.com/watch?v=Zt2j8s9nXoE', 
    show=True, 
    save=True,
    conf=0.5  # Only show detections it's 50% sure about
)
