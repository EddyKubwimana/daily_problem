#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

#Example 1:

#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def merge(inter):
        new = []
        result = []
        for i in  range (1,len(inter)):
            if inter[i-1][1] > inter[i][0]:
                new.append(inter[i-1])
                print(new)
        for i in new:
        
                for t in range(len(inter)):
                    if i[1] < inter[t][0]:
                        result.append(i)
                        return result + inter[t:]
                    elif i[0] > inter[t][1]:
                        result.append(inter[t])
                    else:
                        new = [min(i[0], inter[t][0]), max(i[1], inter[t][1])]
                result.append(i)
        return result
intervals = [[1,3],[2,6],[8,10],[15,18]]

print(merge(intervals))


            
