# -*- coding: utf-8 -*-
# @Time    : 2021/8/30 8:25 下午
# @Author  : Kai Zheng
# @FileName: pdd_2022.py
# @Software: PyCharm
# @Email: 156252108@qq.com

import sys
n = int(sys.stdin.readline().strip())
for _ in range(n):
    n,m,k = list(map(int,sys.stdin.readline().strip().split(' ')))
    #print(n,m,k)
    ln=list(map(int,sys.stdin.readline().strip().split(' ')))
    lm=list(map(int,sys.stdin.readline().strip().split(' ')))
    count = 0
    res = []
    for i in range(n):
        res.append([])
        for j in range(m):
            if ln[i] >= lm[j]-k and ln[i] <= lm[j]+k:
                res[-1].append(lm[j])
            #count= max(count,len(tmp_n))
    #print(res)
    res = [i for i in res if i !=[]]
    #print(res)
    ret =0
    for i in res:
        ret=max(ret,len(i))
    print(ret)
# 1
# 3 4 1
# 5 2 3
# 1 2 9 7
# ans = 2



import sys
n = int(sys.stdin.readline().strip())
l = []
for i in range(n):
    l.append(sys.stdin.readline().strip())
#print(l)
def comp(a,b):
    na= len(a)
    nb= len(b)
    for i in range(na):
        if a[i] < b[i]
    pass
'''   
l = [1,3,2]
for i in range(n):
    for j in range(n-i):
        if l[j] > l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
print(l)
'''
for i in range(n):
    for j in range(n-i):
        if comp(l[j], l[j+1]):
            l[j],l[j+1] = l[j+1],l[j]
print(l)

# 2
# abcde
# abcdeaf
# ans:
    # abcdeaf
    # abcde
# ？？？abcdeaf的字典序小于abcde的所有形态？？题目记得不太清了。


import sys

n = int(sys.stdin.readline().strip())
# print(n)
l = []
for i in range(n):
    l.append(int(sys.stdin.readline().strip()))


# print(l)
# 算法
def rec(n):
    pass


for num in l:
    print(30)



# 1
# 10
# ans = 3

import sys

num = int(sys.stdin.readline().strip())
for i in range(num):
    n = int(sys.stdin.readline().strip())
    l = list(map(int, sys.stdin.readline().strip().split(' ')))
    # print(l)
    min_l = min(l)
    count = 0
    l_1 = [i - min_l for i in l]
    for i in l_1:
        if i != 0:
            count += 1
    print(min_l + count)

# 1
# 5
# 1 2 1 3 2
# ans= 4
