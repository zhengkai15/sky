# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 5:01 下午
# @Author  : Kai Zheng
# @FileName: tianyiyun2022.py
# @Software: PyCharm
# @Email: 156252108@qq.com
'''
l= [(1,3),(5,7),(2,6)]
l.sort()
# print(l)
N=len(l)
# print(l[1][0])
# res = 0
# for i in range(N-1):
#     if l[i+1][0]>=l[i][1]:
#         res += l[i][1] -l[i][0]
#     else:
#         res += l[i+1][0] - l[i][0]
# print(res)
# store 存放所有，统计数字为1的个数。
store= []
for i in l:
    for j in range(i[0],i[1]):
        store.append((j,j+1))
store.sort()
count = 0
for i in store:
    if store.count(i) == 1:
        count += 1
print(count)

'''
def findMax(numOfItems,total_money,items,vlaues):  #i是多少行 j是多少列
    dp = [[0]*(total_money+1) for i in range(numOfItems+1)]
    #print(dp)
    for i in range(1,numOfItems + 1):
        for j in range(1,total_money + 1):
            if j < items[i-1]:              #只能放上一个物品，因为放不进比他大一个型号的
                dp[i][j] = dp[i - 1][j]
            else:                           #当可以放进时，就比较放进去的收益大还是不放的收益大
                dp[i][j] = max(dp[i - 1][j],dp[i - 1][j - items[i-1]] + vlaues[i-1])
    return dp[i][j]
total_money = 20 #背包容量1000
hotspot_val = [4,8,6,22,2]#[6, 10,3, 4, 5, 8]
unit_price = [4,7,5,10,1]#[200,600,100,180,300,450]
res=findMax(len(unit_price),total_money,unit_price,hotspot_val)
print(res)
