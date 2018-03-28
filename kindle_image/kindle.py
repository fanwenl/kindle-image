import os

from PIL import Image

arr_fname = []
arr_fobj =[]

root = "C:\\Users\\fanwe\\Desktop\\images\\"
for rt, dirs, files in os.walk(root):
    for dir in  dirs:   # 获取目录下的字目录
        # 获取字目录中的文件file[2]是文件名。file[1]是二级目录，file[0]是一级目录
        # for file in os.walk(os.path.join(root, dir)):
        childdir = "".join(rt) + "".join(dir)
        for file in os.listdir(childdir):
            # print("".join(file[2]))
            # 获取目录中文件的name和格式
            fname, fobj = os.path.splitext(file)
            # 如果是图片格式记录文件名和属性
            if fobj in ['.jpg', '.png']:
                arr_fname.append(fname)
                # 如果文件名是'.png'另存为'.jpg'
                if fobj in ['.jpg']:
                    img = Image.open("".join(rt) + "".join(dir) + "\\" + file)
                    img.save("".join(rt) + "".join(dir) + "\\" + fname + "".join('.png'))
        # 判断文件拼接的顺序(依据文件名的长度)
        arr_fname.sort()
        # 获取列表的长度
        num = len(arr_fname)
        if num == 1:
            img = Image.open("".join(rt) + "".join(dir) + "\\" + arr_fname[0] + '.png')
            x1, y1 = img.size
            box = (0, 210, x1, (y1 - 150))
            newimage = img.crop(box)
            newimage = newimage.convert('L')
            x, y = newimage.size  # 获取图片的尺寸
            for i in range(0, int(y / (4 * x / 3))):  # 求图片的整数倍
                box = (0, i * (4 * x / 3), x, (i + 1) * (4 * x / 3))  # 计算截图的大小
                new = newimage.crop(box).resize((758, 1024), Image.ANTIALIAS)  # 截图并且转换为制定的分辨率
                new.save("".join(rt) + "".join('image') + "\\" + arr_fname[0] + str(i) + '.png')
        elif num == 2:
            img1 = Image.open("".join(rt) + "".join(dir) + "\\" + arr_fname[0] + '.png')
            img2 = Image.open("".join(rt) + "".join(dir) + "\\" + arr_fname[1] + '.png')
            x1, y1 = img1.size
            x2, y2 = img2.size
            box1 = (0, 210, x1, (y1 - 150))
            box2 = (0, 210, x2, (y2 - 150))
            newimage1 = img1.crop(box1)
            newimage2 = img2.crop(box2)
            newimage = Image.new('RGBA', (x1, (y1 + y2 - 720))) # 新建拼接的图片
            newimage.paste(newimage1, (0, 0))
            newimage.paste(newimage2, (0, y1 - 360))
            newimage = newimage.convert('L')
            x, y = newimage.size  # 获取图片的尺寸
            for i in range(0, int(y / (4 * x / 3))):  # 求图片的整数倍
                box = (0, i * (4 * x / 3), x, (i + 1) * (4 * x / 3))  # 计算截图的大小
                new = newimage.crop(box).resize((758, 1024), Image.ANTIALIAS)  # 截图并且转换为制定的分辨率
                new.save("".join(rt) + "".join('image') + "\\" + arr_fname[0] + str(i) + '.png')
        elif num == 3:
            img1 = Image.open("".join(rt) + "".join(dir) + "\\" + arr_fname[0] + '.png')
            img2 = Image.open("".join(rt) + "".join(dir) + "\\" + arr_fname[1] + '.png')
            img3 = Image.open("".join(rt) + "".join(dir) + "\\" + arr_fname[2] + '.png')
            x1, y1 = img1.size
            x2, y2 = img2.size
            x3, y3 = img3.size
            box1 = (0, 210, x1, (y1 - 150))
            box2 = (0, 210, x2, (y2 - 150))
            box3 = (0, 210, x3, (y3 - 150))
            newimage1 = img1.crop(box1)
            newimage2 = img2.crop(box2)
            newimage3 = img3.crop(box3)
            newimage = Image.new('RGBA', (x1, (y1 + y2 + y3 - 1080)))  # 新建拼接的图片
            newimage.paste(newimage1, (0, 0))
            newimage.paste(newimage2, (0, y1 - 360))
            newimage.paste(newimage3, (0, y2 - 720))
            newimage = newimage.convert('L')
            newimage.save("".join(rt) + "".join('image') + "\\" + arr_fname[0] + '.png')
        else:
            print("error")
        arr_fname = []