from ML3.trees import *
from ML3.treePoltter import *

# myDat, labels = createDataSet()
# print(createTree(myDat,labels))
# '''
# 结果集：
# {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
# '''

# myTree = retrieveTree(0)
# print(myTree)
# print("getNumLeafs==", getNumLeafs(myTree))
# print("getTreeDepth==", getTreeDepth(myTree))
# '''
# 结果集：
# {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
# getNumLeafs== 3
# getTreeDepth== 2
# '''
#
# myTree['no surfacing'][3] = 'maybe'
# createPlot(myTree)


#打开文件
fr=open('lenses.txt')
#获得lenses的矩阵，即之前使用的myDat
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
print(lenses)
#获得lenses的矩阵，即之前使用的labels
lensesLabels = [ 'tearRate','age', 'prescript', 'astigmatic']
lensesTree =createTree(lenses, lensesLabels)
print(lensesTree)
#创建
createPlot(lensesTree)
