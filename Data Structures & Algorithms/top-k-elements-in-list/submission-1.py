class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            if num in result:
                result[num]+=1
            else:
                result[num] = 1
        sort = sorted(result, key=result.get, reverse=True)
        return sort[0:k]