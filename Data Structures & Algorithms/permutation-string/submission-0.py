class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
       

        if len(s1) > len(s2):
            return False

        window_size = len(s1)
        dic1 = {}
        dic2 = {}
        for char in s1:
            dic1[char] = dic1.get(char, 0) + 1

        l = 0
        for r in range(len(s2)):
            
            dic2[s2[r]] = dic2.get(s2[r], 0) + 1
            
            if r-l + 1 > window_size:
                dic2[s2[l]] -= 1
                if dic2[s2[l]] == 0:
                    del dic2[s2[l]]
                l += 1
            
            if r - l + 1 == window_size:
                if dic1==dic2:
                    return True

            
            
        return False
        # window = s2[l:window_size]
        # for char in window:
        #     # If char isn't in dict, default to 0 and add 1
        #     dic2[char] = dic2.get(char, 0) + 1
        # if dic1 == dic2:
        #     return True
        
        # abde ab