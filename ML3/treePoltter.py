import matplotlib.pyplot as plt

# （以下三行）定义文本框和箭头格式
decisionNode = dict(boxstyle="sawtooth", fc="0.8")
leafNode = dict(boxstyle="round4", fc="0.8")
arrow_args = dict(arrowstyle="<-")


# （以下两行）绘制带箭头的注解
# xycoords为目标点的坐标系统,axes fraction指按照坐标轴相对位置
# xytext在坐标为xytext处添加坐标为x, y的点的注释
# textcoords为目标点的坐标系统, axes fraction指按照坐标轴相对位置
# bbox应该是（矩形的）文本框属性，alpha是相对不透明度，facecolor应该是背景颜色
# arrowprops的属性：shrink, facecolor, width（箭头宽度），headwidth（箭头宽度)
def plotNode(nodeTxt, centerPt, parentPt, nodeType):
    createPlot.ax1.annotate(nodeTxt, xy=parentPt, xycoords='axes fraction', xytext=centerPt, textcoords='axes fraction',
                            va="center", ha="center", bbox=nodeType, arrowprops=arrow_args)


def createPlot():
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    createPlot.ax1 = plt.subplot(111, frameon=True)
    plotNode('决策节点', (0.5, 0.1), (0.1, 0.5), decisionNode)
    plotNode('叶节点', (0.8, 0.1), (0.3, 0.8), leafNode)
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.show()


#
# 取得叶节点数目，就是横着的数目
# 遍历整棵树，累计叶子节点的个数
#
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


#
# 取得树的层数
# 计算遇到判断节点的个数，该函数的终止条件是叶子节点，一旦遇到叶子节点，从递归中返回，树的深度变量+1
#
def getTreeDepth(myTree):
    maxDepth = 0
    firstStr = list(myTree.keys())[0]
    secondDict = myTree[firstStr]
    for key in secondDict.keys():
        # 判断是不是字典类型
        if type(secondDict[key]).__name__ == 'dict':
            # 如果是字典的话，在第二层所有的层级数目上+1
            thisDepth = 1 + getTreeDepth(secondDict[key])
        else:
            # 如果不是字典类型，就加1层
            thisDepth = 1
        # 该节点的层级数>最大层级的时候，将最大层级赋值为最大层级
        if thisDepth > maxDepth: maxDepth = thisDepth
    return maxDepth


#
# 上述2个方法具有相同的数据结构，在python的字典中存储树信息。
# 第一个关键字是第一次划分数据集的类别标签，附带的数值表示自己点的取值
#

def retrieveTree(i):
    listOfTrees = [{'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}},
                   {'no surfacing': {0: 'no', 1: {'flippers': {0: {'head': {0: 'no', 1: 'yes'}}, 1: 'no'}}}}]
    return listOfTrees[i]


# 算父节点和子节点的中间位置，并在此处添加简单的文本标签信息
#
# 第一参数 现在的面板
# 第二参数 父面板
# 第三参数 写出来的数字
#
def plotMidText(cntrPt, parentPt, txtString):
    xMid = (parentPt[0] - cntrPt[0]) / 2.0 + cntrPt[0]
    yMid = (parentPt[1] - cntrPt[1]) / 2.0 + cntrPt[1]
    createPlot.ax1.text(xMid, yMid, txtString, va="center", ha="center", rotation=30)


def plotTree(myTree, parentPt, nodeTxt):
    # （以下两行）计算宽和高
    numLeafs = getNumLeafs(myTree)
    depth = getTreeDepth(myTree)
    firstStr = list(myTree.keys())[0]
    #  横向的位移+（1+叶子个数）/2/横向长度，纵向位移
    #
    # plotTree.totalW：树的宽度
    # plotTree.totalD ：树的深度
    # xOff 横坐标，yOff纵坐标
    #
    cntrPt = (plotTree.xOff + (1.0 + float(numLeafs)) / 2.0 / plotTree.totalW, plotTree.yOff)
    #  标记子节点属性值
    plotMidText(cntrPt, parentPt, nodeTxt)
    plotNode(firstStr, cntrPt, parentPt, decisionNode)
    secondDict = myTree[firstStr]
    # （以下两行）减小y坐标，并标注此处将要绘制子节点
    plotTree.yOff = plotTree.yOff - 1.0 / plotTree.totalD
    for key in secondDict.keys():
        # 递归
        # 如果不是叶子节点
        if type(secondDict[key]).__name__ == 'dict':
            plotTree(secondDict[key], cntrPt, str(key))  # recursion
        # 如果是叶子节点，就画上一个节点
        else:
            # 横向坐标值
            plotTree.xOff = plotTree.xOff + 1.0 / plotTree.totalW
            # 画节点
            plotNode(secondDict[key], (plotTree.xOff, plotTree.yOff), cntrPt, leafNode)
            # 写字
            plotMidText((plotTree.xOff, plotTree.yOff), cntrPt, str(key))
    # 全部操作结束后，增加Y的坐标
    plotTree.yOff = plotTree.yOff + 1.0 / plotTree.totalD

def createPlot(inTree):
    #面板颜色
    fig = plt.figure(1, facecolor='white')
    fig.clf()
    axprops = dict(xticks=[], yticks=[])
    #frameon=False 没有边框
    createPlot.ax1 = plt.subplot(111, frameon=False, **axprops)
    #子节点个数是width，层级是height
    plotTree.totalW = float(getNumLeafs(inTree))
    plotTree.totalD = float(getTreeDepth(inTree))
    # -0.5/叶子个数,向左侧移半格
    plotTree.xOff = -0.5 / plotTree.totalW;
    # 纵向移动1个格
    plotTree.yOff = 1.0;
    plotTree(inTree, (0.5, 1.0), '')
    plt.show()
