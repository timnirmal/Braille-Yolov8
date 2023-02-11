from ultralytics import YOLO

# Load model
model = YOLO("model.pt")

# Validate model
model.val(data="datasets/data.yaml")

