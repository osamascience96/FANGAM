import re

# Question asked by Uber
# The Solution is not be more modified.....
# The regular expression can also detect the spaces between brackets.....

# The problem is that the split function cannot differentiate between the space inside brackets vs the space outside brackets.

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
# determine if the input string is valid.

class Solution:
    def isValid(self, s):
        # let the value of flag 
        self.flag = False
        # let the regex be 
        # Fix the regex of this problem
        self.regex = r"\(\s*[\[\s*\{\s*\}\]]*\)"
        # if the string is empty, 
        if (s == ""):
            self.flag = True
        else:
            # seperates the string wrt space in it.
            self.newStr = s.split()
            for string in self.newStr:
               self.flag = True if re.match(self.regex, string) else False
               # if the flag becomes false at any point, break the loop
               if self.flag == False:
                   break
        
        # return flag
        return self.flag

# let a sample string be equal to 
# s = "() () {(())" #False
# s = "" #True
# s = "([{}]) ()" #True 
s = "() ()" #True

print(Solution().isValid(s))