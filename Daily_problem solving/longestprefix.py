
def longest_prefix(s):
    '''
    return the longest prefix between two words
    '''
    if len(s) == 1:
        return s[0]
    if len(s) == 0:
        return ""
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
            
            if len(s)> 2:
                next_pref = next_pref+longest_prefix(s[1:])
    
                return next_pref
            
            else:
                return  pref
                    
           
       
       
       
       
                            
            
strs = ["racogg", "rat", "rnime", "c", "v"]
print(longest_prefix(strs))
