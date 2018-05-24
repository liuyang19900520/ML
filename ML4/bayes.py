from numpy import *


#
# 创建实实验样本，
# 返回值1：词条切割后的文档集合
# 返回值2：一个类别标签的集合
#
def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    # 1 is abusive（侮辱性文字）, 0 not
    classVec = [0, 1, 0, 1, 0, 1]
    return postingList, classVec


#
# 创建一个包含在所有文档中不重复词的列表，使用set数据类型
#
#
def createVocabList(dataSet):
    # 创建一个空的集合
    vocabSet = set([])
    for document in dataSet:
        # 创建2个集合的合并
        vocabSet = vocabSet | set(document)
    return list(vocabSet)


#
# 参数1：词汇表，参数2：输入的文档
# return：文档向量（向量的每一个元素为1或者0，分别表示词汇表中的单词是否在文档中出现）
#
def setOfWords2Vec(vocabList, inputSet):
    # 创建一个所含元素都是0 的向量
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        # 如果输入的文档中的词汇在vocablist中存在就设置为1
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec


#
# 词袋模型
# 和原有的模型的差别在于+=1 这一块
# 如果输入的文档中的词汇在vocablist中存在就设置为1，现在是出现就累加，
# 在词集中，每个单词只能出现一次，而在词袋中，可以出现多次
#
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec


#
# trainMatrix：文档矩阵（postingList中的每个元素在my Vocabulary中是否出现的情况）
# trainCategory：每篇文章类别标签构成的向量
#
#
def trainNB0(trainMatrix, trainCategory):
    # 计算每个类别中的文档个数
    numTrainDocs = len(trainMatrix)
    # 计算my Vocabulary的个数
    numWords = len(trainMatrix[0])
    # sum(测试分类的和)/测试分类的数量
    pAbusive = sum(trainCategory) / float(numTrainDocs)
    # 分母变量是一个元素个数等于词汇表大小的NumPy数组。
    # sum(trainCategory)是向量为1的与文档个数总作比较得出pbAusive
    # 初始化概率(p0 代表0（正常）词条，p1代表1（侮辱）词条，出现文档中的词条# )
    p0Num = ones(numWords);
    p1Num = ones(numWords)  # change to ones()
    p0Denom = 2.0;
    p1Denom = 2.0  # change to 2.0

    for i in range(numTrainDocs):
        # 如果词条出现在文档中, 增加该词条的计数值
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]  # 将传递的参数（文档矩阵）自加，得到在总词条中出现的个数的矩阵
            p1Denom += sum(trainMatrix[i])  # 这里是矩阵值相加，最后得出矩阵中元素出现的次数和
        # 增加所有词条的计数值
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    # 对于每个元素/该类别的总元素（矩阵/向量，这个词出现在侮辱性语句中的频率）
    p1Vect = log(p1Num / p1Denom)  # change to log()
    p0Vect = log(p0Num / p0Denom)  # change to log()
    return p0Vect, p1Vect, pAbusive


#
# 朴素贝叶斯函数
# vec2Classify:分类向量
# p0Vec:0的概率
# p1Vec 1的概率
# pClass1: 在分类中1的概率
#
def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + log(pClass1)  # element-wise mult
    p0 = sum(vec2Classify * p0Vec) + log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else:
        return 0


def testingNB():
    # 切割后的文本与标签
    listOPosts, listClasses = loadDataSet()
    # 创建不重复词表
    myVocabList = createVocabList(listOPosts)
    trainMat = []
    # postinDoc是每一个词汇的数组
    for postinDoc in listOPosts:
        # append 中的内容是：输入的文档在词汇表中是否在文档中出现
        # 同时将向量添加到trainMat中，trainMat的数组中包含了
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
    # 分别得到0的概率 1的概率 分类中出现1的概率
    p0V, p1V, pAb = trainNB0(array(trainMat), array(listClasses))
    testEntry = ['love', 'my', 'dalmation']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry, 'classified as: ', classifyNB(thisDoc, p0V, p1V, pAb))


#
# 接受一个大字符串并将其解析为字符串列表。
# 该函数去掉少于两个字符的字符串，并将所有字符串转换为小写。
#

def textParse(bigString):  # input is big string, #output is word list
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]


def spamTest():
    docList = [];
    classList = [];
    fullText = []
    for i in range(1, 26):
        # 正常邮件
        print('111111111   %d ', i)
        wordList = textParse(open('email/spam/%d.txt' % i, 'r', encoding='utf-8').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1)
        # 垃圾邮件
        print('00000000   %d ', i)
        wordList = textParse(open('email/ham/%d.txt' % i, 'r', encoding='utf-8').read())
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    # 创建词汇表
    vocabList = createVocabList(docList)  # create vocabulary
    trainingSet = list(range(50));
    testSet = []  # create test set
    # 构建随机的训练集合
    for i in range(10):
        # 任意抽取出10分邮件，第i封，选一个随机数
        randIndex = int(random.uniform(0, len(trainingSet)))
        # 加入test的集合中
        testSet.append(trainingSet[randIndex])
        # 从训练的集合中移除
        del (trainingSet[randIndex])
    trainMat = [];
    trainClasses = []
    # 训练集合
    for docIndex in trainingSet:  # train the classifier (get probs) trainNB0
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V, p1V, pSpam = trainNB0(array(trainMat), array(trainClasses))
    errorCount = 0

    # 对测试集进行分类
    for docIndex in testSet:  # classify the remaining items
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        # 通过分类器得出的结果和判断的词汇表进行判断球的判断的错误率
        if classifyNB(array(wordVector), p0V, p1V, pSpam) != classList[docIndex]:
            errorCount += 1
            print("classification error", docList[docIndex])
    print('the error rate is: ', float(errorCount) / len(testSet))
    # return vocabList,fullText
