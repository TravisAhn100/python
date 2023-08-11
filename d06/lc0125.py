class Solution:
    def isPalindrome(self, s: str) -> bool:
        v = ''
        for c in s:
            if c.isalnum() == True:
                v += c.lower()
        if len(v) % 2 == 0:
            v2 = len(v) // 2 
            f_half = v [ 0 : v2]
            l_half = v [len(v) - 1 : v2 - 1 : -1]
            if l_half == f_half:
                return True
        else :
            v3 = len(v) // 2
            ahn = v [0 : v3]
            cheolsu = v [: v3  : -1]
            if ahn == cheolsu:
                return True
        