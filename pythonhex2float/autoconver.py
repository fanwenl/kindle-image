''' 本文件实现double类型浮点数的自动转化，主要用于电子围栏问题的分析和查找
    需要转化的数据放在conver.txt中
'''
import struct

filename = 'conver.txt'
with open(filename, 'r') as f:
    while True:
        str = f.read(32)
        # 判断是否到了文件的末尾,read()函数返回空字符。''表示空字符
        if str is not '':
            lat = str[:16]
            lon = str[16:]
            latnew = struct.unpack('<d',bytes.fromhex(lat))[0]
            lonnew = struct.unpack('<d',bytes.fromhex(lon))[0]
            print('[lat:{},lon:{}]'.format(latnew, lonnew))
        else:
            print('end of file')
            break;


