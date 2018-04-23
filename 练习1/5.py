curr = input()
num = float(curr[3:-1] + curr[-1])
if curr[0:3] in ['RMB','rmb']:
    USD = num / 6.78
    print("USD{:.2f}".format(USD))
elif curr[0:3] in ['USD','usd']:
    RMB = num * 6.78
    print("RMB{:.2f}".format(RMB))
else:
    print('wrong')
