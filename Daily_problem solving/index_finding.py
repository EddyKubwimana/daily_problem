#Given a sorted array of distinct integers and a target value,
#return the index if the target is found. If not, return the index where
#it would be if it were inserted in order.

def findindex(listnumber, number):
    mid = len(listnumber)/2+1
    checker = True
    while checker:
        if listnumber[mid]== 5:
            return mid
        elif listnumber[mid]>5:
            mid = (len(listnumber[mid:])+mid)
        else:
            pass
        
            
        
