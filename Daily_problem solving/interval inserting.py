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

def insert(inter, new):
        result = []
        for i in range(len(inter)):
            if new[1] < inter[i][0]:
                result.append(new)
                return result + inter[i:]
            elif new[0] > inter[i][1]:
                result.append(inter[i])
            else:
                new = [min(new[0], inter[i][0]), max(new[1], inter[i][1])]
        result.append(new)
        return result
        
            
                
        


intervals = [[1,2], [3,4], [5,6],[7,9]]
newInterval = [4,5]
print(insert(intervals, newInterval))
