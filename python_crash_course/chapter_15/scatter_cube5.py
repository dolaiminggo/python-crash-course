#15.2.9 数字的立方图5个数据

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]
plt.scatter(input_values, cubes, s=100)

"""设置图标标题并给坐标轴加上标签"""
plt.title("Cube Numbers", fontsize= 24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cube of value', fontsize=14)

""""设置刻度标记的大小"""
plt.tick_params(axis='both', labelsize=14)

plt.show()
plt.savefig('cube_plot.png', bbox_inches="tight")

