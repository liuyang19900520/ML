from numpy import *

randMat = mat(random.rand(4,4))
print(randMat)

invRandMat = randMat.I
print(invRandMat)

myEye = randMat*invRandMat
print(myEye)


print("==================================")
print(myEye - eye(4))