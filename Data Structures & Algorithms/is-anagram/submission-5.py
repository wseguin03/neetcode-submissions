class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ana_dict1 = {}
        ana_dict2 = {}
        for char in s:
            if char in ana_dict1:
                 ana_dict1[char]+=1
            else: ana_dict1[char] = 1
        for char in t:
            if char in ana_dict2:
                 ana_dict2[char]+=1
            else: ana_dict2[char] = 1
            
        if len(ana_dict1.keys()) != len(ana_dict2.keys()):
            return False
        for key, value in ana_dict1.items():
            if key in ana_dict2:
                if ana_dict2[key] == value:
                    continue
                else: return False
            else: return False
            
        return True    