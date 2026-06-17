class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        nums_sorted = list(sorted(nums_set))
        count = 1
        max_count = 1
        if len(nums) == 0:
            return 0
        for num in nums_sorted:
            if num+1 in nums_set:
                count+=1
                if count > max_count:
                    max_count = count
            else: count = 1
        return max_count