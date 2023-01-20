def roman(s):
        '''
        Take a string as Roman number and returns a inter
        '''

        number = {"I":1, "V":5, "X":10, "L":50,"C":100,"D":500, "M":1000}
        sub = {"IV":-2, "IX":-2, "XL":-20, "XC":-20, "CD":-200, "CM" :-200}
        total = 0

        for i in s:
            #time complexity O(n)
            #space complexity O(1)
            total += number[i]

        for i in range(0, len(s)):
            #time complexity O(n)
            #space complexity O(1)
            print(s[i:i+2])
            try:
                if sub[s[i:i+2]]:
                    total+= sub[s[i:i+2]]
            except:
                pass

       
        print(total)
roman("XLXIV")

