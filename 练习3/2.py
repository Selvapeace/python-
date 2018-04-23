a = eval(input())
b = abs(a)
if a == b:
    print(b,b+10,abs(b-10),b*10,sep = ' ')
else:
    print(b,-b-10,-abs(b-10),-b*10,sep = ' ')
