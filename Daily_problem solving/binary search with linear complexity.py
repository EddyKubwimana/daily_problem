import time
start= time.time()
number = [23, 87, 98, 0, 45, 78, 34, 21, 74, 23, 3,7, 534, 86, 9, 1, 31,66, 7474, 8686, 858467, 74464, 46474774, 95757484, 646484, 4474, 467,874,846,8354,846,857,536,858,68, 874, 6484,65656,4344,5454,43,854,8464,84648,25, 60, 92, 53]
#find 53
#using algorithm of complixity O(n):
for item in number:
    if item == 53:
        print ( "53 found")
end = time.time()
duration = end-start
print(duration)
