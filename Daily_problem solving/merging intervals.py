#Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

#Example 1:

#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
#Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

def merge(intervals):
        i = 1
        x = True
        while x:
            x = False
            for n in range(1,len(intervals)):
                if intervals[n-1][0] > intervals[n][0]:
                    x = True
                    intervals[n-1], intervals[n] = intervals[n], intervals[n-1]
        interval = intervals[:]
        print(interval)
        while i < len(interval):
            if interval[i-1][1]< interval[i][0]:
                i+= 1
            else:

               low =interval.pop(i-1)
               
               high = interval.pop(i-1)
               print(low)
               print(high)
               new = [min(low[0], high[0]), max(low[1], high[1])]
               interval.insert(i-1, new)

    
        return interval
                
                
                
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

print("[[1,3],[2,6],[8,10],[7,12],[13,16],[15,18]]")
print("The solution")
print(merge(intervals))


            
