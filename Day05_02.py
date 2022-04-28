'''
1F: 1 -> 一種走法
2F: 1+1, 2 ->兩種走法
3F: 1F+2, 2F+1 -> (1)+2, (1+1)+1, (2)+1 -> 三種走法
4F: 2F+2, 3F+1 -> [(1+1)+2, (2)+2,] [(1+2)+1, (1+1+1)+1, (2+1)+1] -> 五種走法
nF: (n-2)F+2, (n-1)F+1 -> #(n-2)F + #(n-1)F
'''

def climb(n):
    if n == 1 :
      return 1
    elif n == 2 :
      return 2 
    steps = [0]*(n) # 紀錄爬到每一樓的總走法
    # print(steps)
    steps[0] = 1 
    steps[1] = 2 
    for i in range(2,n):
      steps[i] = steps[i-1] + steps[i-2]
    return steps[n-1]

print(climb(3))


# def climbStairs(n: int) -> int:
#   W = [0, 1, 2]
#   for i in range(3, n):
#     W[i] = W[i - 2] + W[i - 1]
#   return W[n]

# def climbStairs(n: int) -> int:
#     W = [0, 1, 2]
#     if len(W) < n:
#         W[n] = climbStairs(n - 2) + climbStairs(n - 1);
#     return W[n];
