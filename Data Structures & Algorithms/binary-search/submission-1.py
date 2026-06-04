class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right :
            mid = (left + right) // 2
            cur = nums[mid]
            if target == cur:
                return mid
            elif target < cur:
                right = mid - 1
            elif target > cur:
                left = mid + 1
        return -1

