import operator
from math import log


# 创建数据集
def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing', 'flippers']
    return dataSet, labels


# 计算给定数据集的香农熵
def calcShannonEnt(dataSet):
    # 计算实例的总数
    numEntries = len(dataSet)
    labelCounts = {}
    # 为所有可能创建字典，即每一种情况
    for featVec in dataSet:
        # 创建一个数据字典，它的键值是最后一列的数，获得最后的评定
        currentLabel = featVec[-1]
        # 如果当前键值不存在，则扩展字典并将当前键值加入字典
        if currentLabel not in labelCounts.keys():
            # 这个评定不在字典中，就添加，并将值设置为0
            labelCounts[currentLabel] = 0
        # 这个评定在列表中，就给数值+1
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    # 最后得到的labelCounts应该是每个评定以及每个评定的个数
    for key in labelCounts:
        prob = float(labelCounts[key]) / numEntries
        # 以2为底求对数log2(下)prob（上），计算香农熵
        shannonEnt -= prob * log(prob, 2)
    return shannonEnt


#
# 按照指定特征划分数据集合
#  dataset 等待划分的数据集合
#  axis 划分数据集的特征（就是去掉最后labels剩下的特征值的index）
#  value 需要返回的的特征的值
#
# 返回的是：在这个特征值下，有多少数据
#
def splitDataSet(dataSet, axis, value):
    # 创建这个list对象的原因是为了不修改原始数据集合，因为splitDataSet函数在同一数据上多次引用
    retDataSet = [];
    for featVec in dataSet:
        # 当需要返回的特征值与fetVec（fet就是一条数据的3个特征值），fetVet[i]就是获取一个特征
        # 当得到的特征与我们传入的特征（value）
        if featVec[axis] == value:
            # 以下两行取出除去这个特征之外的数据,
            # 从index为0的元素一直到底axis元素
            reducedFeatVec = featVec[:axis]
            # 如果使用a.append(n)，[1,2,3,[4,5,6,]];而a.extend(b)==[1,2,3,4,5,6]
            # 从index为axis+1的元素一直到最后元素
            reducedFeatVec.extend(featVec[axis + 1:])
            # 将上述得出的特征值添加到返回值中
            retDataSet.append(reducedFeatVec)
    # 返回了这个特征下的下的所有数据
    return retDataSet


#
# 选取特征，划分数据集合，计算出最好的划分数据集特征
# 要求：
# 1，数据必须是一种由列表元素组成的列表，而且所有列表元素都具有相同的数据长度
# 2，数据的最后一列，或者每个实例最后一个元祖是当前实例的类别的标签
#
# 返回：应该是第几个特征是最好的分类特征
#
def chooseBestFeatureToSplit(dataSet):
    # 获取数据集合一共有多少特征值
    numFeatures = len(dataSet[0]) - 1
    # 计算了整个数据集的原始香农熵,保存最初的无序度量值，用于与划分完之后的数据集计算的熵值进行比较。
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1
    # 第一个for循环遍历了所有特征（0代表特征一，1代表特征二等等）
    for i in range(numFeatures):
        # 创建唯一的分类标签列表,将数据集中所有第i个特征值写入这个新列表
        # 获得所有数据第i个特征组成给一个列表，在uniquevals进行去装
        featList = [example[i] for example in dataSet]
        # featList是一个数组，而uniqueVals是等于把featList进行了去重，得到了不重复的特征值
        uniqueVals = set(featList)
        newEntropy = 0.0
        # 计算每种划分方式的信息熵
        # 遍历当前特征中的唯一属性值，对每一个特征划分一次数据集2
        # 这里的value是每个特征值的具体指，比如0代表可以游泳，1代表不能游泳等等
        for value in uniqueVals:
            # dateSet 是这个数据集合，i是这个特征值的index，value是刚刚去重后的特征值
            # 得出来的应该是符合条件的数据集合
            subDataSet = splitDataSet(dataSet, i, value)
            # len计算元素个数，符合特征的子集的个数/总数
            prob = len(subDataSet) / float(len(dataSet))
            # 新的熵=这个比例*子集的熵（各个子集相加）
            newEntropy += prob * calcShannonEnt(subDataSet)
            infoGain = baseEntropy - newEntropy
            # 信息增益是熵的减少或者数据无须度的减少，所以infoGain越大说明新的enwEntropy越小，数据越好。
        if (infoGain > bestInfoGain):
            # 计算最好的信息增益
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature


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

