#1 method

def valid(s):
        if len(s)== 1:
            return False
        para = {")":"(", "}":"{", "]":"["}
        stack = []
        for i in s:
            if i in para and len(stack)>=1:
                if stack[len(stack)-1] == para[i] :
                   stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        print(stack)
        if len(stack) == 0:
            return True
        else:
            return False


#2 nd method

def valid_par(s):
    para = {")":1,"(":-1, "}":2,"{":2, "]":3,"[":3}
    summation = ""
    for i in s:
        summation+= str(para[i])
    if summation == summation[::-1]:
        return True
    else:
        return False
    

s = "[([])]"
print(valid(s))
print(valid_par(s))
