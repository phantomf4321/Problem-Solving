def first_solution(m):
    d = dict( (j,(x, y)) for x, i in enumerate(m) for y, j in enumerate(i) )
    return d[1]

matrix = []
for i in range(0, 5):
    input_list = list(map(lambda x: int(x), input().split()))
    matrix.append(input_list)

print(first_solution(matrix))