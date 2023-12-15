def first_solution(xlist):
    counter = 0
    for i in xlist:
        if(i[0] == "+" and i[1] == "+"):
            counter += 1
        if (i[0] == "-" and i[1] == "-"):
            counter -= 1
    return counter

n = int(input())
list = list(map(lambda x: int(x), input().split()))


