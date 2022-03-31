"""
# 上一版程序之所以运行的慢，原因是：很多值会被重复运算
# 为了解决重复运算，可以做一个非常简单的方法 加一个cache
"""
from collections import defaultdict
prices=[1,5,8,9,10,17,17,20,24,30,33]
complete_price=defaultdict(int)
for i,p in enumerate(prices):complete_price[i+1]=p

soluion={}

cache={} # cache

def r(n):
    if n in cache: return cache[n]
    candiates=[(complete_price[n],(n,0))]+[(r(i)+r(n-i),(i,n-i)) for i in range(1,n)]
    optimal_price,split=max(candiates)
    soluion[n]=split
    cache[n]=optimal_price
    return optimal_price

if __name__=="__main__":
    print(r(133))

# cache 是很重要的一种思想
# 贝尔曼发现，在数学中，有一类问题叫做： “”子问题的重复“”。
# 贝尔曼提出的解决办法就是：使用一张表格，不断地写表，查表操作，这种方法叫做 dynamic（不断地，动态的） programming （写表读表）。
# 从而可以大幅度提升计算性能。

# 动态规划中的表，为什么如此重要？
# 其实，问题都可以不使用动态规划，也可以解决，前提是有无限长的表（然而并没有）。所以，动态规划很重要。