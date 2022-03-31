"""
# 上一个程序，解决了计算慢的问题，但是具体的分割方式，还不清楚(只能知道，分成了2半，剩下的2半再怎么分，不知道！)。
# 所以，可以这样解决：
"""
from collections import defaultdict
prices=[1,5,8,9,10,17,17,20,24,30,33]
complete_price=defaultdict(int)
for i,p in enumerate(prices):complete_price[i+1]=p

soluion={}
cache={}

def r(n):
    if n in cache: return cache[n]
    candiates=[(complete_price[n],(n,0))]+[(r(i)+r(n-i),(i,n-i)) for i in range(1,n)]
    optimal_price,split=max(candiates)
    soluion[n]=split
    cache[n]=optimal_price
    return optimal_price

def parse_solution(n,cut_solution):
    left,right=cut_solution[n]
    if left==0 or right==0:return [left+right,]
    else:
        return parse_solution(left,cut_solution)+parse_solution(right,cut_solution)

if __name__=="__main__":
    print(r(19))
    print(parse_solution(19,soluion))

## 以上代码，是非常间经典的一个动态规划问题