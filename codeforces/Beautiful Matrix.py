def first_solution(m):
    d = dict( (j,(x, y)) for x, i in enumerate(m) for y, j in enumerate(i) )
    index1 = abs(2 - d[1][0])
    index2 = abs(2 - d[1][1])
    result = index1 + index2
    return result

matrix = []
for i in range(0, 5):
    input_list = list(map(lambda x: int(x), input().split()))
    matrix.append(input_list)

print(first_solution(matrix))