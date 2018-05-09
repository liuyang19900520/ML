import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50) #范围是(-3,3);个数是50
y1 = 2*x + 1 # 仿真一维数据组(x ,y1)表示曲线1
y2 = x**2 #仿真一维数据组(x ,y2)表示曲线2，（平方）

fig=plt.figure(num=3, figsize=(4, 3)).add_subplot(111)#编号3，大小是800*500（代表的是这个图形的模型的大小）
list1=[1,1,1,1,1,2,2,2,2,2]
list2=[1,2,3,4,5,6,7,8,9,10]
list3=[1,2,3,1,2,3,1,2,3,1]
fig.scatter(list1,list2,list3,list3)
plt.show()#展示函数