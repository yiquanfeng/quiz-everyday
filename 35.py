class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        first = 0
        last = len(nums)-1
        mid = int((last - first) / 2)
        ans = 0 
        while first <= last:
            if target > nums[mid]:
                first = mid+1
                ans = mid+1
            elif target < nums[mid]:
                last = mid-1
                ans = mid
            else:
                ans = mid
                break
            mid = int((last - first) / 2) + first
        return ans