my_string = "asdfds"
unique_words = set([*my_string])
print(len(unique_words))
def first_solution(my_string):
    unique_words = set([*my_string])
    if(len(unique_words)%2 == 0):
        return("CHAT WITH HER!")
    else:
        return("IGNORE HIM!")