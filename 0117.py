"""
# Definition for a Node.
class Node:
    def init(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        return None if root is None else list(filter(lambda _: False, itertools.accumulate(itertools.chain(([root],), repeat(None)), lambda nodes, _: next(iter(())) if not nodes else any(setattr(lhs, 'next', rhs) for lhs, rhs in itertools.zip_longest(nodes, nodes[1:])) or list(itertools.chain.from_iterable((*(() if n.left is None else (n.left,)), *(() if n.right is None else (n.right,))) for n in nodes))))) or root
    '''
    def _get_next_level(self, nodes: list['Node']) -> list['Node']:
        res = []
        for n in nodes:
            if n.left is not None:
                res.append(n.left)
            if n.right is not None:
                res.append(n.right)
        return res

    def _connect_level(self, nodes: list['Node']) -> None:
        for lhs, rhs in itertools.zip_longest(nodes, nodes[1:]):
            lhs.next = rhs

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        nodes = [root]
        while nodes:
            self._connect_level(nodes)
            nodes = self._get_next_level(nodes)

        return root
    '''
