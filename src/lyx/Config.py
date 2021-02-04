# txt_path = "../cexia/config_file/cexia_test.txt"
# save_path = "../cexia/result"
# folder_name = "cexia"
# classes = 5

# txt_path ="/home/ubuntu/cexia/cexia_test.txt" #"../guinei/config_file/guinei_test.txt"
img_path = '/home/ubuntu/zhongce/augment/img/'  # tupianlujing
save_path ="/home/ubuntu/zhongce/result"  #"../guinei/result"
folder_name = "cexia" #"guinei"
classes = 5

Darknet = {"configPath": "../" + folder_name + "/config_file/" + folder_name + ".cfg",
           'weightPath': "../" + folder_name + "/config_file/" + folder_name + "_last.weights",
           'metaPath': "../" + folder_name + "/config_file/" + folder_name + ".data",
           'classes': classes,
           'class_name': "../" + folder_name + "/config_file/" + folder_name + ".names"}
