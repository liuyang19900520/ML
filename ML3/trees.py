from math import log
import operator


def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


def calcShannonEnt(dataSet):
    # 计算实例的总数
    numEntries = len(dataSet)
    labelCounts = {}
    # 为所有可能创建字典
    for featVec in dataSet:
        # 创建一个数据字典，它的键值是最后一列的数
        currentLabel = featVec[-1]
        # 如果当前键值不存在，则扩展字典并将当前键值加入字典
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
            labelCounts[currentLabel] += 1
        shannonEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        # 以2为底求对数log2(下)prob（上），计算香农熵
        shannonEnt -= prob * log(prob, 2)

    return shannonEnt


#
# 按照指定特征划分数据集合
#  dataset 等待划分的数据集合
#  axis 划分数据集的特征
#  value 需要返回的的特征的值
#
# 返回的是
#
def splitDataSet(dataSet, axis, value):
    # ❶ 创建新的list对象
    # 创建这个list对象的原因是为了不修改原始数据集合，因为splitDataSet函数在同一数据上多次引用
    retDataSet = [];
    for featVec in dataSet:
        if featVec[axis] == value:
            # ❷ （以下三行）抽取
            reducedFeatVec = featVec[:axis]
            # 如果使用a.append(n)，[1,2,3,[4,5,6,]];而a.extend(b)==[1,2,3,4,5,6]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


#
# 选取特征，划分数据集合，计算出最好的划分数据集特征
# 要求：
# 1，数据必须是一种由列表元素组成的列表，而且所有列表元素都具有相同的数据长度
# 2，数据的最后一列，或者每个实例最后一个元祖是当前实例的类别的标签
#
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    # 计算了整个数据集的原始香农熵,保存最初的无序度量值，用于与划分完之后的数据集计算的熵值进行比较。
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0;
    bestFeature = -1
    # 第一个for循环遍历了所有特征
    for i in range(numFeatures):
        # ❶ （以下两行）创建唯一的分类标签列表,
        # 创建新的列表，将数据集中所有第i个特征值写入这个新列表
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        # ❷ （以下五行）计算每种划分方式的信息熵
        # 遍历当前特征中的唯一属性值，对每一个特征划分一次数据集2
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            # len计算元素个数
            prob = len(subDataSet) / float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)
            infoGain = baseEntropy - newEntropy
            # 信息增益是熵的减少或者数据无须度的减少
            if (infoGain > bestInfoGain):
                # ❸  计算最好的信息增益
                bestInfoGain = infoGain
                bestFeature = i
        return bestFeature


## set 是集合数据类型，从列表中从创建集合是python语言中得到列表中唯一元素值的最快方法


#
# 改函数使用分类名称的列表，然后创建键值为classList中唯一的字典数据，
# 字典对象存储了classList中每个类标签出现的频率，租后利用operator操作键值排序字典，并返回出现次数最多的分类名称
#
# 　classList的解释：这是分类名称的列表
#
def majorityCnt(classList):
    # 创建分类的统计
    classCount = {}
    for vote in classList:
        # 如果vote不在classCount中，将这个出现的次数设置为0
        if vote not in classCount.keys():
            classCount[vote] = 0
        # 将出现的次数+1
        classCount[vote] += 1
    # 将出现的次数排序
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    # 返回出现频率最多的那个class
    return sortedClassCount[0][0]


#
#  参数1：数据集，参数2:标签列表（包含了数据集中所有的特征的标签）
#  数据集的要求：与之前相同
# 1，数据必须是一种由列表元素组成的列表，而且所有列表元素都具有相同的数据长度
# 2，数据的最后一列，或者每个实例最后一个元祖是当前实例的类别的标签
# 　
#
def createTree(dataSet, labels):
    #创建了列表变量classList：包含了数据集的所有类标签
    # 获取这个类的最后一项，和要求2相同
    classList = [example[-1] for example in dataSet]
    # 递归函数有2个停止条件：
    # ❶ （以下两行）类别完全相同则停止继续划分
        #classList 中第一个分类的数量=classList的len
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # ❷ （以下两行）遍历完所有特征时返回出现次数最多的
        # dataSet使用完了所有特征，仍不能将数据集合划分成仅包含一类别的分组
    if len(dataSet[0]) == 1:
        # 由于无法返回唯一的类标签，使用majorityCnt取得最多频率的标签
        return majorityCnt(classList)
    #划分数据集合，计算出最好的划分数据集特征
    bestFeat = chooseBestFeatureToSplit(dataSet)
    #获得标签列表中最好的数据集合的值
    bestFeatLabel = labels[bestFeat]
    #字典类型存储树的信息
    myTree = {bestFeatLabel: {}}
    # ❸ 得到列表包含的所胡属性值，并且删掉
    del (labels[bestFeat])
    #遍历当前选择特征包含的所有属性值
    featValues = [example[bestFeat] for example in dataSet]
    #set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    #构成了一个不重复的属性值集合
    uniqueVals = set(featValues)
    # 遍历这个不重复的属性集合，
    for value in uniqueVals:
        #subLabels 就是labels去掉列表包含属性值的后的标签列表
        #为了保证每次调用函数createTree() 时不改变原始列表的内容，使用新变量subLabels 代替原始列表
        subLabels = labels[:]
        # bestFeatLabel=列表中最好数据的集合的值  value=不重复的标签
        # 得到的返回值将被插入到字典变量myTree 中
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree
