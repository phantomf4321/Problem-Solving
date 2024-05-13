def solve(s):
    d = s.count("D")
    a = s.count("A")
    if a > d:
        return "Anton"
    if a < d:
        return "Danik"
    if a == d:
        return "Friendship"
        
n = int(input())
s = input()
print(solve(s))
