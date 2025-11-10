class Solution:
    def search(self, nums: List[int], target: int) -> int:
        length = len(nums)
        start = 0
        end = length - 1
        is_left = target > nums[end]
        ans = -1
        while start <= end:
            mid = (end + start) // 2
            if is_left:
                if nums[mid] > nums[length-1]:
                    if nums[mid] > target:
                        end = mid - 1
                    elif nums[mid] < target:
                        start = mid + 1
                    else:
                        ans = mid
                        break
                else:
                    end = mid - 1
            else:
                if nums[mid] > nums[length-1]:
                    start = mid + 1
                else:
                    if nums[mid] > target:
                        end = mid - 1
                    elif nums[mid] < target:
                        start = mid + 1
                    else:
                        ans = mid
                        break
        return ans