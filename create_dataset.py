import pandas as pd
import numpy as np
import tensorflow as tf
import os
import pickle
from PIL import Image
from tensorflow import keras

IMG_WIDTH=150
IMG_HEIGHT=150
image_size=(IMG_WIDTH,IMG_HEIGHT)


def create_dataset(img_folder):
    img_data_array = []
    class_name = []
    i = 0

    for dir1 in os.listdir(img_folder):
        for file in os.listdir(os.path.join(img_folder, dir1)):
            image_path = os.path.join(img_folder, dir1, file)
            image = np.array(Image.open(image_path).convert('RGB').resize((IMG_WIDTH, IMG_HEIGHT), Image.ANTIALIAS))
            img_data = image.astype('float32')
            img_data /= 255
            img_data_array.append(img_data)
            class_name.append(dir1)
            i = i + 1
            print(i)

    return img_data_array, class_name

img_folder=r'C:/Users/polco/Documents/UNI/TFG/Mushrooms'
img_data, class_name=create_dataset(img_folder)

img_data=np.array(img_data)
target_dict={k: v for v, k in enumerate(np.unique(class_name))}
target_val=  [target_dict[class_name[i]] for i in range(len(class_name))]
target_val=np.array(target_val)

with open ('C:/Users/polco/Documents/UNI/TFG/data_img_pickle/img_data','wb') as file_pi:
    pickle.dump(img_data,file_pi)
with open ('C:/Users/polco/Documents/UNI/TFG/data_img_pickle/img_labels','wb') as file_pi:
    pickle.dump(target_val,file_pi)
with open ('C:/Users/polco/Documents/UNI/TFG/data_img_pickle/img_dict','wb') as file_pi:
    pickle.dump(target_dict,file_pi)
