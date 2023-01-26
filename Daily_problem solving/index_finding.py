#Given a sorted array of distinct integers and a target value,
#return the index if the target is found. If not, return the index where
#it would be if it were inserted in order.

def findindex(listnum, number):
    if len(listnum) == 0:
        return 0
    elif listnum[0]> number:
        return 0
    elif listnum[len(listnum)-1] < number:
        return len(listnum)
    else:
        mid = int(len(listnum)/2)+1
        p1 = -1
        p2 = 1
        checker = True

        while checker:
            if listnum[mid-p1]>= number and listnum[mid+p2] <= number:
                return mid
            elif listnum[mid]> number:
                mid = mid +int(mid/2)+1
                print(mid)
            elif listnum[mid]< number:
                mid = mid-int(mid/2)+1
                print(mid)
            else:
                return 0


def split(listnumber):
    
    length = len(listnumber)
    
                  
num = 3
number = [ -1,1,2, 2.5, 3, 6,7,8]
print(findindex(number, num))


