from ML3.trees import *

myDat, labels = createDataSet()
myTree = createTree(myDat, labels)

print("myTree===", myTree)
print("list(myTree.keys())[0]===", list(myTree.keys())[0])


def getNumLeafs(myTree):
    numLeafs = 0
    # 获得该层级上的所有特征标签
    firstStr = list(myTree.keys())[0]
    # 获得该层级的内容
    secondDict = myTree[firstStr]
    # 在这个节点的内容再次获得特征的key
    for key in secondDict.keys():
        # （以下三行）测试节点的数据类型是否为字典
        # 判断子节点是不是字典类型（type）
        if type(secondDict[key]).__name__ == 'dict':
            # 为叶子节点添加特征
            numLeafs += getNumLeafs(secondDict[key])
        else:
            # 直接加1
            numLeafs += 1
    return numLeafs
