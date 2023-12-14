def first_solution(text):
    if(len(text) > 10):
        num = len(text) - 2
        num = str(num)
        result = text[0] + num + text[-1]
    else:
        result = text

    return result

inputs = []
num = int(input())
for i in range (0, num):
    cur = input()
    inputs.append(cur)

for i in inputs:
    print(first_solution(i))