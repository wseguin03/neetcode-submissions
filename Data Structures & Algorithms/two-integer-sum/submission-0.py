class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i in range(len(nums)):
            if(target - nums[i]) in temp.keys():
                return [temp[target - nums[i]], i]
            else:
                temp[nums[i]] = i