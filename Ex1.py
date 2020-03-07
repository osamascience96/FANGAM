# Problem asked by Microsoft

# Definition for Singly LinkedList 
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:  
    # Function that reverse the string
    def ReverseString(self, string):
        # init the new string to return 
        self.str = ""
        # loop through given 
        i = len(string) - 1
        # while i is greater than 0, run the loop
        while i >= 0:
           self.str = self.str + string[i]
           i-=1
    
    # Function that returns the list 
    def addTwoNumbers(self, l1, l2, c = 0):
        # init the first Node value to num1 and num2
        self.num1 = str(l1.value)
        self.num2 = str(l2.value)
        for i in range(2):
            # remaining node values to String nums
            l1 = l1.next
            l2 = l2.next
            self.num1 = self.num1 + str(l1.value)
            self.num2 = self.num2 + str(l2.value)
        # convert the string numbers to integer and add the result to string again
        result = str((int(self.num1) + int(self.num2)))
        # Process to Reverse the String
        self.ReverseString(result)
        # init the new linked list
        l3 = ListNode(int(self.str[0])) #init the 0th index data to list3
        tempList = l3 #stores the temperoray reference to the list
        for i in range(len(self.str)):
            if i == 0:
                #if the index is 0, continue the cycle
                continue
            # move the pointer to the next node
            l3.next = ListNode(int(self.str[i]))
            l3 = l3.next
        # init the l3 list to start node.    
        l3 = tempList
        return l3            


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)

# Print the list that contains the result
# init the variable to hold the value to print
string = ""
# while the list is not null, then concatenate
while result:
    string = string + str(result.value)
    result = result.next

print(string)