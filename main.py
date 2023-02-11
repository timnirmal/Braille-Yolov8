from ultralytics import YOLO

model = YOLO("yolov8n.yaml")
model.train(data="datasets/data.yaml", epochs=5, imgsz=800, plots=True)
