from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO("model.pt")
# accepts all formats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcam
# results = model.predict(source="0")
# results = model.predict(source="folder", show=True) # Display preds. Accepts all YOLO predict arguments

# # from PIL
# im1 = Image.open("test.jpg")
# results = model.predict(source=im1, save=True)  # save plotted images
# print(results)
# print()
# print()

# # show image in opencv
# cv2.imshow("test", cv2.imread("test.jpg"))
# cv2.waitKey(0)
# # add label to image by results
# cv2.imshow("test", model.add_labels(cv2.imread("test.jpg"), results))
# cv2.waitKey(0)
#

# from ndarray
im2 = cv2.imread("test.jpg")
results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels
print(results)
print()
print()
#
# # from list of PIL/ndarray
# results = model.predict(source=[im1, im2])
#
# print(results)
# print()
# print()