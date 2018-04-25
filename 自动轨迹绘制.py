import turtle as t
t.title('自动轨迹绘制')
t.setup(800,600,0,0)
t.pencolor('red')
t.pensize(5)

datals = []
f = open('C:/Users/Administrator/Desktop/f.txt')
for line in f:
    line = line.replace('\n','')
    datals.append(list(map(eval,line.split(','))))
f.close()
'''上述代码对文件进行逐行读入，去掉读入行的换行符；
line.split(',')返回一个列表，map表示用eval函数处理该列表中的每个元素，
并将最终结果设为列表格式'''
for i in range(len(datals)):
    t.pencolor(datals[i][3],datals[i][4],datals[i][5])
    t.fd(datals[i][0])
    if datals[i][1]:
        t.right(datals[i][2])
    else:
        t.left(datals[i][2])

# 自动化思维：数据和功能分离
# 接口化设计：格式化接口设计

    
