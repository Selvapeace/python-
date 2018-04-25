# t 以文本形式打开文件，注意路径用反斜杠/
tf = open('C:/Users/Administrator/Desktop/f.txt','rt')   # 默认是rt
print(tf.readline())
tf.close     # 文件关闭

bf = open('C:/Users/Administrator/Desktop/f.txt','rb')    # b 以二进制形式打开文件
print(bf.readline())
bf.close

'''
r表示只读模式，若文件不存在，返回FileNotFoundError；
w表示覆盖写模式，文件不存在则创建，存在则完全覆盖；
x表示创建写模式，文件不存在则创建，存在则返回FileExistsError;
a表示追加写模式，文件不存在则创建，存在则在文件后追加内容；
+与r/w/x/a一同使用，在原功能基础上增加读写功能。
'''

tf.read(3)   # 默认读取tf的全部内容，设参数为3表示读取前3个字节
tf.readline()   # 读取一行
tf.readlines(1)   # 读取所有行，设参数为1表示读取前1行
# 被读取过的内容就没了

# 文件的全文本操作
## 遍历全文本 method 1 （一次性读入）
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
txt = fo.read()
fo.close()
## 遍历全文本 method 2 （逐步读入）
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
txt = fo.read(2)
while txt != '':
    txt = fo.read()    # 每次读2个字节，直到读完
fo.close()

# 文件的逐行操作
## 逐行遍历文件 method 1 （一次性读入）
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
for line in fo.readlines():
    print(line)
fo.close()
## 逐行遍历文件 method2 （逐步读入）
fname = input('请输入要打开的文件名称：')
fo = open(fname,'r')
for line in fo:
    print(line)
fo.close()


# 数据的文件写入
f.write('哈哈哈哈哈')     # 向打开的文件f中写入 一个 字符串或字节流
f.writelines(['h','f'])   # 写入一个元素全为字符串的列表（列表中的字符串不分行）
f.seek(offset)    # 改变当前文件操作指针的位置：offset = 0(文件开头),1(当前位置),2(文件结尾)

fo = open('f.txt','w+')
ls = ['h','i','j']
fo.writelines(ls)
fo.seek(0)       # 必须有这一步，将指针放到文件开头，否则没内容可打印
for line in fo:
    print(line)
fo.close()


# 一维数据的存储和处理
ls = [1,2,3]    # 列表类型可以表示有序一维数据
a = {1,2,3}     # 集合可以表示无序一维数据
## 读取数据
txt = open(fname).read
ls = txt.split()    # 从空格分隔文件中读取数据；若文件的分隔符是其他字符，修改括号里的内容即可
f.close
## 向文件写入数据
ls = [1,2,3]
f = open(fname,'w')
f.write('$'.join(ls))     # 用$分隔的方式写入；其他符号亦可
f.close()


# 二维数据的表示（二维列表）
[[1,2,3],
[4,5,6]]     # 按行存储（即内部每个小列表代表一行）
# 二维数据的处理
## 从csv中读取数据
fo = open(fname)
ls = []
for line in fo:
	line = line.replace('\n','')
	ls.append(line.split(','))
fo.close()
## 把二维列表写入csv
ls = [[],[],[]]
f = open(fname,'w')
for item in ls:
	f.write(','.join(item) + '\n')    # 按行写入，一行的每个元素之间逗号分隔，行尾回车
f.close()
## 遍历二维数据元素
ls = [[],[],[]]
for row in ls:
	for colum in row:
		print(ls[row][colum])     # 可以看成“剥玉米”
		
