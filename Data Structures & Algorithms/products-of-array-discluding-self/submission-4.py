class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        hash_map = {}
        result = []
        total_prod = 1
        zero = False
        zero_index_set = set()
        for i, num in enumerate(nums):
            hash_map[i] = num
            if num != 0:
                total_prod *= num
            else:
                zero = True
                zero_index_set.add(i)
        for i in range(len(nums)):
            if not zero:
                result.append(total_prod//hash_map[i])
            else:
                if i in zero_index_set and len(zero_index_set) == 1:
                    result.append(total_prod)
                else:
                    result.append(0)
        return result