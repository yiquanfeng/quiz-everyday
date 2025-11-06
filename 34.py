class Solution:
    
    def binarySearch(self, nums: List[int], target: int, equal: bool) -> int:
        left = 0
        right = len(nums) - 1
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target or (nums[mid] <= target and equal):
                left = mid + 1
                ans = mid
            else:
                right = mid - 1
                ans = mid - 1
        return ans
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = self.binarySearch(nums,target, False)+1
        end = self.binarySearch(nums,target, True)
        print(start)
        print(end)
        if len(nums) == 1 and nums[0] == target:
            return[0, 0]
        if start <= end:
            return [start, end]
        else:
            return [-1, -1]
            