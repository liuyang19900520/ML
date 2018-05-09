import kNN
import matplotlib
import matplotlib.pyplot as plt
from numpy.ma import array

print("1111111111111111111111111111111111111111111111111111")
group, labels = kNN.createDataSet()
print(group)
print(labels)
print("1111111111111111111111111111111111111111111111111111")

r = kNN.classify0([0, 0], group, labels, 3)
print(r)
print(kNN.file2matrix("datingTestSet.txt"))
fig = plt.figure()  # 创建plot的图像展示
ax = fig.add_subplot(111)  # z整体展示
datingDataMat, datingLabels = kNN.file2matrix('datingTestSet.txt')  # 读文件，得到3项数据的矩阵，和好感度的数组

normMat, ranges, minVals = kNN.autoNorm(datingDataMat)
print("2222222222222222222222222222222222222222222222222222")

print(datingDataMat)
print("2222222222222222222222222222222222222222222222222222")
print(normMat)
# ax.scatter(datingDataMat[:,1], datingDataMat[:,2])
#scatter是做散点图的函数，分别是
print("2222222222222222222222222222222222222222222222222222")
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
#ax.axis([-2, 25, -0.2, 2.0])#指定图像范围
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
plt.show()  # 显示图像
print("33333333333333333333333333333333333333333333333333333")
kNN.datingClassTest()
print("33333333333333333333333333333333333333333333333333333")
print("44444444444444444444444444444444444444444444444444444")
kNN.classifyPerson()


print("44444444444444444444444444444444444444444444444444444")
print("555555555555555555555555555555555555555555555555555555")

kNN.handwritingClassTest()