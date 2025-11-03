class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        all_list = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                all_list.append(matrix[i][j])
        
        start = 0
        end = m * n - 1
        mid = int((end - start)/2)
        while start <= end:
            if target < all_list[mid]:
                end = mid - 1
            elif target > all_list[mid]:
                start = mid + 1
            else:
                return True
            mid = start + int((end - start) / 2)
        return False        