class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        chars_s1 = Counter (s1)

        flag = False
        lens1= len(s1)
        l = r = 0
        for char in s2 :
            if char not in chars_s1:
                l += 1 
                r += 1
                continue
                print ( "not in ", l , r)

            else :
                chars_s1 = Counter (s1)
                while ( r - l + 1   <= lens1):
                    print ( "while outer :  ", s2[l] ,s2[r])
                    if s2 [r] in chars_s1 and chars_s1[s2[r]] > 0:
                        print ( "while r in s2 :  ", s2[l] ,s2[r])
                        chars_s1[s2[r]] -= 1
                        print(chars_s1)
                        r+=1
                        if sum(chars_s1.values()) == 0:
                            return True
                    else: 
                        print ( "l == r")
                        l = r
                        break
        return False



                

