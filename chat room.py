def can_say_hello(s):
    hello = "hello"
    i = 0

    for char in s:
        if char == hello[i]:
            i += 1
            if i == len(hello):
                return "YES"

    return "NO"

s = input().strip()
print(can_say_hello(s))
