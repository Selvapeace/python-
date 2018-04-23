# 组合数据类型：集合、序列（元组、列表）、字典

# 字典：通过键值对对数据索引扩展，字典是键值对的集合，键值对之间无序
dic = {'name':'Jiang','age':23,'location':'China'}
dic['name'] = 'jiangjiang'
dic['sex'] = 'female'

dic1 = {}       # 空集的定义只能用set()；从而{}可以生成空字典
type(dic1)

del dic['age']
'location' in dic
dic.keys()    # 返回所有键的信息
dic.values()    # 返回所有值的信息
dic.items()     # 返回所有键值对的信息

dic.get('location','no location')   # 返回locaiton对应的值,如果dic中没有键location，则返回'no location'
dic.pop('location','no location')   # ....同时删除location对应的值，如果....
dic.popitem()    # 随机取出键值对，以元组形式返回
dic.clear()     # 删除所有键值对
len(dic)

'''
字典的应用场景：
对映射的表达，即表达键值对数据进而进行操作
'''
