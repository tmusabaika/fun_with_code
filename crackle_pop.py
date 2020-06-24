'''
Write a program that prints out the numbers 1 to 100 (inclusive).
If the number is divisible by 3, print Crackle instead of the number. 
If it's divisible by 5, print Pop. 
If it's divisible by both 3 and 5, print CracklePop. 
You can use any language.
'''
def crackle_pop(num):
    if (num%3==0) & (num%5==0):
        return "CracklePop"
    elif num%3==0:
        return "Crackle"
    elif num%5==0:
        return "Pop"
    else:
        return num

for i in range (1,101):
    print(crackle_pop(i))

