from numpy import *

print(tile([1, 2], (3, 2)))

print("====================================")
group = array([[1, 2], [4, 5]])
print(group)
print(group.sum(axis=1))
#  [[1 2]
#  [4 5]]
# 0将数组的列相加[5 7]，
# 1将数组的行相加[3 9]

print("====================================")
group = array([[1, 2], [3, 4], [5, 6]])
print(group)
print(group.sum(axis=0))
#  [[1 2 ]
#  [3 4 ]
#  [5 6]]
# 0将数组的列相加[9，12]，
# 1将数组的行相加[3，7，11]
print("====================================")
A = array([[1,1],[2,2]])
B=array([[1,1],[2,2]])
print(A)
print(B)
print("====================================")
print(A*B)

print(4**0.5)

