start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("\nOdd Numbers in given range: ", end=" ")

while start <= end:
    if start % 2 == 1:
        print(start, end=" ")
    
    start += 1