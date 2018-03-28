""" 绘制折线图 """
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 设置线宽,显示图像
plt.plot(input_values, squares, linewidth=5)

# 设置图标的标题，并添加标签
plt.title("Squares Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)
plt.show()



