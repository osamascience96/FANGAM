# Problem asked by Microsoft

# Definition for Singly LinkedList 
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

class Solution:
    
    def addTwoNumbers(self, l1, l2, c = 0):
        return 0            


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)




