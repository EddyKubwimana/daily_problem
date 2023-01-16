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
    stack = []
    up = None
    low = None
    for i in range(len(inter)):
        if inter[i][0] < new[0]and inter[i][1] < new[0]:
            stack.append(inter[i])

        elif inter[i][0] < new[0] and inter[i][1] > new[0]:
             low = inter[i][0]

        elif inter[i-1][1] < new[0] and inter[i][0]> new[0]:
            low = new[0]
        elif inter[i][0] < new[1] and inter[i+1][1] > new[1]:
            
            up = inter[i][1]
            stack.append([low,up])
            if i+1< len(inter)-1:
                stack.extend(inter[i+1:])
                return stack
           

        elif inter[i][0] < new[1] and inter[i+1][1] > new[1]:
            up = inter[i+1][1]
            
            stack.append([low,up])
            if i+1< len(inter)-1:
                stack.extend(inter[i+2:])
                return stack
        

            
            
        
        
    return stack

intervals = [[1,3],[6,9]]
new = [2,5]
#intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
#new = [4,8]

print(insert_interval(intervals, new))
             
        
             

