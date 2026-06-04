class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}

        for i,n in enumerate(nums):
            indices[n] = i

        for i,n in enumerate(nums):
            dif = target - n
            
            if dif in indices and indices[dif] != i:
                return [i, indices[dif]]

            