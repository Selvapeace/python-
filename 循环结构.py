# 遍历循环

## 计数循环
for i in range(1,10,2):
    print(i)
    
## 字符串遍历循环
for c in 'python123':
    print(c,end = ',')
    
## 列表遍历循环
for item in [123,'py',456]:
    print(item)
    
## 文件遍历循环(略）
## 只要in后面是多个元素的对象，for in 都可以实现遍历循环



# 无限循环
a = 2
while a > 0:
    print(a)
    a -= 1



# 循环控制保留字
## break /continue 都可以和for /while 一起用
for c in 'python':
    if c == 't':
        continue              # 跳出该次循环，做下一次循环
    print(c,end = '')
    
print('\n')

for c in 'python':
    if c == 't':
        break              # 跳出整个循环
    print(c,end = '')

print('\n')

s = 'PYTHON'
while s != '':
    for c in s:
        print(c,end ='')
    s = s[:-1]

print('\n')

s = 'PYTHON'
while s != '':
    for c in s:
        if c == 'T':
            break
        print(c,end ='')
    s = s[:-1]


# 循环的高级用法
## else语句作为正常完成循环（没遇到break)的奖励
for c in 'python':
    if c == 't':
        continue
    print(c,end = '')
else:
    print("正常退出")

for c in 'python':
    if c == 't':
        break
    print(c,end = '')
else:
    print("正常退出")
