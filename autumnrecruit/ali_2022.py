#算法：把所有的数字补成最大的值是基础次数，如果小于这个次数，就是当前的最大值。如果大于这个次数，就是添加后的最大值
import sys
l = list(map(int,sys.stdin.readline().strip().split()))
n,k= l[0],l[1]
#print(l)
a = list(map(int,sys.stdin.readline().strip().split()))
#print(a)
max_a = max(a)
count = 0
for i in a:
    count += max_a - i
#print(count)
if k <= count:
    print(max_a)
else:
    plus = ((k - count-1)//n)+1
    print(max_a+ plus)





import sys
l = list(map(int,sys.stdin.readline().strip().split()))
n,m= l[0],l[1]
# 算法：如果两边除了边界上，存在一条直线是都是1的，必不能聚集

zhaozhe= []
for i in range(n):
    tmp_l = []
    a= sys.stdin.readline()
    for i in a[:-1]:
        tmp_l.append(int(i))
    zhaozhe.append(tmp_l)
#print(zhaozhe)
k = int(sys.stdin.readline().strip())
arm= []
for i in range(k):
    arm.append(list(map(int,sys.stdin.readline().strip().split())))
#print(arm)
for i in range(1,n-1):
    count = 0
    for j in range(m):
        if zhaozhe[i][j] == 1:
            count += 1
    if count == m:
        print(-1)
        break
for i in range(1,m-1):
    count = 0
    for j in range(n):
        if zhaozhe[j][i] == 1:
            count += 1
    if count == n:
        print(-1)
        break

 