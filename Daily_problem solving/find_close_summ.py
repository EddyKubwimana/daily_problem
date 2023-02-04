def closer(nums, target):
    summ = []
    x = True
    counter = 0
    while x is True:
            
        for i in range (1,len(nums)):
            if i<=len(nums)+2:
                solution = nums[counter]+nums[i]+nums[i+1]
                summ.append(solution)
            else:
                break
        if counter <= len(nums)+2:
            break
        else:
            counter+= 1
    summ.append(target)
    summ.sort()
    index = summ.index(target)

    difference1 = abs(target-summ[index-1])
    difference2 = abs(target-summ[index+1])
    if difference1> difference2:
        return summ[index-1]
    else:
        return summ[index+1]
    
        
