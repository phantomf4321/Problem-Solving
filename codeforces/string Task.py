def remove_vowels(s):
    vowels = ["a", "e", "o", "u", "i", "y"]
    if s in vowels:
        return ""
    else:
        return s
        
def solve(string):
    result = ""
    for s in string:
        cur = ""
        cur = s.lower()
        cur = remove_vowels(cur)
        result = result + cur
    return result
def printer(string):
    result = solve(string)
    cur = ""
    for s in result:
        cur = cur + "." + s
    return cur

string = input()
print(printer(string))
