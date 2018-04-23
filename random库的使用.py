import random
random.seed(0)
random.random()      # 随机产生0到1的小数
random.seed(0)
random.random()

random.randint(1,10)    # 1到10的随机整数
random.randrange(1,100,3)    # 1到100以3为步长的随机整数
random.getrandbits(40)   # 产生一个40bits长的随机整数
random.uniform(1,10)    # 1到10的随机小数
random.choice([1,2,3,4])    # 从列表中随机取一个
s = [1,2,3,4]
random.shuffle(s)    # 打乱，随机排列
print(s)
