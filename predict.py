import cv2
from ultralytics import YOLO

model = YOLO("model.pt")

im2 = cv2.imread("test.jpg")
results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels
print(results)
