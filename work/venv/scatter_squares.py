import matplotlib.pyplot as plt

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,
            edgecolor='none',s=40)

#标题以及坐标轴标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

#坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.savefig('squares_plot.png',bbox_inches='tight')