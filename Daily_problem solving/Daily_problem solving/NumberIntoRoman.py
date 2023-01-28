#change integer into roman numbers

def toRoman(number):
    romanmap= {0:"",1: "I",2: "II",3: "III", 4:"IV" , 5 :"V",
               6:"VI", 7:"VII", 8: "VIII", 9: "IX", 10: "X",
               50 :"L", 90: "XC",100:"C", 500: "D", 1000: "M", 900: "CM"}
    rem = 0
    left = number
    position = 10
    result = ""
    mag = 1
    while left > 0:
        rem = left % position
        left = left//position
        if rem*mag in romanmap:
           result = romanmap[mag*rem]+result
        else:
            result = romanmap[rem]+romanmap[mag]+result
        mag = mag*10
    return result
        

def sum_numbers(listn):
    summ = 0
    for i in listn:
        summ+=i
    return summ

number = 58
var = toRoman(number)
print(var)
#print(number, sum_numbers(var))

print("MCMXCIV")
        
        
