
''' This program finds a closest sum of three number to a given target
@author : Eddy Kubwimana
@email: eddy.kubwimana@ashesi.edu.gh
@created: 04/4/2023
@version : 1:0:1
'''

# function definiton for the whole process
def closer(nums, target):
    '''
    Takes a list of numbers and a target
    returns the close sum of triplet
    '''
    summ = []
    counter = 0
    while True: 
        for i in range (1,len(nums)):
            if i<=len(nums)+2:
                solution = nums[counter]+nums[i]+nums[i+1]
                summ.append(solution)
            else:
                break
        if counter <= len(nums)+2:
             counter+= 1
            
        else:
            break
    summ.append(target)
    summ.sort()
    index = summ.index(target)

    difference1 = abs(target-summ[index-1])
    difference2 = abs(target-summ[index+1])
    if difference1<difference2:
        return summ[index-1]
    else:
        return summ[index+1]

  
#Testing case for the function

# test1

    
