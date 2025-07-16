# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        decimal_value = 0

        values = self.getNodeValues(head)
        place_value = 1
        for a_value in values:
            if a_value == 1:
                decimal_value += place_value
            place_value *= 2

        return decimal_value

    def getNodeValues(self, node: ListNode) -> List:
        if node.next:
            values = self.getNodeValues(node.next)
        else:
            values = []

        values.append(int(node.val))
        return values