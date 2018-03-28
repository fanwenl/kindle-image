""" 天气数据可视化 """
import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = '.\\downloads_data\\death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            # 读取时间，进行转化
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            # 读取数据，除了标题，转换为整数
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            highs.append(high)
            lows.append(low)
            dates.append(current_date)

# 根据数据绘制图形
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperture(F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
