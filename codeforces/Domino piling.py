def first_solution(m, n):
   return (m * n) // 2

M, N = map(int, input().split())

max_dominoes = (M * N) // 2

print(max_dominoes)