m = input()
if 'm' in m:
    num = m[0:-1]
    inch = eval(num) * 39.37
    print('{:.3f}in'.format(inch))
elif 'in' in m:
    num = m[0:-2]
    mi = eval(num) / 39.37
    print('{:.3f}m'.format(mi))
else:
    print('wrong format')

