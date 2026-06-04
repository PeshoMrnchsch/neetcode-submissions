class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()
        for el in nums:
            if el in res:
                return True
            else:
                res.add(el)

        return False