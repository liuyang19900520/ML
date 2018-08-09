import operator

from ML2.kNN2 import *
from ML2.kNN import *
import numpy as np

returnMat = zeros((10, 3))
print("returnMat")
print(returnMat)
print("====================================")

a = np.random.randint(0, 10, size=[10, 3])
print(a)
print("====================================")

index = 0
firstLine = a[0]
print("firstLine")
print(firstLine)

returnMat[index, :] = firstLine[0:3]
print(firstLine[-1])
print(returnMat)
print("====================================")

datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
print(datingDataMat)
print(datingLabels)
print(15.0 * array(datingLabels))
print(array(datingLabels))
print("====================================")

group, labels = createDataSet()
print(group)
print(shape(group))
print(group.min(0))
print("====================================")

normMat, ranges, minVals = autoNorm(datingDataMat)
print(normMat)
print("====================================")
m = normMat.shape[0]
print(normMat[0, :])
print("====================================")
