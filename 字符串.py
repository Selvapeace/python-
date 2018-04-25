# 为什么字符串有3种表示方式
print('''hahahaha
你是不是傻''')
'''nihao'ya'hahaha''hhhhh''en'''

# 字符串索引  <字符串>[M]

# 字符串切片
"abcde"[:3]         # 即[0:3]
"abcedfghijk"[1:8:2]   # 以2为步长，从第一个到第8个元素，进行切片
"abcedfghijk"[::-1]    # 以-1为步长，从第1个到最后一个元素，进行切片；即倒序

# 转义符 \  ： \之后的字符表示字符的本意
"hhhhh\"nihao\""
\b     # 光标向前回退一个位置
\n     # 换行
\r     # 光标回到当前行的行首


## 字符串的操作符
x + y    # 连接两个字符串
n * x    # 复制n次字符串x
x in s   # 如果x是s的子串，返回True

## 字符串处理函数
len(x)   # 输出字符串长度
str(x)   # 将任意类型变为字符串,与eval()做相反工作
hex(x)    # 转化为十六进制
oct(x)   # 转化为八进制
chr(x)   # x为Unicode编码，返回其对应字符（pathon用的是Unicode，Unicode涵盖世界上所有语言，每个字符对应一个代码）
ord(x)   # 与chr()相反

for i in range (12):
    print(chr(9800 + i),end= " ")

## 字符串处理方法   <a>.<b>
str.lower()     # 把字符串的字符全部小写/大写
str.upper()
str.split(sep = None)  # 返回一个列表，由str根据sep被分割的部分组成'A,B,C'.split(',')
str.count(sub)     # 返回子串sub在字符串中出现的次数
str.replace(old,new)
str.center(width[,fillchar])   # 字符串str根据宽度width居中，并在剩余部分用fillchar填充
str.strip(chars)    # 'python ='.strip(" np")则将'python ='中的空格、n、p去掉
str.join(iter)   # 在iter变量除最后元素外每个元素后加一个str  ','.join('12345')

## 字符串类型的格式化   .format()
# {} :槽，占用
"{1}你好{2}傻比{0}".format('!','hhh','em')    # 数字0,1,2对应顺序
# 花括号内用冒号引导格式配置
# 填充、对齐、宽度
"{0:=^20}".format('PYTHON')     # =是填充符号，^是居中对齐（右对齐是>)，20是输出宽度
# 千位分割、精度、类型
"{0:,.2f}".format(12345.6789)    # ，是添加千位分割符，.2f表示保留2位小数（四舍五入）
"{0:b},{0:c},{0:d},{0:o},{0:x},{0:X}".format(425)    # 依次：二进制、Unicode、十进制、八进制、十六进制、大写十六进制
"{0:e},{0:E},{0:f},{0:%}".format(3.14)   # 依次：科学计数法、科学计数法大写、普通方法、百分数

