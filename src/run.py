from darknet import *
import numpy as np
import cv2
import Config


class Network:
    def __init__(self):
        # 网络模型初始化
        self.init_netMain, self.init_metaMain, self.init_altNames = performDetect(
            configPath=Config.Darknet['configPath'], weightPath=Config.Darknet['weightPath'],
            metaPath=Config.Darknet['metaPath'], initOnly=True)
        if self.init_netMain is None or self.init_metaMain is None or self.init_altNames is None:
            print('Model initialization failed')

    def detection(self, image):
        results = detect(self.init_netMain, self.init_metaMain, self.init_altNames,
                         image, thresh=0.1)
        return results


def save_result(image, results, save_crop=""):
    image_bgr = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    # 检测框内图片的保存路径
    if save_crop != "":
        if not os.path.exists(save_crop):
            os.makedirs(save_crop)

    if results:
        for detection in results:
            # 当前检测框的标签和置信度
            label = detection[0]
            confidence = detection[1]
            confidence = str(np.rint(100 * confidence)) + "%"

            # bbox信息
            bounds = detection[2]
            y_extent = int(bounds[3])
            x_entent = int(bounds[2])
            # 左上角的坐标
            x_coord = int(bounds[0] - bounds[2] / 2)
            y_coord = int(bounds[1] - bounds[3] / 2)
            bbox = [[x_coord, y_coord], [x_coord, y_coord + y_extent],
                    [x_coord + x_entent, y_coord + y_extent], [x_coord + x_entent, y_coord]]

            # 矫正bbox
            if bbox[0][0] < 0:
                bbox[0][0] = 0
            if bbox[0][1] < 0:
                bbox[0][1] = 0
            if bbox[1][0] < 0:
                bbox[1][0] = 0
            if bbox[1][1] > image.shape[0]:
                bbox[1][1] = image.shape[0]
            if bbox[2][0] > image.shape[1]:
                bbox[2][0] = image.shape[1]
            if bbox[2][1] > image.shape[0]:
                bbox[2][1] = image.shape[0]
            if bbox[3][0] > image.shape[1]:
                bbox[3][0] = image.shape[1]
            if bbox[3][1] < 0:
                bbox[3][1] = 0

            # 按类别保存检测框内的图片
            if save_crop != "":
                # if label == "1":
                if True:
                    save_dir_crop_now = save_crop + "/" + label
                    if not os.path.exists(save_dir_crop_now):
                        os.makedirs(save_dir_crop_now)
                    global count
                    # cv2.imwrite(save_dir_crop_now + "/" + str(count).zfill(5) + ".png",
                    #             cv2.resize(image[bbox[0][1]:bbox[2][1], bbox[0][0]:bbox[2][0]], (64, 64)))
                    cv2.imwrite(save_dir_crop_now + "/" + str(count).zfill(5) + ".png",
                                image[bbox[0][1]:bbox[2][1], bbox[0][0]:bbox[2][0]])
                    count += 1

            # 绘制检测框
            cv2.rectangle(image_bgr, tuple(bbox[0]), tuple(bbox[2]), (0, 255, 0), 5)
            # 在检测框右下角显示类别和置信度信息：
            text = str(label) + ":" + confidence
            cv2.putText(image_bgr, text, tuple(bbox[1]), cv2.FONT_HERSHEY_COMPLEX, 1.0, (100, 200, 200), 5)
    return image_bgr


count = 0


if __name__ == '__main__':
    img_type = Config.img_type

    # 检测结果保存路径
    save_path_crop = "../" + img_type + "/result/crop"
    if not os.path.exists(save_path_crop):
        os.makedirs(save_path_crop)
    # save_path_whole = "../" + img_type + "/result/whole"
    # if not os.path.exists(save_path_whole):
    #     os.makedirs(save_path_whole)

    # 网络模型初始化
    network = Network()

    path = "../" + img_type + "/data/ori/" + img_type + "/img/"  # 数据存放位置
    filelist = os.listdir(path)

    for name in filelist:
        filename = path + name
        img = cv2.imread(filename, 0)

        print("正在检测：" + name)
        detect_results = network.detection(img)
        result_img = save_result(img, detect_results, save_path_crop)
        # cv2.imwrite(save_path_whole + "/" + name, result_img)
