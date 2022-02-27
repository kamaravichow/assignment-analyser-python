import pathlib
from build_model import create_model
import tensorflow as tf
import numpy as np
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential
import pathlib
import cv2


dataset_dir = pathlib.Path('F:/Desktop/homework-analyser-python/generator/train_images')
print(dataset_dir.name)

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_dir,
    color_mode="grayscale",
    image_size=(24,24),
    batch_size=32
)

class_names = train_ds.class_names

np.save("class_name.npy", class_names)

AUTOTUNE = tf.data.experimental.AUTOTUNE
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)

model = create_model()

model.fit(train_ds, epochs=10)

model.save_weights('checkpoint/char_checkpoint')

