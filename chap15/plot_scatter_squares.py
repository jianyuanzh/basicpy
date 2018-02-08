import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# 使用edgecolor='none'删除数据点的轮廓
# 使用c='red'设置数据点的颜色， c=(0,0,0.4)
# 还可以使用颜色银蛇
# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=5)
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors='none', s=10)
plt.title('Square numbers', fontSize=10)
plt.xlabel('Value', fontSize=10)
plt.ylabel('Square Value', fontSize=10)
plt.tick_params(axis='both', which='major', labelsize=8)

plt.axis([1, 1100, 0, 1100000])

# 保存文件
plt.savefig('squres_plot.png', bbox_inches='tight')


plt.show()
