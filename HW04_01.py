def add1(n):
    return n+1 


def isPrime(n):
    # return True or False
    if n==1 or n==2:
        return True

    for i in range(2,n): # 從2~n-1都除一次
        if n % i == 0:
            return False
    
    return True

def f(L, F):
    response = []

    for element in L:
        response.append(F(element))   # F(element) = add1(element)

    return response

L = [1,2,3,4,5,6]
F = add1

print(f(L, F))   # [2,3,4,5,6,7]

L = [2,3,4,5,6,7]
F = isPrime
print(f(L,F))     # [True, True, False, True, False, True]
