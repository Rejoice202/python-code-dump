"""
resize并将jpg文件转为png
"""
from PIL import Image
import os.path
import glob  # 该方法返回所有匹配的文件路径列表（list）

Datadir = "/home/ubuntu/zhongce/result/crop/4/*.jpg"
savedir = "/home/ubuntu/zhongce/result/crop/4_resize"
#Datadir = "/home/ubuntu/roolar_augu/guiwai/0/*.png"
#savedir = "/home/ubuntu/roolar_augu/guiwai/0_resize"
if not os.path.exists(savedir):
    os.makedirs(savedir)


def convertjpg(jpgfile, outdir, width=64, height=64):
    img = Image.open(jpgfile)
    new_img = img.resize((width, height), Image.BILINEAR)
    new_img.save(os.path.join(outdir, os.path.basename(jpgfile).split(".")[0] + ".png"))


for jpgfile in glob.glob(Datadir):

    convertjpg(jpgfile, savedir)
