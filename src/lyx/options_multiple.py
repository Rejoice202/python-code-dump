import argparse
import os
import torch


class Options:
    """
    Options class
    Returns:
        [argparse]: argparse containing train and test options
    """

    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        """
        Base
        """
        # 数据集
        self.parser.add_argument('--dataset', default='***', help='cexia_0 | cexia_1 | ... ')
        # 网络模型
        self.parser.add_argument('--model', type=str, default='isgan', help='ganomaly | skipganomaly | isgan')
        # 训练/测试
        self.parser.add_argument('--stage', default='train', help='train | test ')
        # 是否调用检测算法
        self.parser.add_argument('--cv_test', action='store_true', default=False)
        # batchsize
        self.parser.add_argument('--batchsize', type=int, default=64, help='input batch size')
        # 图片分辨率
        self.parser.add_argument('--isize', type=int, default=64, help='input image size.')
        # 向量Z的维度
        self.parser.add_argument('--nz', type=int, default=100, help='size of the latent z vector')
        # 评估指标
        self.parser.add_argument('--metric', type=str, default='os', help='auc | con | os')

        self.parser.add_argument('--dataroot', default='', help='path to dataset')
        self.parser.add_argument('--path', default='', help='path to the folder or image to be predicted.')
        self.parser.add_argument('--workers', type=int, help='number of data loading workers', default=8)
        self.parser.add_argument('--droplast', action='store_true', default=True, help='Drop last batch size.')
        self.parser.add_argument('--nc', type=int, default=3, help='input image channels')
        self.parser.add_argument('--ngf', type=int, default=64)
        self.parser.add_argument('--ndf', type=int, default=64)
        self.parser.add_argument('--extralayers', type=int, default=0, help='Number of extra layers on gen and disc')
        self.parser.add_argument('--device', type=str, default='gpu', help='Device: gpu | cpu')
        self.parser.add_argument('--gpu_ids', type=str, default='0', help='gpu ids: e.g. 0  0,1,2, 0,2. use -1 for CPU')
        self.parser.add_argument('--ngpu', type=int, default=1, help='number of GPUs to use')
        self.parser.add_argument('--name', type=str, default='experiment_name', help='name of the experiment')
        self.parser.add_argument('--display_server', type=str, default="http://localhost",
                                 help='visdom server of the web display')
        self.parser.add_argument('--display_port', type=int, default=8097, help='visdom port of the web display')
        self.parser.add_argument('--display_id', type=int, default=0, help='window id of the web display')
        self.parser.add_argument('--display', action='store_true', default=False, help='Use visdom.')
        self.parser.add_argument('--verbose', action='store_true', default=False,
                                 help='Print the training and model details.')
        self.parser.add_argument('--outf', default='./output', help='folder to output images and model checkpoints')
        self.parser.add_argument('--manualseed', default=-1, type=int, help='manual seed')
        self.parser.add_argument('--abnormal_class', default='defect',
                                 help='Anomaly class idx for mnist and cifar datasets')

        """
        训练
        """
        # 训练轮数
        self.parser.add_argument('--niter', type=int, default=25, help='number of epochs to train for')
        # loss系数
        self.parser.add_argument('--w_adv', type=float, default=1, help='Weight for adversarial loss. default=1')
        self.parser.add_argument('--w_con', type=float, default=40, help='Weight for reconstruction loss. default=50')
        self.parser.add_argument('--w_lat', type=float, default=1, help='Weight for latent space loss. default=1')
        self.parser.add_argument('--w_psnr', type=float, default=0.01, help='Weight for psnr loss')
        self.parser.add_argument('--w_ssim', type=float, default=0.5, help='Weight for ssim loss')
        # 训练时保存验证结果
        self.parser.add_argument('--save_test_images', action='store_true', default=False,
                                 help='Save valid images for demo')

        self.parser.add_argument('--print_freq', type=int, default=100,
                                 help='frequency of showing training results on console')
        self.parser.add_argument('--save_image_freq', type=int, default=100,
                                 help='frequency of saving real and fake images')
        self.parser.add_argument('--load_weights', action='store_true', help='Load the pre-trained weights')
        self.parser.add_argument('--resume', default='', help="path to checkpoints (to continue training)")
        self.parser.add_argument('--phase', type=str, default='train', help='train, val, test, etc')
        self.parser.add_argument('--iter', type=int, default=0, help='Start from iteration i')
        self.parser.add_argument('--niter_decay', type=int, default=100,
                                 help='# of iter to linearly decay learning rate to zero')
        self.parser.add_argument('--beta1', type=float, default=0.5, help='momentum term of adam')
        self.parser.add_argument('--lr', type=float, default=0.0002, help='initial learning rate for adam')

        self.parser.add_argument('--lr_policy', type=str, default='lambda', help='lambda|step|plateau')
        self.parser.add_argument('--lr_decay_iters', type=int, default=50,
                                 help='multiply by a gamma every lr_decay_iters iterations')
        self.isTrain = True
        self.opt = None

        """
        测试
        """
        # 测试所用的模型路径
        self.parser.add_argument('--weight_path', type=str, default="./output/{}/{}/train/weights/netG_**.pth",
                                 help='the pre-trained weights you wanted to use in this test')
        # 缺陷指数的定义
        self.parser.add_argument('--Anomaly_score_type', type=str, default="PSNR", help='PSNR | SSIM')

        # 以batch为单位拼接保存本次测试中所有图片的原图及生成器生成的图片
        self.parser.add_argument('--save_batch_images', action='store_true', default=False,
                                 help='Save test images--Stitched by batch')
        # 保存本次测试中所有图片的原图、生成器生成的图片（以及差异图像）
        self.parser.add_argument('--save_single_images', action='store_true', default=False,
                                 help='Save test images--Single')
        # 是否将本次测试中所有图片的原图、生成器生成的图片以及差异图像保存到指定路径
        self.parser.add_argument('--save_single_images_cv', type=str, default="",
                                 help='"./cv_images/wheel_wp=0.01_ws=0.5/"  default=""')
        # 保存检测出的异常图片的原图、生成图片以及标记出检测框的差异图像
        self.parser.add_argument('--save_abnormal_images', action='store_true', default=True,
                                 help='Save abnormal images')
        # 保存检测出的标记有检测框的异常图片的原图
        self.parser.add_argument('--save_results', action='store_true', default=True,
                                 help='Save results')
        # 保存ROC曲线
        self.parser.add_argument('--save_ROC', action='store_true', default=True,
                                 help='Save ROC curve')
        # 保存原始异常得分的分布情况
        self.parser.add_argument('--save_ori_abnormal_score', action='store_true', default=False,
                                 help='Save the distribution of original abnormal scores')
        # 保存异常得分的分布情况
        self.parser.add_argument('--save_abnormal_score', action='store_true', default=True,
                                 help='Save the distribution of abnormal scores')

        # 64*64分辨率下HSV参数的上下限
        self.parser.add_argument('--HSV_64', nargs=6, type=int, default=[95, 43, 46, 124, 255, 255],
                                 help='Upper and lower limits of HSV parameters(64*64)')
        # 初次筛选时HSV参数的上下限,依次为HSV值的下限、HSV值的上限
        self.parser.add_argument('--HSV_first', nargs=6, type=int, default=[110, 230, 90, 125, 255, 200],
                                 help='Upper and lower limits of HSV parameters during the first screening')
        # 二次筛选时HSV参数的上下限（比首次筛选时的范围要大一些，这里采用的是蓝色的HSV值范围）
        self.parser.add_argument('--HSV_second', nargs=6, type=int, default=[100, 43, 46, 124, 255, 255],
                                 help='Upper and lower limits of HSV parameters during the second screening')
        # 初次筛选时其它参数的设定，依次为 ①可疑区域轮廓的宽高比 ②真正的异常像素点占比 ③真正的异常像素点个数
        self.parser.add_argument('--Parameter_first', nargs=3, type=float, default=[0.3, 0.5, 2],
                                 help='Setting of other parameters during the first screening')
        # 二次筛选时其它参数的设定，依次为 ①可疑子区域轮廓的宽高比 ②子区域上真正的异常像素点占比 ③子区域上真正的异常像素点个数
        self.parser.add_argument('--Parameter_second', nargs=3, type=float, default=[0.55, 0.5, 4],
                                 help='Setting of other parameters during the second screening')

    def parse(self, data_name, weight_number="last"):
        """
        Parse Arguments.
        """

        self.opt = self.parser.parse_args()
        self.opt.isTrain = self.isTrain   # 训练/测试
        self.opt.dataset = data_name
        self.opt.weight_path = "./output/{}/{}/train/weights/netG_" + weight_number + ".pth"

        str_ids = self.opt.gpu_ids.split(',')
        self.opt.gpu_ids = []
        for str_id in str_ids:
            id = int(str_id)
            if id >= 0:
                self.opt.gpu_ids.append(id)

        # set gpu ids
        if len(self.opt.gpu_ids) > 0:
            torch.cuda.set_device(self.opt.gpu_ids[0])

        args = vars(self.opt)

        if self.opt.verbose:
            print('------------ Options -------------')
            for k, v in sorted(args.items()):
                print('%s: %s' % (str(k), str(v)))
            print('-------------- End ----------------')

        # save to the disk
        if self.opt.name == 'experiment_name':
            self.opt.name = "%s/%s" % (self.opt.model, self.opt.dataset)
        expr_dir = os.path.join(self.opt.outf, self.opt.name, 'train')
        test_dir = os.path.join(self.opt.outf, self.opt.name, 'test')

        if not os.path.isdir(expr_dir):
            os.makedirs(expr_dir)
        if not os.path.isdir(test_dir):
            os.makedirs(test_dir)

        file_name = os.path.join(expr_dir, 'opt.txt')
        with open(file_name, 'wt') as opt_file:
            opt_file.write('------------ Options -------------\n')
            for k, v in sorted(args.items()):
                opt_file.write('%s: %s\n' % (str(k), str(v)))
            opt_file.write('-------------- End ----------------\n')
        return self.opt
