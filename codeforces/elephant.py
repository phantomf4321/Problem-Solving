def solve(n):
    counter = 0
    while(n >= 5):
        n = n - 5
        counter = counter+1
    while(n >= 4):
        n = n - 4
        counter = counter+1
    while(n >= 3):
        n = n - 3
        counter = counter+1
    while(n >= 2):
        n = n - 2
        counter = counter+1
    while(n >= 1):
        n = n - 1
        counter = counter+1
        
    return counter
    
n = int(input())
print(solve(n))
    
