from PyQt5.Qt import *
from PyQt5.QtCore import*
from PyQt5.QtWidgets import QWidget, QApplication, QGroupBox, QPushButton, QLabel, QHBoxLayout,  QVBoxLayout, QGridLayout, QFormLayout, QLineEdit, QTextEdit
import sys

class login(QWidget):
    def __init__(self):
        super(login,self).__init__()
        self.initUi()

    def initUi(self):
        self.setWindowTitle("classify_augument")
        layout = QGridLayout()
        self.setGeometry(600, 600, 400, 400)


        dataLabel = QLabel("data_path")
        self.dataLineEdit = QLineEdit(" ")
        trainLabel = QLabel("train_path")
        self.trainLineEdit = QLineEdit(" ")
        testLabel = QLabel("test_path")
        self.testLineEdit = QLineEdit(" ")
        layout.addWidget(dataLabel,1,0)
        layout.addWidget(self.dataLineEdit,1,1)
        layout.addWidget(trainLabel, 2, 0)
        layout.addWidget(self.trainLineEdit, 2, 1)
        layout.addWidget(testLabel, 3, 0)
        layout.addWidget(self.testLineEdit, 3, 1)
        layout.setColumnStretch(1, 5)
        save_Btn = QPushButton('执行')
        cancle_Btn = QPushButton('取消')
        cancle_Btn.clicked.connect(QCoreApplication.quit)
        save_Btn.clicked.connect(self.addNum)
        layout.addWidget(save_Btn,10,1)
        layout.addWidget(cancle_Btn,10,5)
        self.setLayout(layout)

    def addNum(self):
        data = self.dataLineEdit.text()  # 获取文本框内容
        train = self.trainLineEdit.text()  # 获取文本框内容
        test = self.testLineEdit.text()  # 获取文本框内容
        print(data)
        print(train)
        print(test)
        f_generate(data[1:-1],train[1:-1],test[1:-1])


def f_generate(img_path,train_path,test_path):
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


    #img_path ='/home/ubuntu/zhongce/augment/img/'
    #img_path ='/home/ubuntu/FlaskTEDS/TEDS_Data/guiwai/img/'
    data_list = []
    print(len(os.listdir(img_path)))
    for item in os.listdir(img_path):
        if item.endswith('.jpg'):
            data_list.append(item)
    train_list, test_list = random_sample(data_list, 10)  # 设定测试集中图片的数量
    random.shuffle(train_list)
    random.shuffle(test_list)
    with open(train_path, 'w+') as f1:#D:/Abnormal_Detection/Yolo_data/cexia/config_file//cexia_train.txt
    #with open('/home/ubuntu/FlaskTEDS/TEDS_Data/guiwai/guiwai_train.txt', 'w+') as f1:#D:/Abnormal_Detection/Yolo_data/cexia/config_file//cexia_train.txt
        for train_name in train_list:
            f1.write(img_path + train_name)
            f1.write('\n')
        print('f1 success')
    #with open('/home/ubuntu/FlaskTEDS/TEDS_Data/guiwai/guiwai_test.txt', 'w+') as f2:#'D:/Abnormal_Detection/Yolo_data/cexia/config_file/cexia_test.txt'
    with open(test_path, 'w+') as f2:#'D:/Abnormal_Detection/Yolo_data/cexia/config_file/cexia_test.txt'
        for test_name in test_list:
            f2.write(img_path + test_name)
            f2.write('\n')
        print('f2 success')


if __name__=="__main__":

    app = QApplication(sys.argv)
    w = login()
    w.show()
    sys.exit(app.exec_())
