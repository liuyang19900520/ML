from numpy import *

# 来处理输入格式问题
from ML2.kNN import classify0


def file2matrix(filename):
    # 设置喜欢程度的数字标识
    love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
    # 打开文件
    fr = open(filename)
    # 读文件的所有行
    arrayOLines = fr.readlines()
    # 得到文件行数
    numberOfLines = len(arrayOLines)
    # 创建一个numberOfLines行，3列的矩阵，所有的元素都是0
    returnMat = zeros((numberOfLines, 3))
    # 设置返回的级别的数组
    classLabelVector = []  # prepare labels return
    index = 0
    for line in arrayOLines:
        # 用于移除字符串头尾的空格
        line = line.strip()
        # 根据空格截取，txt文件中不同种类就是用空格来差分的
        listFromLine = line.split('\t')
        # 可以理解把文本中的每一行的前三个元素，放入returnMat的[index]行的前三个元素
        returnMat[index, :] = listFromLine[0:3]
        # 方法检测文本每一行最后的字符串是否只由数字组成
        if (listFromLine[-1].isdigit()):
            # 直接添加123的数字
            classLabelVector.append(int(listFromLine[-1]))
        else:
            # 将文字转换成数字返回
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))
        # +1之后准备对returnMat的下一行进行操作
        index += 1
    # 返回2个集合，一个是矩阵，一个是好感度
    # 这2个集合就是KNN算法中的group 和labels
    return returnMat, classLabelVector


# 以自动将数字特征值转化为0到1的区间
def autoNorm(dataSet):
    # 将每列的最小值放在minVals中
    minVals = dataSet.min(0)
    # 将每列的最大值放在maxVals中
    maxVals = dataSet.max(0)
    # 计算可能的取值范围
    ranges = maxVals - minVals
    # shape函数取得的tuple是这个数组的各个维度，再将各个维度重新赋值为0
    normDataSet = zeros(shape(dataSet))
    # 得到数据集的行数，shape方法用来得到矩阵或数组的维数
    m = dataSet.shape[0]
    # tile:numpy中的函数。tile将原来的一个数组minVals，扩充成了m行1列的数组
    # 矩阵中所有的值减去最小值
    normDataSet = dataSet - tile(minVals, (m, 1))
    # 矩阵中所有的值除以最大取值范围进行归一化
    normDataSet = normDataSet / tile(ranges, (m, 1))  # 特征值相除
    # 返回归一矩阵 取值范围 和最小值
    return normDataSet, ranges, minVals


# 分类器针对约会网站的测试代
def datingClassTest():
    # 预计取出10%
    hoRatio = 0.10
    # 以下2行，从文件中读取数据并转化为归一值
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 得到数据集的行数  shape方法用来得到矩阵或数组的维数
    m = normMat.shape[0]
    # 测试数据的个数
    numTestVecs = int(m * hoRatio)
    # 初始化错误的个数
    errorCount = 0.0
    # 循环判断
    for i in range(numTestVecs):
        # classify0是我们最早写的临近算法参数意义如下
        # 用于分类的输入向量是inX：normMat[i, :]归一后的数据第i行的所有的数值
        # 输入的训练样本集为dataSet：normMat[numTestVecs:m, :],用于测试的数据集合
        # 标签向量为labels：datingLabels[numTestVecs:m] 得到的好感度的集合，和用于测试数据的集合的行数相同
        # 最后的参数k：表示用于选择最近邻居的数目，取3个点，然后组成{（a,2）,(b,1)的集合，取出个数最多的作为结果}
        # 备注：其中标签向量的元素数目和矩阵dataSet的行数相同。
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        # 通过KNN算法得到结果集，是一个分类，the real answer取得是labels的第i个索引得到的值
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        # 如果上述2者不同，将错误数值+1
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    # 计算错误率（错误个数/总数）
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']

    # 负责输入3项目内容
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))

    # 取得数据和好感度数组
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])

    # 第一个参数是需要计算的0到1中间的输入值：（实际数据-最小值）/可能的取值范围，特征值相除
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    # 输出结果
    print("You will probably like this person: ", resultList[classifierResult - 1])
