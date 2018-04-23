# example 1
def fact(n):       # n为必选参数
    s = 1
    for i in range(1,n+1):
        s *= i
    return s

# example 2
def fact(n,m=1):       # m为可选参数，默认为1
    s = 1
    for i in range(1,n+1):
        s *= i
    s = s // m
    return s

# example 3
def fact(n,*b):       # *b表示可变参数，随意几个
    s = 1
    for i in range(1,n+1):
        s *= i
    for each in b:
        s *= each
    return s

# example 4
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    s = s // m
    return s,n,m
## 用元组返回多个值
def fact(n,m=1):
    s = 1
    for i in range(1,n+1):
        s *= i
    s = s // m
    a = s,n,m
    return a

# 全局变量和局部变量即使命名相同，也是不同的变量
# 在函数内部使用全局变量用global
n,s = 10,100
def fact(n):
    global s
    for i in range(1,n+1):
        s *= i
    return s
print(fact(n),s)

# 局部变量为组合数据类型且未创建时，等同于全局变量
# example 1
ls = ['f','F']
def func(a):
    ls.append(a)     # 在函数中ls未创建，因此就等同全局变量
    return
func('C')       # 全局变量被修改了
print(ls)       # 打印全局变量
# example 2
ls = ['f','F']
def func(a):
    ls = []         # 被创建了，ls是局部变量
    ls.append(a)
    return
func('C')       # 局部变量被修改了
print(ls)       # 打印全局变量


# lambda函数:一种匿名函数，返回结果是函数名，用于简洁地定义函数.谨慎使用
# example 1
f = lambda x , y : x + y
print(f(10,15))
# example 2
f = lambda : 'lambda函数'
print(f())
