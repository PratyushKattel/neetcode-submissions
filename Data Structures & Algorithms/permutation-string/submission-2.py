class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
         #window size  is equal to the len of the s1
        freq_s1 = Counter(s1)
        for i in range(len (s2)):
            s  = s2[i : i +len(s1)]
            freq_sub = Counter(s)
            if freq_sub == freq_s1:
                return True
        return False

        
                
        



                

