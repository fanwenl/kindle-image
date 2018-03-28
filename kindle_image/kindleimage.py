import os

from PIL import Image

arr_fname = []
arr_fobj =[]
arr_newfname = []

root = "C:\\Users\\fanwe\\Desktop\\images\\"
for rt, dirs, files in os.walk(root):
    for f in files:
        # 获取图片的name和格式
        fname, fobj = os.path.splitext(f)
        outfile = fname + ".jpg"
        if f != outfile:
            try:
                Image.open("".join(rt)+"".join(dirs)+f).save("".join(rt)+"".join(dirs)+outfile)

            except IOError:
                print("cannot convert", f)
        img = Image.open("".join(rt) + "".join(dirs) + f)
        # 直接转换之后图片像素变低
        img = img.convert('L')
        # img = np.array(img)
        # rows, cols = img.shape
        # for x in range(rows):
        #     for y in range(cols):
        #         if img[x, y] <= 128:
        #             img[x, y] = 0
        #         else:
        #             img[x, y] = 1
        # img.save("".join(rt) + "".join(dirs) + f)
        x, y = img.size

        for i in range(0, int(y / (4 * x / 3))):
            box = (0, i * y, x, 0)
#            newimage = Image.new('RGBA', (x, 4 * x / 3))
            img.crop(box)
#            newimage.paste(img1, (0, y2))
            img.save("".join(rt) + "".join(dirs) + "111.jpg")



#        new = fname[0] + 'b' + fname[1]
#        os.rename(os.path.join(rt,f),os.path.join(rt,new))