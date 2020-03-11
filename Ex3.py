# Question Asked by Twitter

# Find the longest palindromic SubString in S.

class Solution:
    def longestPalindrome(self, s):

        # init the start and last corners of the string
        self.first = 0
        self.last = len(s) - 1

        for i in range(len(s) - 1):
            self.index = len(s) - 1
            while(self.index >= 0):
                # compare chars
                if (i != self.index):
                    if (s[i] == s[self.index]):
                        self.first = i
                        self.last = self.index
                        return s[self.first:self.last+1]
                        
                self.index-=1

        return None


# banana, million, tracecars, diana
print(Solution().longestPalindrome("tracecars"))

