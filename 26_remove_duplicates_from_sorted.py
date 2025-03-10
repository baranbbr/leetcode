class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0  # pointer to last unique element
        for j in range(1, len(nums)):  # start one ahead
            if (nums[j] != nums[idx]):  # ahead is different (higher) so change
                idx += 1  # move pointer ahead
                nums[idx] = nums[j]  # update current with new unique element
            # if nums[j] == nums[idx], duplicate element so skip, j increments
        return idx + 1  # return length of array with unique elements
