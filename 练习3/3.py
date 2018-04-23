# 好好学习时每天比前一天提高千分之N，不学习时下降千分之N
N = eval(input())
up = pow(1.0 + N/1000,365)
down = pow(1.0 - N/1000,365)
sub = int(up/down)
print('{:.2f},{:.2f},{}'.format(up,down,sub))
