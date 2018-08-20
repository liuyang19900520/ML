from numpy import *
import operator

# 创建数据集合
# 4组数据，每组数据有两个我们已知的属性或者特征值
# group矩阵：每行包含一个不同的数据，可想象某个日志文件中不同的测量点或者入口
# 向量labels：包含了每个数据点的标签信息，labels包含的元素个数等于group矩阵行数
def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


# 创建数据集合
# 参数：
#    inx：用于分类的输入向量
#    dataSet:输入的训练样本集
#    labels:标签向量
#    k:表示用于选择最近邻居的数目
# 备注：
#    标签向量的元素数目和矩阵dataSet的行数
def classify0(inX, dataSet, labels, k):
    # 求数组的长度
    dataSetSize = dataSet.shape[0]

    # 第二个参数的意思就是把inX补成有datasetsize行数的矩阵，每个元素值重复1次
    # 并且组成的新矩阵-输入的训练样本;表示目标输入向量到样本中每个元素的距离，会存在负数的情况
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet

    # diffMat相乘，得到平方，避免负数的情况
    sqDiffMat = diffMat ** 2

    # axis=1按照列求和，0是按照行求和
    # 2行4列的矩阵，就会得到一个数组，数组中有4个元素
    sqDistances = sqDiffMat.sum(axis=1)

    # 开方计算距离
    distances = sqDistances ** 0.5

    # 数组排序，将排序的数组值的索引值返回
    sortedDistIndicies = distances.argsort()

    # 创建一个空数组
    classCount = {}

    # k:选择距离最小的k个点
    for i in range(k):
        # sortedDistIndicies=[2 3 1 0]（索引值）
        # sortedDistIndicies[i]取出的是第几索引值，labels[索引]得到的是显示的结果标签，及A或B
        # voteIlabel是最后显示的结果
        voteIlabel = labels[sortedDistIndicies[i]]

        # classCount.get可以理解赋值默认值0，然后得到一个就加一，累加
        # 循环3次的classCount结果是
        # 第一次：{'B': 1}
        # 第二次：{'B': 2}
        # 第三次：{'B': 2, 'A': 1}
        # classCount[voteIlabel]就是这个label的个数
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1

    # classCount.items()：dict_items([('B', 2), ('A', 1)])
    # key 是根据元素的第2项排序
    # reverse 倒序
    # sortedClassCount结果为[('B', 2), ('A', 1)]
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)
    # 返回第一项目的label
    return sortedClassCount[0][0]