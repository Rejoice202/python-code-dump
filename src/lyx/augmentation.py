"""
数据增强
"""
import xml.etree.ElementTree as ET
import os
import numpy as np
from PIL import Image
import shutil
import imgaug as ia
from imgaug import augmenters as iaa


ia.seed(1)


if __name__ == "__main__":
#IMG_DIR = "/home/ubuntu/roolar_augu/guiwai/0_resize"
    #AUG_TRAIN_DIR = "/home/ubuntu/roolar_augu/guiwai/0_resize/train/0.normal"
    #AUG_TEST_DIR = "/home/ubuntu/roolar_augu/guiwai/0_resize/test/0.normal"
    #AUG_VALID_DIR = "/home/ubuntu/roolar_augu/guiwai/0_resize/valid/0.normal"
    IMG_DIR = "/home/ubuntu/zhongce/result/crop/0_resize/ori"
    AUG_TRAIN_DIR = "/home/ubuntu/zhongce/result/crop/0_resize/train/0.normal"
    AUG_TEST_DIR = "/home/ubuntu/zhongce/result/crop/0_resize/test/0.normal"
    AUG_VALID_DIR = "/home/ubuntu/zhongce/result/crop/0_resize/valid/0.normal"
    if not os.path.exists(AUG_TRAIN_DIR):
        os.makedirs(AUG_TRAIN_DIR)
    if not os.path.exists(AUG_TEST_DIR):
        os.makedirs(AUG_TEST_DIR)
    if not os.path.exists(AUG_VALID_DIR):
        os.makedirs(AUG_VALID_DIR)

    count_train = 500
    loop_train = 40-1
    count_test = 100
    loop_test = 35-1
    count_valid = 70
    loop_valid = 10-1
    count = 0

    train_num = 0
    test_num = 0
    valid_num = 0

    # 图像增强
    seq = iaa.Sequential([
        iaa.Flipud(0),  # 上下翻转
        iaa.Fliplr(0.5),  # 左右翻转
        iaa.Multiply((0.9, 1.1)),  # 亮度
        iaa.GaussianBlur(sigma=(0, 1.0)),  # 高斯噪声
        iaa.Affine(translate_px={"x": 0, "y": 0}, scale=(1, 1), rotate=(0, 0))  # 射影变换
    ])

    for root, sub_folders, files in os.walk(IMG_DIR):
        for name in files:
            if count < count_train:
                img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.png'))
                path = os.path.join(AUG_TRAIN_DIR, str(train_num).zfill(6) + '.png')
                img.save(path)
                train_num += 1
                count += 1
                for epoch in range(loop_train):
                    seq_det = seq.to_deterministic()  # 保持坐标和图像同步改变，而不是随机
                    # 读取图片
                    img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.png'))
                    img = np.asarray(img)
                    # 存储变化后的图片
                    image_aug = seq_det.augment_images([img])[0]
                    path = os.path.join(AUG_TRAIN_DIR, str(train_num).zfill(6) + '.png')
                    Image.fromarray(image_aug).save(path)
                    train_num += 1
            elif count < count_train + count_test:
                img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.png'))
                path = os.path.join(AUG_TEST_DIR, str(test_num).zfill(6) + '.png')
                img.save(path)
                test_num += 1
                count += 1
                for epoch in range(loop_test):
                    seq_det = seq.to_deterministic()  # 保持坐标和图像同步改变，而不是随机
                    # 读取图片
                    img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.png'))
                    img = np.asarray(img)
                    # 存储变化后的图片
                    image_aug = seq_det.augment_images([img])[0]
                    path = os.path.join(AUG_TEST_DIR, str(test_num).zfill(6) + '.png')
                    Image.fromarray(image_aug).save(path)
                    test_num += 1
            elif count < count_train + count_test + count_valid:
                img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.png'))
                path = os.path.join(AUG_VALID_DIR, str(valid_num).zfill(6) + '.png')
                img.save(path)
                valid_num += 1
                count += 1
                for epoch in range(loop_valid):
                    seq_det = seq.to_deterministic()  # 保持坐标和图像同步改变，而不是随机
                    # 读取图片
                    img = Image.open(os.path.join(IMG_DIR, name[:-4] + '.png'))
                    img = np.asarray(img)
                    # 存储变化后的图片
                    image_aug = seq_det.augment_images([img])[0]
                    path = os.path.join(AUG_VALID_DIR, str(valid_num).zfill(6) + '.png')
                    Image.fromarray(image_aug).save(path)
                    valid_num += 1
            else:
                break
