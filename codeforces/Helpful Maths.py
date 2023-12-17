def first_solution(text):
    numbers = [int(num) for num in text.split('+')]  # Split the expression and convert numbers to integers
    sorted_expression = '+'.join(str(num) for num in sorted(numbers))  # Sort the numbers and join them back with '+'

    return sorted_expression