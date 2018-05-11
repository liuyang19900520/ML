from ML3.treePoltter import retrieveTree,getTreeDepth,getNumLeafs,createPlot
# from ML3.trees import createDataSet,classify,createTree,storeTree,grabTree,createTree2
from ML3.trees2 import createDataSet,classify,createTree,storeTree,grabTree
#
# myDat, labels = createDataSet()
# print(myDat)
# print(11111111111111111111111111111111)
# # myDat[0][-1] = 'maybe'
# # print(calcShannonEnt(myDat))
# # print(22222222222222222222222222222222)
#
# #
# #0.9287712379549449
# #11111111111111111111111111111111
# #1.3931568569324173
# #22222222222222222222222222222222
# #
#
#
# myDat, labels = createDataSet()
# print(myDat)
# print(11111111111111111111111111111111)
#
# r1=splitDataSet(myDat,0,1)
# r2=splitDataSet(myDat,0,0)
# print(r1)
# print(r2)
# print(33333333333333333333333333333333333333333333333333333)
# #
# #[[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
# #11111111111111111111111111111111
# #[[1, 'yes'], [1, 'yes'], [0, 'no']]
# #[[1, 'no'], [1, 'no']]
# #33333333333333333333333333333333333333333333333333333
# #
#
#
#
# # print(33333333333333333333333333333333333333333333333333333)
# # myDatx,labels=createDataSet()
# # chooseBestFeatureToSplit(myDatx)
# # print(myDatx)
# # print(33333333333333333333333333333333333333333333333333333)
# #
#
# # myDat, labels = trees.createDataSet()
# # print(chooseBestFeatureToSplit(myDat))
#

# myDat, labels = createDataSet()
# myTree = createTree(myDat, labels)
# print(myTree)

# result:
# {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}

#treePoltter.retrieveTree(1)
# myTree=retrieveTree(0)
# myTree['no surfacing'][3] = 'maybe'
# myTree['no surfacing'][4] = 'maybe'
# print(myTree)
# createPlot(myTree)

# myDat,labels=createDataSet()
# print(labels)
# myTree=retrieveTree(0)
# r=classify(myTree,labels,[1,0])
# print(r)
#
# storeTree(myTree)

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