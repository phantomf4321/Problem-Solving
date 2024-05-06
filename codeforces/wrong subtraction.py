def solve(n, s):
    number = n
    counter = s
    while counter > 0:
        counter = counter-1
        if(number %10 == 0):
            number = number/10
        else:
            number = number-1
    
    return number
    
n, s = input().split()

print(int(solve(int(n), int(s))))
