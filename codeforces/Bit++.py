def first_solution(xlist):
    counter = 0
    for i in xlist:
        if "+" in i:
            counter += 1
        if "-" in i:
            counter -= 1
    return(counter)

n = int(input())
list = []
for i in range(0, n):
    cur = input()
    list.append(cur)

print(first_solution(list))

