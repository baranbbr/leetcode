class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # pointer to put next non-val element
        for j in range(0, len(nums)):
            if nums[j] != val:
                # move current element to pointer to put next non-val
                nums[i] = nums[j]  # move current element to front of list
                i += 1  # move pointer along
        return i  # length of array without val
        # e.g. [3,2,2,3] becomes [2,2,2,3], k=2 first two elements are correct
