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
