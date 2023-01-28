#Given a sorted array of distinct integers and a target value,
#return the index if the target is found. If not, return the index where
#it would be if it were inserted in order.

def findindex(listnum, number):
    if len(listnum) == 0:
            return 0
    if len(listnum)==1 and listnum[0]< number:
            return 1

    if len(listnum)==1 and listnum[0]> number:
            return 0
    keeper = 0
    mid = int(len(listnum)/2 +1 )
    lower, upper = listnum[:mid], listnum[mid:]

    checker = True
    while checker:
      if lower[len(lower)-1]> number and upper[0]<= number:
          return mid
      elif lower[len(lower)-1] == number:
          return len(lower)-1
      elif upper[len(upper)-1] == number:
          return len(upper)-1
      elif lower[0] == number:
          return 0
      elif upper[0] == number:
          return 0
     
      else:
        
        if lower[len(lower)-1] < number:
            keeper += mid
            mid = int(len(lower)/2 +1 )
            lower,upper = upper[:mid], upper[mid:]
            
            
        if lower[len(lower)-1] > number:
             keeper += mid
             mid = int(len(upper)/2 +1 )
             lower,upper = upper[:mid], upper[mid:]

        
    
                  
num = 1
number = [ -1,1,2, 2.5, 3, 6,7,8]
print(findindex(number, num))


