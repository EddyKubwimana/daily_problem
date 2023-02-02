#reverse integer
def reverse(x):

    if x< 0:
        sign = False
    else:
        sign = False

    temp = 0
    while x != 0:
        temp = temp*10+ x%10
        x = x//10
    return temp

        
number = 123789


print(reverse(number))
print("question", number)


