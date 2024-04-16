def solution(a, b):
    counter = 0
    while(a<=b):
        counter = counter + 1
        a = a*3
        b = b*2
    
    return counter
    
a, b = map(int, input().split())
print(solution(a, b))
