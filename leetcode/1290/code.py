# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimal_value = 0

        values = self.getNodeValues(head)
        for a_value in values:
            decimal_value = (decimal_value * 2) + a_value

        return decimal_value

    def getNodeValues(self, node: ListNode) -> List:
        if node.next:
            values = self.getNodeValues(node.next)
        else:
            values = []

        values.append(int(node.val))
        return values