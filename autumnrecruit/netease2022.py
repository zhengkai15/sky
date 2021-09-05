# -*- coding: utf-8 -*-
# @Time    : 2021/8/15 9:24 下午
# @Author  : Kai Zheng
# @FileName: netease2022.py
# @Software: PyCharm
# @Email: 156252108@qq.com

# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param arr float浮点型一维数组 非空无序数组
# @return float浮点型
# 算法：排序，判断奇数还是偶数，奇数就是中间那个，偶数中间两个的和的一半，空，1，2？？
class Solution:
    def median(self, arr):
        # write code here
        nums = len(arr)
        arr.sort()
        # print(arr)
        if nums % 2 == 0:
            index = nums // 2
            return (arr[index - 1] + arr[index]) / 2
        else:
            index = nums // 2
            return arr[index]


import sys
name = list(sys.stdin.readline().strip().split(" "))
#print(name)
s = sys.stdin.readline().strip()
#print(s)
count = 0
for i in name:
    count += s.count(i)

print(count)

import sys
import math
def softmax(x):
    tmp = []
    for i in x:
        tmp.append(math.exp(i))
    s  = sum(tmp)
    y =[i/s for i in tmp ]
    return y
#print('softmax',softmax([1,2,3]))

l = list(map(int,sys.stdin.readline().strip().split(" ")))
N, K = l[0], l[1]
#logits = [[0 for i in range(K)] for j in range(N)]
logits = []
for _ in range(N):
    tmp = list(map(float,sys.stdin.readline().strip().split(" ")))
    logits.append(tmp)
#print(logits)
for _ in range(N):
    tmp1 =logits[_][:]
    tmp = softmax(tmp1)
    index = tmp.index(max(tmp))
    res = str(tmp[index]).split(".")
    ret = res[0] +'.'+ res[1][:6]
    print(index,ret)

import sys
l = list(map(int,sys.stdin.readline().strip().split(" ")))
#print(l) 算法基础 是len(l) 个，然后判断每个的旁边是不是有比他大的数字。
# 如果第一个大于第二个；如果倒数第一个大于倒数第二个；
def paper(l):
    count = len(l)
    if count < 2:
        return 1
    if l[0]>l[1]:
        count += 1
    if l[-1] > l[-2]:
        count += 1

    for i in range(1,len(l)-1): #从第二个开始判断到倒数第二个
        if l[i] > l[i-1]:
            count +=1
        if l[i] > l[i-1]:
            count +=1
    return count
print(paper(l))

