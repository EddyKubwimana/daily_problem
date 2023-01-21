import heapq

number = [1,4,9,7,0]
number = [-ele for ele in number]
heapq.heapify(number)
for i in range(3):
    value = -heapq.heappop(number)
print(value)
    
