from ML3.treePoltter import retrieveTree,getTreeDepth,getNumLeafs,createPlot

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
myTree=retrieveTree(0)
myTree['no surfacing'][3] = 'maybe'
myTree['no surfacing'][4] = 'maybe'
print(myTree)
createPlot(myTree)