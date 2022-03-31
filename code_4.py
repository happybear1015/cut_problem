from collections import defaultdict

### python中，有很多问题，已经帮我们解决一些问题（）帮我们把很久没有使用过的数进行删除，从而将cache 保持在一个固定的范围内，例如：
# functools 中有一个 lru_cache (least recent used)
from functools import lru_cache

prices=[1,5,8,9,10,17,17,20,24,30,33]
complete_price=defaultdict(int)
for i,p in enumerate(prices):complete_price[i+1]=p

soluion={}
cache={} # 当 n 非常大的时候，这个cache也会非常大。此时，就需要让cashe 保留最重要的东西

@lru_cache(maxsize=2**10) # 是一个装饰器，设定它可以存储这么多个值
def r(n):
    # @lru_cache：当调用这个函数，如果这个函数的参数曾经被计算过，则直接返回这个值，如果没有被计算过，则计算一个，然后记录下来
    # if n in cache: return cache[n]
    candiates=[(complete_price[n],(n,0))]+[(r(i)+r(n-i),(i,n-i)) for i in range(1,n)]
    optimal_price,split=max(candiates)
    soluion[n]=split
    # cache[n]=optimal_price
    return optimal_price

def parse_solution(n,cut_solution):
    left,right=cut_solution[n]
    if left==0 or right==0:return [left+right,]
    else:
        return parse_solution(left,cut_solution)+parse_solution(right,cut_solution)

if __name__=="__main__":
    print(r(19))
    print(parse_solution(19,soluion))

# 当一个程序很慢的时候，可以想起来，用lru_cache来进行优化处理

# 所有的动态规划问题，都包含以下问题：
# 1. 可以被分解成子问题
# 2. 存在子问题的重复
# 3. 需要解析solution