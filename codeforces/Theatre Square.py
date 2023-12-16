def round(a):
    b = int(a)
    if (a == b):
        return a
    else:
        return b+1

def first_solution(m, n, a):
    var1 = round(m/a)
    var2 = round(n/a)
    return var1 * var2

n = int(input())
m = int(input())
a = int(input())
print(first_solution(m, n, a))