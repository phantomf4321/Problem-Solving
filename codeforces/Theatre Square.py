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

print(first_solution(6, 6, 4))