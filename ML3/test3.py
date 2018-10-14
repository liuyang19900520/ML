from ML3.trees import *
from ML3.treePoltter import *

myDat, labels = createDataSet()
print("labels===", labels)

myTree = retrieveTree(0)
print("myTree===", myTree)

print("result===", classify(myTree, labels, [1, 0]))

'''
labels=== ['no surfacing', 'flippers']
myTree=== {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}}
result=== no
'''