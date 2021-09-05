# -*- coding: utf-8 -*-
# @Time    : 2021/8/4 9:49 下午
# @Author  : Kai Zheng
# @FileName: kedaxunfei.py
# @Software: PyCharm
# @Email: 156252108@qq.com

'''
def find( a ):
    # write code here
    s = set(a)
    ss = [i for i in s]
    ss.sort()
    d= {}
    for i in ss:
        tmp = a.count(i)
        d[tmp] = i
    res = sorted(d.keys())
    return d[res[0]]
print(find([3,7,7,9,9]))
'''


'''
def NN_Box( a):
    # write code here
    nums = len(a) // 2
    # a.sort(lambda x | -x)
    a.sort()
    res = 0

    for i in range(len(a) - 1, len(a) - 1 - nums, -1):
        res += a[i]
    return res
print(NN_Box([1,2,3,4,5])) # 8

'''


'''
def ColorTheTree( connect, color):
    # write code here 最大连通的数量。
    return 15

# [[1,2],[1,3],[3,4],[3,5]],[0,1,1,0,0]  # 3
'''
