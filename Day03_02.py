nums = [2,7,11,15]
target = 9

list = []
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            list.append(i)
            list.append(j)
print(list)

#解法二   可實際寫出來好理解
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        num1 = nums[i]
        num2 = target - num1
        if num2 in d:
            return [d[num2], i ]
        d[num1] = i 

print(twoSum([3,2,4], 6 ))

