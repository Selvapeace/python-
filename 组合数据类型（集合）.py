# 组合数据类型：集合、序列（元组、列表）、字典

# 集合：多个元素的无序组合（不存在相同元素），集合元素不可更改
## 定义集合
A = {'python',123,('python',123)}    # 使用{}建立集合
B = set('pypy123')     # 把pypy123拆开分别作为集合的元素，重复的直接删除；创建空集只能用set()
C = {'python123','python123'}
## 集合的运算
A = {'p',123,('python',123)} 
A|B    # 并
A-B    # 差
A&B     #交
A^B    # 补(集合A和B中不相同的元素集合)
A <= B
A < B
A >= B          # 判断包含关系
A > B
A|=B    # 把A、B的并作为新的A，更新A
A-=B    # 差，更新A
A&=B     #交，更新A
A^=B    # 补，更新A
## 集合的处理方法
A.add('x')      # 如果'x'不在集合A中，加入
A.discard('x')     # 从A中移除'x'，若A中没有'x'，不报错
A.remove('p')       # 从A中移除'x'，若A中没有'x'，报错
A.clear()        # 移除A中所有元素
C.pop()          # 随机返回A中一个元素并删除这个元素，若A为空集，报错
A.copy()
len(A)
'X' in A
'X' not in A
set('x')    # 将其他类型转化为集合类型

# example 1
D = {'p','y','gggg'}
for item in D:
    print(item,end = '')      # 由于集合中元素是无序的，用for in循环每次取的元素顺序也不确定

print('\n')
# example 2
'''打印D中的元素，直到所有元素都打印完了，退出(报错时pass)'''
try:
    while True:
        print(D.pop(),end = '')
except:
    pass

'''
集合类型的应用场景：
1、包含关系的比较
2、数据去重（删除一组数据中重复的内容）(利用集合无重复元素的性质）example 3
'''
# example 3
ls = ['p','p','y','y',123]
s = set(ls)
ls = list(s)


