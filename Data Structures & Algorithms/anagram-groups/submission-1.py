class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        answer = []
        visited = set()
        for i in range(n):
            if i in visited:
                continue
            anagram = []
            ana1 = sorted(strs[i])
            anagram.append(strs[i])
            visited.add(i)
            for j in range(i+1, n):
                if j in visited:
                    continue
                ana2 = sorted(strs[j])
                if ana1 == ana2:
                    anagram.append(strs[j])
                    visited.add(j)
            answer.append(anagram)
            
        return answer