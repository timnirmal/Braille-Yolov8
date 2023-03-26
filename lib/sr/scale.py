import os

import cv2
import numpy as np
import torch

from .RRDBNet_arch import RRDBNet as arch

model_path = 'models/RRDB_ESRGAN_x4.pth'
# device = torch.device('cuda')  # if you want to run on CPU, change 'cuda' -> cpu
device = torch.device('cpu')

model = arch(3, 3, 64, 23, gc=32)
model.load_state_dict(torch.load(model_path), strict=True)
model.eval()
model = model.to(device)

print('Model path {:s}. \nTesting...'.format(model_path))

# check if the path exists
if not os.path.exists('results'):
    os.makedirs('results')
    print("Created results folder")


def scale_image(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image = image * 1.0 / 255
    image = torch.from_numpy(np.transpose(image[:, :, [2, 1, 0]], (2, 0, 1))).float()
    image_LR = image.unsqueeze(0)
    image_LR = image_LR.to(device)

    print('img_LR size', image_LR.size())

    with torch.no_grad():
        output = model(image_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    output = (output * 255.0).round()

    # save the image
    cv2.imwrite('results/{:s}_rlt.png'.format("0_2_jpg.rf.76b9c6cba32571b357830b5f3e74db1a"), output)

    return output


test_img_name = r"C:\Users\timni\PycharmProjects\Yolo\datasets\super_resolution\0_2_jpg.rf.76b9c6cba32571b357830b5f3e74db1a.jpg"

# output = scale_image(test_img_name)
