def solve(my_list):
    counter_dict = {}
    for ml in my_list:
        if ml in counter_dict:
            counter_dict[ml] += 1
        else:
            counter_dict[ml] = 1
        if counter_dict[ml] == 1:
            print("OK")
        else:
            print(f"{ml}{counter_dict[ml]-1}")

n = int(input())
my_list = []
for i in range(n):
    curr = input()
    my_list.append(curr)

solve(my_list)
