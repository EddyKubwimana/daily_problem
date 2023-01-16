# PROBlEM

#You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent
#the start and the end of the ith interval and intervals is sorted in ascending order by starti.
#You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

#Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
#does not have any overlapping intervals (merge overlapping intervals if necessary).

#case 1 : Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]

#Case 2 :Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

def insert_interval(inter, new):
    low = []
    high = []
    upper = len(inter)-1
    lower = 0
    low_b = None
    check_l = True
    check_r = True
    while lower <= upper:
        check_l = True
        check_r = True

        if inter[lower][1] < new[0]:
            low.append(inter[lower])
            print(low)
            lower+= 1
            check_l = False
        if inter[upper][0] > new[1]:
            high.append(inter[upper])
            print(high)
            upper-= 1
            check_r = False

        if inter[lower][0]< new[0] and inter[lower][1]> new[0]:
            low_b = [inter[lower][0]]
            lower+= 1
            check_l = False

        if inter[upper][0]<=new[1] and inter[upper][1]> new[1]:
            low_b.append(inter[upper][1])
            upper-= 1
            check_r = False

        if check_r == True and check_l == True:
            upper-= 1
            lower+=1
            
        
    low.append(low_b)
    low.extend(high[:])
    return low

#intervals = [[1,3],[6,9]]
#new = [2,5]
intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
new = [4,8]

print(insert_interval(intervals, new))
             
        
             

