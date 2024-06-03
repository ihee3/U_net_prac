##필요한 패키지 등록'
import os
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

dir_data = './EMdataset'

name_label = 'train-labels.tif'
name_input = 'train-volume.tif'

img_label = Image.open(os.path.join(dir_data, name_label))
img_input = Image.open(os.path.join(dir_data, name_input))

ny, nx = img_label.size
nframe = img_label.n_frames

## train, test, validation set 나누기
nframe_train = 24
nframe_val = 3
nframe_test = 3 

dir_save_train = os.path.join(dir_data, 'train') #train data가 저장될 디렉토리
dir_save_val = os.path.join(dir_data, 'val')
dir_save_test = os.path.join(dir_data, 'test')

#ditectoty generate
if not os.path.exists(dir_save_train):
    os.makedirs(dir_save_train)
    
if not os.path.exists(dir_save_val):
    os.makedirs(dir_save_val)
    
if not os.path.exists(dir_save_test):
    os.makedirs(dir_save_test)    

## 생성한 디렉토리에 데이터셋 나누어 저장하기
# random index
id_frame = np.arange(nframe)
np.random.shuffle(id_frame)

offset_nframe = 0

for i in range(nframe_train):
    img_label.seek(id_frame[i + offset_nframe])
    img_input.seek(id_frame[i + offset_nframe])
    
    label_ = np.asarray(img_label)
    input_ = np.asarray(img_input)
    
    np.save(os.path.join(dir_save_train, 'label_%03d.npy' %i), label_)
    np.save(os.path.join(dir_save_train, 'input_%03d.npy' %i), input_)

offset_nframe += nframe_train

for i in range(nframe_val):
    img_label.seek(id_frame[i + offset_nframe])
    img_input.seek(id_frame[i + offset_nframe])
    
    label_ = np.asarray(img_label)
    input_ = np.asarray(img_input)
    
    np.save(os.path.join(dir_save_val, 'label_%03d.npy' %i), label_)
    np.save(os.path.join(dir_save_val, 'input_%03d.npy' %i), input_)

offset_nframe += nframe_val

for i in range(nframe_test):
    img_label.seek(id_frame[i + offset_nframe])
    img_input.seek(id_frame[i + offset_nframe])
    
    label_ = np.asarray(img_label)
    input_ = np.asarray(img_input)
    
    np.save(os.path.join(dir_save_test, 'label_%03d.npy' %i), label_)
    np.save(os.path.join(dir_save_test, 'input_%03d.npy' %i), input_)