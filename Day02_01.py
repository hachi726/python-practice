import re

input1 = "This company is not poor at all."
start_index = input1.find("not")
end_index = input1.find("at all")

r = input1.replace(input1[start_index:end_index+6], "good")
print(r)

print(re.sub("not.*at all", "good" , input1))   # not 後面的 . 代表 任何字元  * 代表字元的個數
