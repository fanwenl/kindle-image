import os

from PIL import Image

arr_fname = []
arr_fobj =[]
arr_newfname = []

root = "C:\\Users\\fanwe\\Desktop\\images\\"
for rt, dirs, files in os.walk(root):
    for f in files:
        # 打开图片
        img = Image.open("".join(rt) + "".join(dirs) + f)
        x, y = img.size # 获取图片的尺寸
        for i in range(0, int(y / (4 * x / 3))): # 求图片的整数倍
            box = (0, i * (4 * x / 3), x, (i + 1) * (4 * x / 3)) # 计算截图的大小
#              newimage = Image.new('RGBA', (x, 4 * x / 3))
            newimage = img.crop(box).resize((758, 1024), Image.ANTIALIAS) # 截图并且转换为制定的分辨率
            # newimage.resize((758, 1024), Image.ANTIALIAS)
#            newimage.paste(img1, (0, y2))
            newimage.save("".join(rt) + "".join(dirs) + f + str(i) + ".jpg")


