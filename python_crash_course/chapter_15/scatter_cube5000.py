#数字的立方 5000个数据

import matplotlib.pyplot as plt

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=40)

#设置图表标题并加上标签
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

#设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()

#保存图片
plt.savefig("cube_5000.png", bbox_inches='tight')
