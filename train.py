from ultralytics import YOLO

# Load model
model = YOLO("yolov8n.yaml")

# Train model
model.train(data="datasets/data.yaml", epochs=5, imgsz=800, plots=True)
