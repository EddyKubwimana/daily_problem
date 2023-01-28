def number(number):
    if len(number)>= 0 and len(number)<=0:
        return None
    else:
        sub_number =[]
        for n in range(1,len(number)):
            for i in range(1, len(number)):
                try:
                   if not ([number[n-1],number[i], number[i+1]]) in sub_number:
                      if i>n:
                      
                          sub_number.append([number[n-1],number[i], number[i+1]])
                except :
                    pass
        triplet = [] 
        for sub in sub_number:
            if sub[0]**2+ sub[1]**2 == sub[2]**2:
                triplet.append(sub)
        return triplet
            
numb =[1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17]
print(number(numb))
            
