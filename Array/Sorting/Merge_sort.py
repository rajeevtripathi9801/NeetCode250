class Solution:
    def merge(self, nums, low, mid, high):
        left = low
        right = mid + 1

        temp = []
        while left<= mid and right <= high:
            if nums[left] < nums[right]:
                temp.append(nums[left])
                left += 1
            else:
                temp.append(nums[right])
                right += 1

        while left<= mid:
            temp.append(nums[left])
            left += 1

        while right<=high:
            temp.append(nums[right])
            right +=1

        for i in range(len(temp)):
            nums[low + i] = temp[i]

    def merge_sort(self, nums, low, high):
        if low == high:
            return
        mid = (low + high) // 2

        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid + 1, high)
        self.merge(nums, low, mid, high)

if __name__ == "__main__":
    obj = Solution()
    nums = [3, 1, 2, 4, 1, 5, 6, 4, 5]
    low = 0
    high = len(nums) - 1
    obj.merge_sort(nums, low, high)
    print(nums)