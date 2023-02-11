from ultralytics import YOLO

model = YOLO("model.pt")
# It'll use the data yaml file in model.pt if you don't set data.
model.val(data="datasets/data.yaml")
# model.val()
# or you can set the data you want to val
