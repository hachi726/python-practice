a = input()
b = input()
int_a = int(a)
int_b = int(b)
if int_a > int_b :
    int_a, int_b = (int_b, int_a)   # 變數互換的寫法
else:
    int_a , int_b = int_a, int_b

def is_self_dividing(n:int):
    q = str(n)
    for w in list(q) :   # 把輸入的 int 轉成 str ，再利用for 迴圈後再轉成 int 去嘗試是否可以自除
        ww = int(w)
        if ww == 0:
            return False
        elif n % ww != 0:
            return False
    return True

self_dividing_numbers = []
for ab in range(int_a , int_b +1 ):
    if is_self_dividing(ab):
        self_dividing_numbers.append(ab)

print(self_dividing_numbers)

max_distance = -1 
max_distance_index= -1

for idx in range(1, len(self_dividing_numbers)): #[11,12,15]
    distance = self_dividing_numbers[idx] - self_dividing_numbers[idx-1]
    if distance > max_distance:
        max_distance = distance
        max_distance_index = idx

print(self_dividing_numbers[max_distance_index-1], self_dividing_numbers[max_distance_index])
