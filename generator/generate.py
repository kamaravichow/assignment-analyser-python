# coding=utf-8
from __future__ import print_function
from PIL import Image, ImageFont, ImageDraw
import os
import shutil
import time


lable_dict = {0: '0', 1:'1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8:'8', 9:'9', 10:'=', 11:'+', 12:'-', 13:'×', 14: '÷'}

for value,char in lable_dict.items():
    print(value,char)
    train_images_dir = './train_images/' + str(value)
    if os.path.isdir(train_images_dir):
        shutil.rmtree(train_images_dir)
    os.makedirs(train_images_dir)
    

def generate_image(lable_dict, font_path, w=24, h=24, rotation =0):

    for value,char in lable_dict.items():
        img = Image.new('RGB', (w, h), "black")
        draw = ImageDraw.Draw(img)

        font = ImageFont.truetype(font_path, int(w * 0.9))
        font_width, font_height = draw.textsize(char, font)

        x = (w - font_width - font.getoffset(char)[0]) / 2
        y = (h - font_height - font.getoffset(char)[1]) / 2

        draw.text((x, y), char, (255,255,255), font)

        img = img.rotate(rotation)

        time_value = int(round(time.time() * 1000))
        img_path = "./train_images/{}/img-{}_r-{}_{}.png".format(value, value, rotation, time_value)
        img.save(img_path)


font_dir = './fonts/'

for font_name in os.listdir(font_dir):
    path_of_font = os.path.join(font_dir, font_name)
    
    for k in range(-10,10,1):
        generate_image(lable_dict, path_of_font, rotation=k)


