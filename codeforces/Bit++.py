def first_solution(xlist):
    counter = 0
    for i in xlist:
        if(i[0] == "X"):
            print("hi")
            counter += 1
        if (i[1] == "X"):
            print("ih")
            counter -= 1

    return(counter)

n = int(input())
list = list(map(lambda x: str(x), input().split()))
print(first_solution(list))

