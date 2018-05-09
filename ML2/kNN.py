from numpy import *
import operator
from os import listdir


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


group, labels = createDataSet()
print(group)
print(labels)


#
# 用于分类的输入向量是inX，
# 输入的训练样本集为dataSet，
# 标签向量为labels ，
# 最后的参数k 表示用于选择最近邻居的数目，
# 其中标签向量的元素数目和矩阵dataSet 的行数相同。
#
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]  # 求数组的长度
    # ❶（以下三行）距离计算
    # 第二个参数的意思就是把inX补成有datasetsize行数的矩阵,
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    # print("====================================")
    # print(diffMat)
    sqDiffMat = diffMat ** 2  # diffMat相乘
    # print("====================================")
    # print(sqDiffMat)
    sqDistances = sqDiffMat.sum(axis=1)  # axis=1按照列求和，0是按照行求和
    distances = sqDistances ** 0.5  # 开方，结果为[1.48660687 1.41421356 0.0 0.1 ]
    # print("====================================")
    # print(distances)
    sortedDistIndicies = distances.argsort()  # argsort把想向量中的每个元素进行排序  [2 3 1 0]
    # print("====================================")
    # print(sortedDistIndicies)
    classCount = {}
    # ❷ （以下两行）选择距离最小的k个点
    # 循环执行的过程，大概是分别对照，然后给AB计数
    # dict_items([('B', 1)])
    # dict_items([('B', 2)])
    # dict_items([('B', 2), ('A', 1)])
    #
    for i in range(k):
        # sortedDistIndicies=[2 3 1 0],sortedDistIndicies[i]取出的是第几个，labels取出的是对应的AB值
        voteIlabel = labels[sortedDistIndicies[i]]
        # classCount.get可以理解赋值默认值0，然后得到一个就加一，累加
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    # 根据元素的第二个排序，返回的结果[('B', 2), ('A', 1)]
    sortedClassCount = sorted(classCount.items(),
                              key=operator.itemgetter(1), reverse=True)

    return sortedClassCount[0][0]  # 返回B


print(classify0([0, 0], group, labels, 3))


#
def file2matrix(filename):
    love_dictionary = {'largeDoses': 3, 'smallDoses': 2, 'didntLike': 1}
    fr = open(filename)  # 打开文件
    arrayOLines = fr.readlines()  # 读文件的所有行
    numberOfLines = len(arrayOLines)  # get the number of lines in the file（得到文件行数）
    returnMat = zeros((numberOfLines, 3))  # prepare matrix to return（创建Numpy矩阵）
    classLabelVector = []  # prepare labels return 设置返回的级别的数组
    index = 0
    for line in arrayOLines:
        line = line.strip()  # 用于移除字符串头尾的空格
        listFromLine = line.split('\t')  # 根据空格截取，txt文件中不同种类就是用空格来差分的
        returnMat[index, :] = listFromLine[0:3]  # 一行的前三个
        if (listFromLine[-1].isdigit()):  # 方法检测字符串是否只由数字组成
            classLabelVector.append(int(listFromLine[-1]))  # 直接添加123的数字
        else:
            classLabelVector.append(love_dictionary.get(listFromLine[-1]))  # 将文字转换成文字进行
        index += 1  # +1之后准备返回2个集合，一个是矩阵，一个是好感度
    return returnMat, classLabelVector


def autoNorm(dataSet):
    minVals = dataSet.min(0)  # 将每列的最小值放在minVals中
    maxVals = dataSet.max(0)  # 将每列的最大值放在maxVals中
    ranges = maxVals - minVals  # 计算可能的取值范围
    normDataSet = zeros(shape(dataSet))  # 创建新的返回矩阵
    m = dataSet.shape[0]  # 得到数据集的行数  shape方法用来得到矩阵或数组的维数
    # tile:numpy中的函数。tile将原来的一个数组minVals，扩充成了m行1列的数组
    # 矩阵中所有的值减去最小值
    normDataSet = dataSet - tile(minVals, (m, 1))
    # 矩阵中所有的值除以最大取值范围进行归一化
    normDataSet = normDataSet / tile(ranges, (m, 1))  # 特征值相除
    # 返回归一矩阵 取值范围 和最小值
    return normDataSet, ranges, minVals


def datingClassTest():
    hoRatio = 0.99
    # 从文件中读取数据并转化为归一值
    datingDataMat, datingLabels = file2matrix('datingTestSet.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 得到数据集的行数  shape方法用来得到矩阵或数组的维数
    m = normMat.shape[0]
    # print("m:%s" %m)
    # 测试数据的个数
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    # 循环判断
    for i in range(numTestVecs):
        # classify0是我们最早写的临近算法参数意义如下
        # 用于分类的输入向量是inX==》normMat[i, :]归一后的数据第i行，所有的数值
        # 输入的训练样本集为dataSet，==》normMat[numTestVecs:m, :],用于测试的数据集合
        # 标签向量为labels ，==》 datingLabels[numTestVecs:m] 得到的好感度的集合，和勇于测试数据的集合的行数相同
        # 最后的参数k 表示用于选择最近邻居的数目 ==》取3个点，然后组成{（a,2）,(b,1)的集合，取出个数最多的作为结果}
        # *其中标签向量的元素数目和矩阵dataSet 的行数相同。
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): errorCount += 1.0
    print("the total error rate is: %f" % (errorCount / float(numTestVecs)))


def classifyPerson():
    resultList = ['not at all', 'in small doses', 'in large doses']
    percentTats = float(input("percentage of time spent playing video games?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    # 取得数据和好感度数组
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = array([ffMiles, percentTats, iceCream])
    # 第一个参数是需要计算的内容可以看到使用（实际数据-最小值）/可能的取值范围。特征值相除
    classifierResult = classify0((inArr - minVals) / ranges, normMat, datingLabels, 3)
    print("You will probably like this person: ", resultList[classifierResult - 1])


# 将32*32的二进制图像矩阵转换为1024向量
def img2vector(filename):
    returnVect = zeros((1, 1024))  # 创建1*1024的图像数组
    fr = open(filename)  # 打开文件
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0, 32 * i + j] = int(lineStr[j])  # 将每行的32个字符存入数组
    return returnVect


def handwritingClassTest():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')
    m = len(trainingFileList)
    # 这个矩阵m行（m个文件，1024列每一行都是这个数字的字节码组成的数组）
    trainingMat = zeros((m, 1024))
    for i in range(m):
        filenameStr = trainingFileList[i]  # 文件名.后缀
        fileStr = filenameStr.split('.')[0]  # 文件名
        classNumStr = int(fileStr.split("_")[0])  # 文件名是4_5.txt ，所以取得的数字
        hwLabels.append(classNumStr)  # 得到的数据
        #
        trainingMat[i, :] = img2vector('trainingDigits/%s' % filenameStr)
    testFileList = listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        filenameStr = testFileList[i]
        fileStr = filenameStr.split('.')[0]  # 文件名
        classNumStr = int(fileStr.split("_")[0])  # 文件名是4_5.txt ，所以取得的数字
        vectorUnderTest = img2vector('testDigits/%s' % filenameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)

        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        if(classifierResult!=classNumStr):errorCount +=1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount / float(mTest)))


