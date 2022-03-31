"""
cutting problem
"""
from collections import defaultdict
# 从容器中导入字典的子类，它调用一个工厂函数,来提供缺少的值，从而不会报错
# 如果使用普通的字典，查找不存在的键值时，就会报错

prices=[1,5,8,9,10,17,17,20,24,30,33] # 分别对应1-11米的木材价格，假设超过11米的，太长不收

complete_price=defaultdict(int)
# 这个工厂函数,可以是list、set、str等等,作用是当key不存在时，返回的是工厂函数的默认值.
# 比如,list对应[]，str对应的是空字符串，set对应set( )，int对应 0

for i,p in enumerate(prices):complete_price[i+1]=p
# print(complete_price[9]) # 9这个长度的木材，不切割，可以卖到多少钱？
# print(complete_price[30]) # 有了defaultdict函数，在调用一个不存在的键，时，就不会报错，而是返回一个0（表示只值0元）***

# def r(n):
#     candiates=[complete_price[n]]# 完全不进行切割，是多少钱？
#     for i in range(1,n):
#         left=i
#         right=n-i
#         total_price = r(left) + r(right) #  巧妙的 ***递归思想 ***
#         candiates.append(total_price)
#     return max(candiates)

# def r(n): # 完全等同于上面的代码
#     return max([complete_price[n]]+[r(i)+r(n-i) for i in range(1,n)])


soluion={}
def r(n): # 再加分割步骤
    ## 大家会发现，这个程序运运行很慢，是由于时间复杂度比较高
    # time complexity= 2*（n-1)*2*(n-2)*...=2^n * n!  (怎么算的？)
    candiates=[(complete_price[n],(n,0))]+[(r(i)+r(n-i),(i,n-i)) for i in range(1,n)]
    # (n,0)表示完全部分割，直接出售
    # (i,n-i)表示，分割成（i和n-i）的长度
    optimal_price,split=max(candiates)
    # list01 = [(19, (10, 1)), (12, (2, 3)), (49, (5, 8))]
    # print(max(list01))  #最大值结果为：(49, (5, 8))

    soluion[n]=split
    return optimal_price

if __name__=="__main__":
# “__main__” 始终指当前执行模块的名称（包含后缀.py）
# “__name__”,每个py文件都包含__name__变量，该模块被直接执行的时候，__name__等于文件名（包含后缀.py）
# 也就是说，”if __name__=="__main__":“以下的所有代码，都只有单独运行该py文件时，才会被执行
    print(r(6))
    print(soluion[6])