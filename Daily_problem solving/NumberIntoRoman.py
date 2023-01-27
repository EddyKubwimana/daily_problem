#change integer into roman numbers

def toRoman(number):
    result = ""
    rem = 0
    left = number
    position = 10
    while left > 0:
        rem = left % position
        left = left//position
        position = position*10
        if 
        
