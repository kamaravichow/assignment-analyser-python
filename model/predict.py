import imp
from unittest import result


import cv2
import numpy as np
from build_model import create_model

img1 = cv2.imread('img1.png', 0)
img2 = cv2.imread('img2.png', 0)

imgs = np.array([img1, img2])

print(imgs)

model = create_model()

model.load_weights('checkpoint/char_checkpoint')

class_name = np.load('class_name.npy')

predicted = model.predict(imgs)

results = []
for predict in predicted:
    index = np.argmax(predict)
    result = class_name[index]
    results.append(result)

print(results)