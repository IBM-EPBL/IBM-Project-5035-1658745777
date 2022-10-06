def fibonacci(n):
    a = 0
    b = 1
        
    print(a, end=" ")
    
    for x in range(1, n + 1):
        print(b, end=" ")
        next = a + b
        a = b
        b = next
        
while True:
    n = int(input("Enter N (Enter -1 to exit): "))
    
    if n < 0:
        break
    
    print(f"{n} fibonacci numbers are:", end=" ")
    fibonacci(n)
    
    print()
    
    