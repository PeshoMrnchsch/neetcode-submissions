class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            getS = ''.join(sorted(i))
            if getS in res:
                res[getS].append(i) 
            else:
                res[getS] = [i]
        return list(res.values())
        
        