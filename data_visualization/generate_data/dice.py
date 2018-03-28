""" 模拟两个骰子 """
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

die_1 = Die()
die_2 = Die()
# 掷100次骰子
results = []

for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果经行可视化
hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')