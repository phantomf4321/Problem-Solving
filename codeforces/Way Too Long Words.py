def first_solution(text):
    if(len(text) > 10):
        result = text[0] + text[-1]
    else:
        result = text

    return result

print(first_solution("internationalization"))