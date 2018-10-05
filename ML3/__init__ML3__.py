from ML3.trees import *
from ML3.treePoltter import *

# myDat, labels = createDataSet()
# print(createTree(myDat,labels))
# '''
# 结果集：
# {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
# '''

myTree = retrieveTree(0)
print(myTree)
print("getNumLeafs==", getNumLeafs(myTree))
print("getTreeDepth==", getTreeDepth(myTree))
'''
结果集：
{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
getNumLeafs== 3
getTreeDepth== 2
'''

myTree['no surfacing'][3] = 'maybe'
createPlot(myTree)
