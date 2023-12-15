def first_solution(xlist):
    counter = 0
    for i in xlist:
        if(i[1] == "+" and i[2] == "+"):
            print("hi")
            counter += 1
        if (i[0] == "-" and i[1] == "-"):
            print("ih")
            counter -= 1
    return(counter)

n = int(input())
list = list(map(lambda x: str(x), input().split()))
print(first_solution(list))

