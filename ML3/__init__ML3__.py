from ML3.trees import *

myDat, labels = createDataSet()
print(myDat)
print(calcShannonEnt(myDat))

print(splitDataSet(myDat,0,0))
print(splitDataSet(myDat,0,1))