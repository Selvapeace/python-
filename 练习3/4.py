# 输出等边三角形
N = eval(input())
for i in range(1,N+1,2):
    a = '*' * i
    print('{}'.format(a).center(N,' '))

