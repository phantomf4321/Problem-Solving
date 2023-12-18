def first_solution(text):
    first = text[0].capitalize()
    second = text[1:]
    result = first + second

    return result

text = input()
print(first_solution(text))
