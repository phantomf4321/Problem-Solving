def solve(my_string):
    danger = 1
    for i in range(0, len(my_string)-1):
        if my_string[i] == my_string[i+1]:
            danger = danger+1
            if danger >= 7:
                return True
        else:
            danger = 1
        
    return False
    
my_string = input()
if solve(my_string):
    print("YES")
else:
    print("NO")
            
