import re

s = 'Here are UPPERCASE and lowercase chars.'

d = {}

for char in set(s): #{H,e,r,a," ",U,P,E,...}
  index_record = []
  for match in re.finditer(char, s): # finditer回傳位置index
    print(match)
    print("--------------------------------------------")
    index_record.append(match.start()+1)

  d[char] = index_record

print(d)
