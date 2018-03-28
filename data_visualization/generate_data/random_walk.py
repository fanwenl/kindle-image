""" 绘制随机漫步图 """
from random import choice
import matplotlib.pyplot as plt


class RandomWalk():
    """ 初始化随机漫步数据的类 """
    def __init__(self, num_points=5000):
        """ 初始化随机漫步的属性 """
        self.num_points = num_points

        # 所有随机漫步开始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ 计算随机漫步包含的所有的点 """
        # 不断漫步，直到达到列表指定的距离
        while len(self.x_values) < self.num_points:
            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # 除去原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            # 计算下一个点的x值和y值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

while True:
    # 创建实例，并绘制 当为5000000绘制比较缓慢。
    rw = RandomWalk(50000) 
    rw.fill_walk()

    # 设置窗口的尺寸
    plt.figure(dpi=128, figsize=(10, 6))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    
    # 突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 影藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # keep_runing = input("Make another walk?(y/n):")
    # if keep_runing == 'n':
    break