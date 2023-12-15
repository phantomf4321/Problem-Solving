def first_solution(xlist):
    counter = 0
    for i in xlist:
        if(i[1] == "+" and i[2] == "+"):
            counter += 1
        if (i[0] == "-" and i[1] == "-"):
            counter -= 1
    return(counter)

n = int(input())
list = []
for i in range(0, n):
    cur = input()
    list.append(cur)

print(first_solution(list))

