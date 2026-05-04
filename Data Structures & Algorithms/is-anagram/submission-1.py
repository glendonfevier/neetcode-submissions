class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #so the problem is you given 2 string,1 is s "jar"and the second one is t="jam",so u gonna make sure that both of this string has the same words
        #first we will check both length because if different ==not palindrome
        if len(s)!=len(t):
            return False

        countS,countT={},{}
        for i in range(len(s)):
            countS[s[i]]=1+countS.get(s[i],0)
            countT[t[i]]=1+countT.get(t[i],0)
        for c in countS:
            if countS[c]!=countT.get(c,0):
                return False
        return True