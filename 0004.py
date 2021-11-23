class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return (lambda m, n: (lambda f: lambda *args: collections.deque(itertools.accumulate(chain((((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args))))(f))(*args),), itertools.repeat(None)), lambda f, _: (lambda f: f() if callable(f) else next(iter(())))(f)), maxlen=1).pop())(lambda f: lambda l, r: (lambda partition1: (lambda partition2: (lambda partition1, partition2: (lambda maxleft1, minright1, maxleft2, minright2: f(l, partition1) if maxleft1 > minright2 else f(r if l + 1 == r else partition1, r) if maxleft2 > minright1 else float(min(minright1, minright2)) if (m + n) % 2 == 1 else (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2)(float('-inf') if partition1 == 0 else nums1[partition1-1], float('inf') if partition1 == m else nums1[partition1], float('-inf') if partition2 == 0 else nums2[partition2-1], float('inf') if partition2 == n else nums2[partition2]))(*((partition1 + partition2 - n, n) if partition2 > n else (partition1 + partition2, 0) if partition2 < 0 else (partition1, partition2))))((m + n) // 2 - partition1))((l + r) // 2))(0, m))(len(nums1), len(nums2))
        '''
        m = len(nums1)
        n = len(nums2)

        # binary search on nums1
        l = 0
        r = m
        
        while True:
            partition1 = (l + r) // 2
            partition2 = (m + n) // 2 - partition1
            
            if partition2 > n:  # partition1 too left
                partition1 = partition1 + partition2 - n
                partition2 = n
            elif partition2 < 0:  # partition1 too right
                partition1 = partition1 + partition2
                partition2 = 0

            maxleft1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
            minright1 = float('inf') if partition1 == m else nums1[partition1]
            maxleft2 = float('-inf') if partition2 == 0 else nums2[partition2-1]
            minright2 = float('inf') if partition2 == n else nums2[partition2]

            if maxleft1 > minright2:  # move left
                r = partition1
            elif maxleft2 > minright1:  # move right
                l = r if l + 1 == r else partition1
            else:  # at correct place
                if (m + n) % 2 == 1:  # odd
                    return float(min(minright1, minright2))
                else:  # even
                    return (max(maxleft1, maxleft2) + min(minright1, minright2)) / 2
        '''
