def solve(n, s):
    resault = 0
    for i in range(n-1):
        if s[i] == s[i+1]:
            resault = resault+1
            
    return resault
    
n = int(input())
s = input()
print(solve(n, s))
