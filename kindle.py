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
        # 将name和属性添加到list
        arr_fname.append(fname)
        arr_fobj.append(fobj)
    for i in arr_fname:
        # 文件名到第截多长（根据最短的name计算）
        arr_newfname.append(i[0:20])
    for j in arr_newfname:
        # 查找名字相同的图片进行拼接
        num = arr_newfname.index(j)
        if num < (len(arr_newfname) - 1):
            if j is arr_newfname[num+1]:
                # 打开name相同的图片，将小的图片拼接到大的图片的下面
                img1 = Image.open("".join(rt) + "".join(dirs) + arr_fname[num]+arr_fobj[num])
                img2 = Image.open("".join(rt) + "".join(dirs) + arr_fname[num+1]+arr_fobj[num + 1])
                x1, y1 = img1.size
                x2, y2 = img2.size
                newimage = Image.new('RGBA', (x1, (y1 + y2))) # 新建拼接的图片
                if y1 < y2:
                    # 图片拼接并保存
                    newimage.paste(img2, (0, 0))
                    newimage.paste(img1, (0, y2))
                    newimage.save("".join(rt) + "".join(dirs) + arr_fname[num] + arr_fobj[num])
                else:
                    newimage.paste(img1, (0, 0))
                    newimage.paste(img2, (0, y1))
                    newimage.save("".join(rt) + "".join(dirs) + arr_fname[num] + arr_fobj[num])






        # 不需要图片转换
        # outfile = fname + ".jpg"
        # if f != outfile:
        #     try:
        #         Image.open("".join(rt)+"".join(dirs)+f).save("".join(rt)+"".join(dirs)+outfile)
        #
        #     except IOError:
        #         print("cannot convert",f)
        # img = Image.open("".join(rt) + "".join(dirs) + f)
        # #直接转换之后图片像素变低
        # img = img.convert('L')
        # img = np.array(img)
        # rows, cols = img.shape
        # for x in range(rows):
        #     for y in range(cols):
        #         if img[x, y] <= 128:
        #             img[x, y] = 0
        #         else:
        #             img[x, y] = 1
        # img.save("".join(rt) + "".join(dirs) + f)


#        new = fname[0] + 'b' + fname[1]
#        os.rename(os.path.join(rt,f),os.path.join(rt,new))