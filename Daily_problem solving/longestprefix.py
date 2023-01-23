def longestPrefix(lis):
   pref = ""
   bound = 1
   if len(lis) == 0:
       return pref
   if len(lis) == 1:
       return lis[0]
   while bound < len(lis)-1:
       pref = lis[bound]
       for i in range(len(pref)):
           if len(pref) != 0 and len(lis[bound])!=0:
              if pref[i]==lis[bound+1][i]:
                  pass

def longest_prefix(s):
    '''
    return the longest prefix between two words
    '''
    a = s[0]
    b = s[1]
    if a[0] != b[0]:
        return ""
    elif len(a)== 1 or len(b) == 1:
        if a[0] == b[0]:
            return a[0]
    elif len(a)== 0 or len(b) == 0:
        return ""
    else:
            pref = s[0][0]
            s[0] = a[1:]
            s[1] = b[1:]
            pref = pref+longest_prefix(s)
            
            return pref
                
           
       
       
       
       
                            
            
strs = ["racogg","racecar"]
print(longest_prefix(strs))
