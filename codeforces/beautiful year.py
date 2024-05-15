def dis(string):
    arr = []
    for s in string:
        if s in arr:
            return True
        else:
            arr.append(s)
    return False
    
def solve(n):
    saver = n + 1
    while(dis(str(saver))):
        saver = saver+1
    
    return saver
    
n = int(input())
print(solve(n))
