from numpy import *

# 用法：zeros(shape, dtype=float, order='C')
# 返回：返回来一个给定形状和类型的用0填充的数组
# 参数：
# shape:形状
# dtype: 数据类型，可选参数，默认numpy.float64
# dtype类型：t, 位域, 如t4代表4位
# b, 布尔值，true or false
# i, 整数, 如i8(64位）
# u, 无符号整数，u8(64位）
# f, 浮点数，f8（64位）
# c, 浮点负数，
# o, 对象，
# s, a，字符串，s24
# u, unicode, u24
# order: 可选参数，c代表与c语言类似，行优先；F代表列优先

k = zeros((2, 3), dtype=[('x', 'i4'), ('y', 'i4'), ('z', 'i4')], order='C')
print(k)
# [[(0, 0, 0) (0, 0, 0) (0, 0, 0)]
# [(0, 0, 0) (0, 0, 0) (0, 0, 0)]]

# 把dtype这3个0一个truple，按照2行3列的方式补齐


str="liuyang1 liuyang2" \
    "liuyang3"
print(str.split('\t'))


list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
m = list[3]
print(m)
print("****************************************************")
print("****************************************************")
print("****************************************************")





print("11111111111111111111")
#[[0. 0. 0. 0.]]  1行4列
returnVect=zeros((1,4))
# 2行4列
#[[0. 0. 0.]
# [0. 0. 0.]]
returnVect=zeros((2,3))
print(returnVect)
