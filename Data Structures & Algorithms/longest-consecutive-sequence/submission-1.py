class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        seen = set(nums)

        longest = 1

        for x in seen:
            if x-1 in seen:
                continue
            # start sequence

            count = 1
            n = 1
            while x + n in seen:
                count +=1
                n+=1
            if count > longest:
                longest = count

        return longest