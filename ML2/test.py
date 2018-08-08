import operator

from ML2.kNN import *

group, labels = createDataSet()
print("data_set:")
print(group)
print("====================================")

dataSetSize = group.shape[0]
print("dataSetSize")
print(dataSetSize)
print("====================================")

inX = array([0, 0])
diffMat = tile(inX, (dataSetSize, 1)) - group
print("diffMat")
print(diffMat)
print("====================================")

sqDiffMat = diffMat ** 2
print("sqDiffMat")
print(sqDiffMat)
print("====================================")

sqDistances = sqDiffMat.sum(axis=1)
print("sqDistances")
print(sqDistances)
print("====================================")

distances = sqDistances ** 0.5
print("distances")
print(distances)
print("====================================")

sortedDistIndicies = distances.argsort()  # argsort把想向量中的每个元素进行排序  [2 3 1 0]
print("sortedDistIndicies")
print(sortedDistIndicies)
print("====================================")

classCount = {}
for i in range(3):
    # sortedDistIndicies=[2 3 1 0]（索引值）
    # sortedDistIndicies[i]取出的是第几索引值，labels[索引]得到的是显示的结果标签，及A或B
    # voteIlabel是最后显示的结果
    voteIlabel = labels[sortedDistIndicies[i]]
    print(voteIlabel)
    # classCount.get可以理解赋值默认值0，然后得到一个就加一，累加
    # 循环3次的结果是
    # 第一次：{'B': 1}
    # 第二次：{'B': 2}
    # 第三次：{'B': 2, 'A': 1}
    classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    print(classCount)
print("====================================")

print("classCount.items()")
print(classCount.items())
sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
print("sortedClassCount")
print(sortedClassCount)
print("====================================")
