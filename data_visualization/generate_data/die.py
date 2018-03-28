""" 模拟骰子 """
from random import randint
import pygal

class Die():
    """ 骰子的类 """
    def __init__(self, num_sides=6):
        """ 骰子的六个面 """
        self.num_sides = num_sides
    
    def roll(self):
        """ 返回一个骰子的一个面 """
        return randint(1, self.num_sides)

die = Die()
# 掷100次骰子
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果经行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')