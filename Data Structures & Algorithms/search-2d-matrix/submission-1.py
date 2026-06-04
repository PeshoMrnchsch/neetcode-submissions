class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            left= 0
            right = len(row)-1
            if row[right] < target and row[left] > target:
                continue

            while left<=right:
                mid = (left + right) //2
                if row[mid] < target:
                    left = mid+1
                elif row[mid] > target:
                    right = mid-1
                else:
                    return True
        

        return False


                # while left <= right:
                #     if target < row[right]:
                #         right -= 1
                #     if target > row[left]:
                #             left += 1    
                #     if target == row[left] or target == row[right]:
                #         return True
                # return False
            