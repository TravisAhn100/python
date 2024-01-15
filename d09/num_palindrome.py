class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        r = 0
        while x!=0:
            last_digit = x % 10
            r = r * 10 + last_digit
