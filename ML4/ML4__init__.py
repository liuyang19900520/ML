import ML4.bayes as bayes

# # 切割后的文本与标签
# listOPosts, listClasses = bayes.loadDataSet()
# #创建不重复词表
# myVocabList=bayes.createVocabList(listOPosts)
# print(myVocabList)
#
# trainMat = []
# # postinDoc是每一个词汇的数组
# for postinDoc in listOPosts:
#     #append 中的内容是：输入的文档在词汇表中是否在文档中出现
#     #同时将向量添加到trainMat中，trainMat的数组中包含了
#     trainMat.append(bayes.setOfWords2Vec(myVocabList, postinDoc))
#
# print(trainMat)
#
# p0V,p1V,pAb=bayes.trainNB0(trainMat,listClasses)
#
# print("p0V代表了这个词汇出现在正常语句中的频率")
# print(p0V)
# print("p1V代表了这个词汇出现在侮辱性语句中的频率")
# print(p1V)
# print(pAb)


# bayes.testingNB();
bayes.spamTest();