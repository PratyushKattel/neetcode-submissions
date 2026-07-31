class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1

        while (1):
            curr_k = (min_k + max_k) // 2
            hour = 0 

            if max_k == min_k:
                return max_k

            for bananas in piles:
                    hour += math.ceil(bananas / curr_k)

            if hour <= h:
                max_k = curr_k
            else:
                min_k = curr_k + 1

        