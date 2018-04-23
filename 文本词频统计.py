# 文本词频统计

# 英文文本
def getText():
    text = open("E:\外文电子书\Harry Potter\Harry Potter and the Sorcerer's Stone.txt",'r').read()
    text = text.lower()                    # 全部小写
    for ch in '|"#%()*+,-./:;<=>?@[\\]^_{|}~':
        text = text.replace(ch,' ')               # 把特殊字符换成空格
    return text

harry = getText()
words = harry.split()
counts = {}
for word in words:
    counts[word] = counts.get(word,0) + 1    # counts.get(word,0)返回键word对应的值，如果不存在键word，在字典中加入word键并返回0
                                             # 也就是，当某word第一次被索引时，counts = 1；不是第一次索引，则返回原有的counts 再加上1
items = list(counts.items())
items.sort(key = lambda x:x[1],reverse = True)    # key = lambda x:x[1] 意为按照列表中每个元素按照元素在1位置的值排序
for i in range(20):
    word,count = items[i]        # 词频最高的10个词
    print('{0:<10}{1:>5}'.format(word,count))     # 共10位，左对齐；共5位，右对齐


# 中文文本
import jieba
txt = open("F:\小说\金庸全集\射雕英雄传\HERO27.TXT",'r',encoding = 'utf-8').read()
cha = jieba.lcut(txt)
excludes = {'帮主','丐帮','群丐','自己','二人','兄弟','长老','铁掌','甚么','之中','只是','一个','说道','我们','帮众','众丐','却是','武功'}
counts1 = {}
for each in cha:
    if len(each) == 1:
        continue               # 把长度为1的字符都删掉（包括你我他、标点符号等）
    elif each == '郭靖' or each == '黄蓉':
        r_each = '郭靖黄蓉夫妇'                  # 把郭靖和黄蓉合并
    else:
        r_each = each
    counts1[r_each] = counts1.get(r_each,0) + 1
for each in excludes:
    del counts1[each]
items1 = list(counts1.items())
items1.sort(key = lambda x:x[1],reverse = True)
for i in range(7):
    cha,count1 = items1[i]
    print('{0:<10}{1:>5}'.format(cha,count1))

