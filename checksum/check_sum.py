""" 计算文件每一行字符的和校验 """

filename = "data.txt"

def caculate_sum(str):
    """ 计算输入数据的和 """
    # str为参与校验的字符串  
    # 检验和的概念一般体现在8bit长度的字符数组  
    # 下面使用的字符串全为ASCII码，在计算GPS坐标的时候去除'$'和'*'字符

    # 和校验是异或运算，需要先强制把字符转换成整形数据
    x = ord(str[1])
    for char in str[2:-2]:
        if char != '\n':
    #        print(char)
            y = ord(char)
            x = x^y

    # x即为校验和
    return x


def main():
    print("start caculate file!")

    # 读取文件，按行开始计算
    with open(filename,"r+") as f:
        while True:
            line = f.readline()
#            print(line)
            if not line:
                break
            sumx = caculate_sum(line)
            # 十六进制大写方式打印和校验
            print('{:X}'.format(sumx))
            
    print("caculate end!")


if __name__ == '__main__':
    main()
