class Solution:
    def isHappy(self, n: int) -> bool:
        seen_squares = set ()
        curr = n
        while ( True ):
            num = 0 
            while (curr):
                remainder = curr % 10
                curr  = curr // 10
                num += remainder ** 2
            if num in seen_squares :
                return False
            if num == 1:
                return True
            seen_squares.add(num)
            curr = num