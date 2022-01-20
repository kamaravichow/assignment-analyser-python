import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
import PIL
import matplotlib.pyplot as plt
import os
import shutil
from numpy.core.records import array
from numpy.core.shape_base import block
import time

from rows import img2rows


def img_y_shadow(img_b):
    (h, w) = img_b.shape

    a=[0 for z in range(0,h)]

    for i in range(0,h):
        for j in range(0,w):
            if img_b[i,j] == 255:
                a[i]+=1

    return a

def img_show_array(a):
    plt.imshow(a)
    plt.show()

def show_shadow(arr, direction= 'x'):

    a_max = max(arr)
    if direction == 'x':
        a_shadow = np.zeros((a_max, len(arr)), dtype=int)
        for i in range(0, len(arr)):
            if arr[i]==0:
                continue

            for j in range(0, arr[i]):
                a_shadow[j][i] = 255
    elif direction == 'y':
        a_shadow = np.zeros((len(arr), a_max), dtype=int)
        for i in range(0, len(arr)):
            if arr[i]==0:
                continue
            
            for j in range(0, arr[i]):
                a_shadow[i][j] = 255
            
    img_show_array(a_shadow)

img_question = 'question.png'
img = cv2.imread(img_question, 0)
thresh = 200

ret, img_b = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY_INV)

# plt.imshow(img_b)
# plt.show()

img_y_shadow_a = img_y_shadow(img_b)
show_shadow(img_y_shadow_a, 'y')


(img_h, img_w) = img.shape
row_mark_boxs = img2rows(img_y_shadow_a, img_w, img_h)
print(row_mark_boxs)

def cut_img(img, mark_boxs):
    img_items = []

    for i in range(0, len(mark_boxs)):
        img_org = img.copy()
        box = mark_boxs[i]

        img_item = img_org[box[1]:box[3], box[0]:box[2]]
        img_items.append(img_item)
    
    return img_items

def save_imgs(dir_name, imgs):
    if os.path.exists(dir_name):
        shutil.rmtree(dir_name)
    
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

    img_paths = []

    for i in range(0, len(imgs)):
        file_path = dir_name + '/part_'+ str(i)+ '.jpg'
        cv2.imwrite(file_path, imgs[i])
        img_paths.append(file_path)
    
    return img_paths

row_imgs = cut_img(img, row_mark_boxs)
imgs = save_imgs('rows', row_imgs)
print(imgs)

kernel = np.ones((3, 3), np.uint80)
row_img_b = cv2.dilate(img_b, kernel, iterations=6)
