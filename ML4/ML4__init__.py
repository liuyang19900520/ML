import ML4.bayes as bayes

listOPosts, listClasses = bayes.loadDataSet()
myVocabList=bayes.createVocabList(listOPosts)
print(myVocabList)
r1=bayes.setOfWords2Vec(myVocabList,listOPosts[0])

print(r1)

