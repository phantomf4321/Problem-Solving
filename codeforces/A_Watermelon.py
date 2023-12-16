def first_solution(a):
    b = 0
    c = 0
    confirm = 0
    for i in range(1, a):
        c = i
        b = a - i
        if (b % 2 == 0 and c % 2 == 0):
            print("YES")
            confirm = 1
            break
    if (confirm == 0):
        print("NO")


def second_solution(a):
    if(a%2 == 0 and a!=2):
        print("YES")
    else:
        print("NO")

x = int(input())
first_solution(x)