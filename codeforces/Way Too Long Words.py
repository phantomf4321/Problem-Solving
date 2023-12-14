def first_solution(text):
    if(len(text) > 10):
        num = len(text) - 2
        num = str(num)
        result = text[0] + num + text[-1]
    else:
        result = text

    return result

print(first_solution("internationalization"))