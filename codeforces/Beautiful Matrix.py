def first_solution(m):
    return m

matrix = []
for i in range(0, 5):
    input_list = list(map(lambda x: int(x), input().split()))
    matrix.append(input_list)

print(first_solution(matrix))