def createTree(dataSet, labels):
    # 创建了列表变量classList：包含了数据集的所有类标签
    # 获取这个类的最后一项，和要求2相同
    classList = [example[-1] for example in dataSet]
    # 递归函数有2个停止条件：
    # （以下两行）类别完全相同则停止继续划分
    # 第一个停止条件：classList 中第一个分类的数量=classList的len：
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    # （以下两行）遍历完所有特征时返回出现次数最多的
    # 第二个停止条件：dataSet使用完了所有特征，仍不能将数据集合划分成仅包含一类别的分组
    if len(dataSet[0]) == 1:
        # 由于无法返回唯一的类标签，使用majorityCnt取得最多频率的标签
        return majorityCnt(classList)
    # 划分数据集合，计算出最好的划分数据集特征
    bestFeat = chooseBestFeatureToSplit(dataSet)
    # 获得标签列表中最好的数据集合的值
    bestFeatLabel = labels[bestFeat]
    # 字典类型存储树的信息
    myTree = {bestFeatLabel: {}}
    # 得到列表包含的所胡属性值，并且删掉
    del (labels[bestFeat])
    # 遍历当前选择特征包含的所有属性值
    featValues = [example[bestFeat] for example in dataSet]
    # set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
    # 构成了一个不重复的属性值集合
    uniqueVals = set(featValues)
    # 遍历这个不重复的属性集合，
    for value in uniqueVals:
        # subLabels 就是labels去掉列表包含属性值的后的标签列表
        # 为了保证每次调用函数createTree() 时不改变原始列表的内容，使用新变量subLabels 代替原始列表
        subLabels = labels[:]
        # bestFeatLabel=列表中最好数据的集合的值  value=不重复的标签
        # 得到的返回值将被插入到字典变量myTree 中
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)

    return myTree


#
# inputTree  树
# featLabels  显示的种类
# testVec ，就是判断的依据
#
def classify(inputTree, featLabels, testVec):
    # 获取第一个标签字符串
    firstStr = list(inputTree.keys())[0]
    # 根据标签字符串取得该标签下的树的数据数据
    secondDict = inputTree[firstStr]
    # 将第一标签字符串转换为索引
    featIndex = featLabels.index(firstStr)
    # 遍历该标签下树的key，也就是第二个集合中，有多少个键值对，key代表着第二层决策的键
    for key in secondDict.keys():
        # key是第二层集合的键
        # featIndex是第一个决策的键
        # testVec[featIndex] 用于firstStr所在索引所对应的值（这里的值是1,0，分别代表是否特征1，是否特征2）
        # 上述值与与第二层决策树节点的key对应，也就是说由于这个inputTree第一层主要是进入决策树用，一定有 testVec[featIndex] == key
        if testVec[featIndex] == key:
            # 如果进入到第二层，判断是不是子节点，如果还有层级，递归
            if type(secondDict[key]).__name__ == 'dict':
                classLabel = classify(secondDict[key], featLabels, testVec)
            else:
                # 如果进入到第二层，如果没有层级了，得到的就是这一层的结果
                classLabel = secondDict[key]
    # 最后的classLabel就是判断依据的key 得到的值
    return classLabel

# pickle:暂时持久化的set 与 get
def storeTree(inputTree, filename):
    import pickle
    fw = open(filename, 'w')
    pickle.dump(inputTree, fw)
    fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)
