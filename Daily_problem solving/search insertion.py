# first implementation using builtin function

def find_value(lista,target):
    if target in lista:
        return lista.index(target)
    else:
        lista.append(target)
        lista.sort()
        return lista.index(target)


def find_valu(lista,target):
    low, upper = 0, len(lista)# boundaries for creating binary search

    while low<= upper:
        mid = (low+upper)//2 # dividing the list in two halves
        if lista[mid] == target:
            return mid
        else:
            if lista[mid]> target:
                upper = mid-1
            else :
                low = mid+1
    return upper
trial = [7,9,10]
target = 9
print(find_value(trial, target))
print(find_value(trial,target))
    
