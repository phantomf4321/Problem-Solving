def first_solution(xlist):
    for i in xlist:
        counter = 0
        if(i[0] == "+" and i[1] == "+"):
            counter += 1
        if (i[0] == "-" and i[1] == "-"):
            counter -= 1
        print(counter)

n = int(input())
list = list(map(lambda x: int(x), input().split()))

for i in range(0, n):
    print(first_solution(list))

