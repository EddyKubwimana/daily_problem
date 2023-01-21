def find(numbers,k_th):
    '''
    return a nth number in an array
    '''
    if len(numbers)>= k_th:
        numbers = sorted(numbers)
        return numbers[len(numbers)-k_th]
    else:
        return "the K-th number does not exist"
        
    
number = [10,20,28,78,90,2]
print(find(number,2))
                
    
