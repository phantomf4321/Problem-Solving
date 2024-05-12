def is_lucky(n):
    return n == 4 or n == 7

def is_nearly_lucky(number):
    # Convert the number to a string to count lucky digits
    number_str = str(number)
    lucky_count = 0
    
    # Count the lucky digits
    for digit in number_str:
        if is_lucky(int(digit)):
            lucky_count += 1
    
    # Check if the count of lucky digits is a lucky number
    return is_lucky(lucky_count)

# Input number
n = int(input(""))

# Output
if(is_nearly_lucky(n)):
    print("YES")
else:
    print("NO")
