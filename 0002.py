# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return (lambda setval, setnext: (lambda new_head: (lambda f: lambda *args: collections.deque(itertools.accumulate(chain((((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args))))(f))(*args),), itertools.repeat(None)), lambda f, _: (lambda f: f() if callable(f) else next(iter(())))(f)), maxlen=1).pop())(lambda f: lambda new_head, current_node, carry, l1, l2: (lambda total: (lambda carry, digit: setval(current_node, digit) and None or (lambda l1, l2: (((lambda carry_node: setval(carry_node, 1) and None or setnext(current_node, carry_node))(ListNode()) if carry > 0 else None) and None or new_head) if l1 is None and l2 is None else (setnext(current_node, ListNode()) and None or f(new_head, current_node.next, carry, l1, l2)))(l1 if l1 is None else l1.next, l2 if l2 is None else l2.next))(total // 10, total % 10))((0 if l1 is None else l1.val) + (0 if l2 is None else l2.val) + carry))(new_head, new_head, 0, l1, l2))(ListNode()))(lambda node, v: setattr(node, 'val', v), lambda node, n: setattr(node, 'next', n))