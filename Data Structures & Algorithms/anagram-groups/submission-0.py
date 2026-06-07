class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash_set = set()
        result = []
        hash_map = {}
        i=0
        # for i, word in enumerate(strs):
        #     hash_map[word] = i
        for word in strs:
            sort = ("".join(sorted(word)))
            if sort not in hash_map.keys():
                hash_map[sort] = i
                result.append([])
                result[i].append(word)
                i+=1
            else:
                index = hash_map[sort]
                result[index].append(word)
                
        return result