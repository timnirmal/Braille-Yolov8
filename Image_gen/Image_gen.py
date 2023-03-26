import os

import cv2

folder = r"C:\Users\timni\PycharmProjects\Yolo\datasets\train\images"

# load each image in the folder
for filename in os.listdir(folder):
    img = cv2.imread(os.path.join(folder, filename))
    if img is not None:
        # blur the image
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        blur2 = cv2.blur(img, (5, 5))
        blur3 = cv2.medianBlur(img, 5)

        # medium level of blur
        blur4 = cv2.GaussianBlur(img, (9, 9), 0)
        blur5 = cv2.blur(img, (9, 9))
        blur6 = cv2.medianBlur(img, 9)

        # high level of blur
        blur7 = cv2.GaussianBlur(img, (15, 15), 0)
        blur8 = cv2.blur(img, (15, 15))
        blur9 = cv2.medianBlur(img, 15)

        # save the image with filename = filename + blurtype + blurlevel + .jpg (e.g. 0_2_jpg.rf.76b9c6cba32571b357830b5f3e74db1a_blur5.jpg) in respective folder
        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\low\gaussian\low_gaussian_" + filename,
                    blur)
        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\low\blur\low_blur" + filename, blur2)
        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\low\median\low_median" + filename, blur3)

        cv2.imwrite(
            r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\medium\gaussian\medium_gaussian_" + filename,
            blur4)
        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\medium\blur\medium_blur_" + filename,
                    blur5)
        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\medium\median\medium_median_" + filename,
                    blur6)

        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\high\gaussian\high_gaussian_" + filename,
                    blur7)
        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\high\blur\high_blur_" + filename, blur8)
        cv2.imwrite(r"C:\Users\timni\PycharmProjects\Yolo\datasets\sr\images\high\median\high_median_" + filename,
                    blur9)

        print(filename)
