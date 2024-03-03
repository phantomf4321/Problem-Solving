def first_solution(my_string):
    unique_words = set([*my_string])
    if(len(unique_words)%2 == 0):
        return("CHAT WITH HER!")
    else:
        return("IGNORE HIM!")

my_string = "xiaodao"
print(first_solution(my_string))