class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return (lambda collections, itertools: (lambda f: lambda *args: collections.deque(itertools.accumulate(chain((((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args))))(f))(*args),), itertools.repeat(None)), lambda f, _: (lambda f: f() if callable(f) else next(iter(())))(f)), maxlen=1).pop())(lambda f: lambda acc, n: (lambda current_number: (lambda pair_number: (lambda i: [i, n] if i is not None else f({**acc, pair_number: n}, n + 1))(acc.get(current_number)))(target - current_number))(nums[n]))({}, 0))(__import__('collections'), __import__('itertools'))
        '''
        Y = lambda f: (lambda x: x(x))(lambda x: f(lambda *args: x(x)(*args)))
        def f1(f):
            def f2(acc, n):
                current_number = nums[n]
                pair_number = target - current_number
                i = acc.get(current_number)
                if i is not None:
                    return [i, n]
                else:
                    return f({**acc, pair_number: n}, n + 1)
            return f2
        return Y(f1)({}, 0)
        '''
