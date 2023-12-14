def first_solution(my_list):
    result = 0
    for i in my_list:
        if(i.count(1) > 1):
            result += 1
    return result


num = int(input())
my_list = []

for i in range(0, num):
    input_list = list(map(lambda x: int(x), input().split()))
    my_list.append(input_list)

print(first_solution(my_list))