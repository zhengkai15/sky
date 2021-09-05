# -*- coding: utf-8 -*-
# @Time    : 2021/8/31 8:57 下午
# @Author  : Kai Zheng
# @FileName: tecent2021-2.py
# @Software: PyCharm
# @Email: 156252108@qq.com


# 腾讯
'''
# 1
n,m =3,3
l1=[2,3,4]
l2=[4,9,16]
from  itertools import permutations
for c in l2:
    for i in permutations(l1,2):
        if c == i[0]**i[1]:
            print(i[0],i[1])
            break
    else:
        print(-1,-1)
'''

# 2
# 算法 ，k,b 都是正数，计算交叉点，分两段积分，保留6位小数。
# y= x**k ; y = -x + b  -> x**k = -x + b 解方程？？x 为正；

# 4  定义四个指针 S T A R,每个都比前面的index大两个。 直到找齐所有
n=8
s = "SSTTAARR"
count = 0
S,T,A,R = 0,0,0,0
while S <= n-6:
    if s[S] == "S":
        T = S + 2
        while T <= n - 4:
            if s[T] == "T":
                A = T + 2
                while A <= n-2:
                    if s[A] == "A":
                        R = A + 2
                        while R <= n-1:
                            if s[R] == "R":
                                count += 1
                                print(S,T,A,R )
                            R += 1
                    A += 1
            T += 1
    S += 1
print(count)
