import matplotlib.pyplot as plt

from ML2.kNN import *
from ML2.kNN2 import *
from ML2.kNN3 import *

group, labels = createDataSet()
print(group)
print(labels)

result = classify0([0, 0], group, labels, 3)
print(result)

datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
print(datingDataMat)
print(datingLabels)

fig = plt.figure()
# 表示表格视图仅一个，可理解独立显示
ax = fig.add_subplot(111)
# scatter是做散点图的函数，数据分别是矩阵第一列和第二列，分别对应的结果集合
ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15.0 * array(datingLabels), 15.0 * array(datingLabels))
plt.xlabel('Percentage of Time Spent Playing Video Games')
plt.ylabel('Liters of Ice Cream Consumed Per Week')
# 显示图像
plt.show()

normMat, ranges, minVals = autoNorm(datingDataMat)
print(ranges)
print(minVals)
print(normMat)

datingClassTest()
classifyPerson()

handwritingClassTest()


