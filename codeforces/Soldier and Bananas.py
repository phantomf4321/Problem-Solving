def first_solution(k, n, w):
    counter = 1
    saver = 0
    while counter <= w:
        saver = saver + counter*k
        counter = counter + 1
    
    res = saver - n
    if res < 0:
        return 0
    else:
        return res
    
k, n, w = map(int, input().split())
print(first_solution(k, n, w))
