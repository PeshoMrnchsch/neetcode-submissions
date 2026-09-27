class Solution:
   def characterReplacement(self, s: str, k: int) -> int:
        # [L.....R]
        # window size - max_frequency <= k
        # so k can replace of the remaining k symbols


        biggest_window = 0
        l = 0
        
        count = {}
        for r in range(len(s)):
            
            count[s[r]] = count.get(s[r], 0) + 1
            freq = max(count.values())

            while r - l + 1 - freq > k:
                    count[s[l]] = count.get(s[l], 0) -1
                    l +=1

            if r-l+1 > biggest_window:
                biggest_window = r-l+1
        


        return biggest_window
