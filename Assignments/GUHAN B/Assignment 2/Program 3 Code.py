import math

def isPrime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    
    return True

while(True):
    n = int(input("Enter N (Enter -1 to exit): "))
    
    if n <= 0:
        break
    
    print(f"Prime numbers till {n}: ", end=" ")
    
    for i in range(n + 1):
        if isPrime(i):
            print(i, end=" ")
    
    print()
