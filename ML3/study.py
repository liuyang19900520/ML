import  operator

# sorted(iterable, *, key=None, reverse=False)¶
#   Return a new sorted list from the items in iterable.
# 简言之这是一个排序函数，本函数是实现对可迭代对象iterable进行排序。
# 可选参数key是比较键的函数；reverse是表示是否反向排列对象里的项，是布尔值。

print(sorted([5, 2, 3, 1, 4]))
print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}, reverse = True))
print(sorted("This is a test string from Andrew".split(), key=str.lower))
student_tuples = [
        ('john', 'A', 75),
        ('jane', 'B', 62),
        ('dave', 'B', 100),
]
print(sorted(student_tuples, key=lambda student: student[2]))   # 按年龄排序


# result：
#[1, 2, 3, 4, 5]
#[5, 4, 3, 2, 1]
#['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']
#[('jane', 'B', 62), ('john', 'A', 75), ('dave', 'B', 100)]




# operator.itemgetter(1)
#   operator模块提供的itemgetter函数用于获取对象的哪些维的数据，
#   参数为一些序号（即需要获取的数据在对象中的序号）
#   operator.itemgetter函数获取的不是值，而是定义了一个函数，通过该函数作用到对象上才能获取值

a=[1,2,3]
b=operator.itemgetter(1) #定义函数b，获取对象的第一个域的值
print(b(a))
b=operator.itemgetter(1,0)#定义函数b，获取对象的第1个域和第0个域的值
print(b(a))

# result:
# 2
# (2, 1)