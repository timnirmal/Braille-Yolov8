# get images from the folder

images = []
for img in os.listdir("images"):
    images.append(cv2.imread("images/" + img))

# turn images to 640x640 by padding
images = [cv2.copyMakeBorder(img, 0, 640 - img.shape[0], 0, 640 - img.shape[1], cv2.BORDER_CONSTANT, value=[0, 0, 0]) for img in images]



# predict
results = model.predict(source=images, save=True, save_txt=True)  # save predictions as labels

