def first_solution(m, n):
   return (m * n) // 2

M, N = map(int, input().split())

max_dominoes = first_solution(M, N)

print(max_dominoes)