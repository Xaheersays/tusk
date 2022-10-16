# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        def ReverseForME(s,n,l):
            if n == l//2 : return
            s[n] , s[l-n] = s[l-n] , s[n]
            return ReverseForME(s,n-1,l)
        ReverseForME(s,len(s)-1,len(s)-1)

        