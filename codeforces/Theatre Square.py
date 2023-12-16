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

input_list = list(map(lambda x: int(x), input().split()))

print(first_solution(input_list[0], input_list[1], input_list[2]))