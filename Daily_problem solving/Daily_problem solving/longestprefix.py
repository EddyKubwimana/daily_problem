
def log(n):
    pref = ""
    if len(n) == 0:
        return ""
    if len(n) == 1:
        return n[0]
    for i in range(1,len(n)):
        n[i] = longest_prefix(n[i-1],n[i])
    return n[i]
          
def longest_prefix(a,b):
            '''
            return the longest prefix between two words
            '''
            if len(a)== 0 or len(b) == 0:
                return ""
            elif a[0] != b[0]:
                return ""
            elif len(a)== 1 or len(b) == 1:
                if a[0] == b[0]:
                    return a[0]
            elif len(a)== 0 or len(b) == 0:
                return ""
            else:
                    pref = a[0]
                    pref = pref+longest_prefix(a[1:],b[1:])
                    return pref     

# second approach:

def longest_pref(strs):
     pref = ""
     for new in zip(*strs):
         if len(set(new)) == 1:
             pref += new[0]
         else:
             return pref
     return pref

# third approach alternative
def long(strs):
        pref = strs[0]
        for i in strs:
            while not i.startswith(pref):
                pref = pref[:-1]
        return pref
                                                 
strs = ["eddy", "eddy", "edmond", "e"]
#print(longest_pref(strs))
#print(long(strs))
print(log(strs))
#print(longest_prefix(strs))
