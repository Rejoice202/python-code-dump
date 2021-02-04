"""
从所有的图片(及label)中选取一定数量的作为测试集,其余的作为训练集
并导出其路径,保存在txt中
"""
import os

# file = open('/home/yuanxue/deeplearning/kuang_code/datasets/test.txt', 'w')
# img_path = '/home/yuanxue/deeplearning/kuang_code/datasets/test'
#
# for item in os.listdir(img_path):
#     if item.endswith('.jpg'):
#         filename = os.path.splitext(item)[0]
#         file.write('data/maogan_test/' + filename + '.jpg' + '\n')
# file.close()


import random


# 从列表中随机选取一定数目的元素
def random_sample(dataList, num1):
    Test_List = []  # 初始化存储随机产生的索引的列表
    for i in range(num1):  # 随机产生索引的数量
        randIndex = int(random.uniform(0, len(dataList)))  # 在指定的范围内产生随机数位置索引
        Test_List.append(dataList[randIndex])  # 进行存储
        del (dataList[randIndex])  # 对已选中的元素进行删除，以便于下一次随机选取
    Train_List = dataList  # 随机选取过后剩下的元素
    return Train_List, Test_List  # 返回随机选取的一定数目的元素，和剩下的元素


img_path ='/home/ubuntu/zhongce/augment/img/'
#img_path ='/home/ubuntu/FlaskTEDS/TEDS_Data/guiwai/img/'
data_list = []
print(len(os.listdir(img_path)))
for item in os.listdir(img_path):
    if item.endswith('.jpg'):
        data_list.append(item)
train_list, test_list = random_sample(data_list, 1000)  # 设定测试集中图片的数量
random.shuffle(train_list)
random.shuffle(test_list)
with open('/home/ubuntu/zhongce/augment/cexia_train.txt', 'w+') as f1:#D:/Abnormal_Detection/Yolo_data/cexia/config_file//cexia_train.txt
#with open('/home/ubuntu/FlaskTEDS/TEDS_Data/guiwai/guiwai_train.txt', 'w+') as f1:#D:/Abnormal_Detection/Yolo_data/cexia/config_file//cexia_train.txt
    for train_name in train_list:
        f1.write(img_path + train_name)
        f1.write('\n')
    print('f1 success')
#with open('/home/ubuntu/FlaskTEDS/TEDS_Data/guiwai/guiwai_test.txt', 'w+') as f2:#'D:/Abnormal_Detection/Yolo_data/cexia/config_file/cexia_test.txt'
with open('/home/ubuntu/zhongce/augment/cexiatest.txt', 'w+') as f2:#'D:/Abnormal_Detection/Yolo_data/cexia/config_file/cexia_test.txt'
    for test_name in test_list:
        f2.write(img_path + test_name)
        f2.write('\n')
    print('f2 success')
