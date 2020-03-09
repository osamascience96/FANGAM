# Question asked by Microsoft
# Find the solution in linear time without repeating characters.

class Solution:
    def lengthOfLongestSubString(self, s):
        self.length = 0 # length variable contains the value of the longest substring
        chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in chars:
            # if the frequency of the char is more than 1,
            x = s.count(i)
            if (x > 1):
                # add the number to the length 
                self.length = self.length + x
        return self.length

print (Solution().lengthOfLongestSubString('abrkaabcdefghijjxxx'))