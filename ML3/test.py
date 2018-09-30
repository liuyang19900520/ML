from ML3.trees import *

myDat, labels = createDataSet()
print(myDat)

axis = 0
value = 0

featList = [example[0] for example in myDat]

uniqueVals = set(featList)

retDataSet = [];
for featVec in myDat:
    # 当需要返回的特征值与fetVec（fet就是一条数据的3个特征值），fetVet[i]就是获取一个特征
    if featVec[axis] == value:
        print('featVec=====', featVec)
        # 取出除去这个特征之外的数据
        reducedFeatVec = featVec[:axis]
        print('reducedFeatVec==(featVec[:axis])=====extend before', reducedFeatVec)
        # 如果使用a.append(n)，[1,2,3,[4,5,6,]];而a.extend(b)==[1,2,3,4,5,6]
        print('(featVec[axis + 1:])', (featVec[axis + 1:]))
        reducedFeatVec.extend(featVec[axis + 1:])
        print('reducedFeatVec=====extend after', reducedFeatVec)
        retDataSet.append(reducedFeatVec)
