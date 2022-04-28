# # 方法一
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic1.update(dic2)
dic1.update(dic3)
print(dic1)

# # 方法二 (python 3.9版本才可以)
dic4 = dic1 | dic2 | dic3
print(dic4)

# 方法三
def Merge(dic1, dic2, dic3): 
    res = {**dic1, **dic2, **dic3} 
    return res 

dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
dic4 = Merge(dic1, dic2, dic3) 
print(dic4)

d1 = {'name': 'Alex', 'age': 25} 
d2 = {'name': 'Alex', 'city': 'New York'} 
merged_dict = {**d1, **d2} 
print(merged_dict) # {'name': 'Alex', 'age': 25, 'city': 'New York'}
