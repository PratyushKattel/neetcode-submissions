class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = Counter(t)
        freq_s = Counter()
        char_t = set(t)
        l = 0
        r = 0
        min_len, min_str = math.inf, ""
        char_pos = []
        # possible_solution= []
        if len(s) < len(t):
            return ""
            
        while r < len(s):
            if s[r] in char_t:
                char_pos.append(r)
                freq_s[s[r]] += 1

            # check for match
            while all(freq_s.get(k, 0) >= freq_t.get(k, 0) for k in freq_t):
                l = char_pos.pop(0)
                if r - l + 1 < min_len:
                    min_len = r - l + 1
                    min_str = s[l : r + 1]
                    # possible_solution.append( (l,r, s[l:r+1]))

                freq_s[s[l]] -= 1
                l += 1

            r += 1
        return min_str
