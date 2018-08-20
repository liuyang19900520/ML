from os import listdir

from ML2.kNN import classify0
from numpy import *


# 将32*32的二进制图像矩阵转换为1024向量
def img2vector(filename):
    # 创建1*1024的图像数组
    returnVect = zeros((1, 1024))
    # 打开文件
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            # 将每行的32个字符存入数组,这个数组1行1024列
            returnVect[0, 32 * i + j] = int(lineStr[j])
    return returnVect


def handwritingClassTest():
    hwLabels = []
    # 获取所有文件
    trainingFileList = listdir('trainingDigits')
    # 获取文件的个数
    m = len(trainingFileList)
    # 这个矩阵m行（m个文件，1024列每一行都是这个数字的字节码组成的数组）
    trainingMat = zeros((m, 1024))
    for i in range(m):
        # 文件名.后缀
        filenameStr = trainingFileList[i]
        # 文件名
        fileStr = filenameStr.split('.')[0]
        # 文件名是4_5.txt ，所以取得的数字
        classNumStr = int(fileStr.split("_")[0])
        # 得到的数据放入labels的数组中
        hwLabels.append(classNumStr)
        # 文件名转成一个数组，i是这个而文件数组中的第几个
        trainingMat[i, :] = img2vector('trainingDigits/%s' % filenameStr)
    # 排列出testDigits中的
    testFileList = listdir('testDigits')
    # 错误的个数
    errorCount = 0.0
    # 获取测试文件夹中文件的个数
    mTest = len(testFileList)
    for i in range(mTest):
        # 文件名.后缀
        filenameStr = testFileList[i]
        # 文件名
        fileStr = filenameStr.split('.')[0]
        # 文件名是4_5.txt ，所以取得的数字
        classNumStr = int(fileStr.split("_")[0])
        # 得到测试的一个图像
        vectorUnderTest = img2vector('testDigits/%s' % filenameStr)
        # 文件名是4_5.txt ，所以取得的数字
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        # 测试
        print("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        # 如果实际的label结果与实际判定出的不准，计数
        if (classifierResult != classNumStr): errorCount += 1.0
    print("\nthe total number of errors is: %d" % errorCount)
    print("\nthe total error rate is: %f" % (errorCount / float(mTest)))
