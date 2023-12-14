def first_solution(scores, rank):
    counter = 0
    scores.sort(reverse=True)
    rank = scores[rank - 1]
    for i in scores:
        if(i >= rank):
            counter += 1

    return counter

print(first_solution([5,7,9,7,7,10,8], 1))
