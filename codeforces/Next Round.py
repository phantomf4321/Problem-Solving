def first_solution(scores, rank):
    counter = 0
    scores.sort(reverse=True)
    return scores

print(first_solution([5,7,9,7,7,10,8], 1))
