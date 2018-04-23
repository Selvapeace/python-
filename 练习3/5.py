# 凯撒密码加密：将原文字母替换为该字母后面第3个字母（26个字母循环）
sec = input()
h = len(sec)
for i in range(h):
    if sec[i] != ' ':
        if sec[i] in ['x','y','z']:
            a = chr(ord(sec[i]) + 3 -26)
            print('{}'.format(a),end = '')
        else:
            a = chr(ord(sec[i]) + 3)
            print('{}'.format(a),end = '')
    else:
        print(" ",end = '')
