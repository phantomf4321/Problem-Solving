def first_solution(scores, rank):
    counter = 0
    scores.sort(reverse=True)
    rank = scores[rank - 1]
    for i in scores:
        if(i >= rank):
            counter += 1

    return counter

num = int(input())
rank = int(input())
input_list = list(map(lambda x: int(x), input().split()))

print(first_solution(input_list, rank))
