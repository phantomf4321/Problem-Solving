def low_up(s):
    lower=0
    upper=0
    for i in s:
          if(i.islower()):
                lower+=1
          else:
                upper+=1
                
    if lower>upper:
        return -1
    if upper>lower:
        return 1
    if upper==lower:
        return 0
        
def solve(s):
    lp = low_up(s)
    if lp == -1 or lp == 0:
        return s.lower()
    if lp == 1:
        return s.upper()
        
s = input()
print(solve(s))
