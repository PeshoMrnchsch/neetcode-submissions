class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = []
        for el in nums:
            if el in res:
                return True
            else:
                res.append(el)

        return False