from ML3.trees import *

myDat, labels = createDataSet()
print(createTree(myDat,labels))
'''
结果集：
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
'''