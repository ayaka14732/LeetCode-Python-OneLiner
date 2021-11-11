class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        return (lambda f: lambda *args: collections.deque(itertools.accumulate(chain((((lambda f: (lambda x: x(x))(lambda y: f(lambda *args: lambda: y(y)(*args))))(f))(*args),), itertools.repeat(None)), lambda f, _: (lambda f: f() if callable(f) else next(iter(())))(f)), maxlen=1).pop())(lambda f: lambda i, j, acc, max_length: max_length if j == len(s) else (lambda acc: f(i, j + 1, acc, max(len(acc), max_length)))({s[j], *acc}) if s[j] not in acc else f(i + 1, j, set((x for x in acc if x != s[i])), max_length))(0, 0, set(), 0)
        '''
        def f(i, j, acc, max_length):
            if j == len(s):
                return max_length
            else:
                if s[j] not in acc:
                    acc = {s[j], *acc}
                    max_length = max(len(acc), max_length)
                    j += 1
                else:
                    acc = set((x for x in acc if x != s[i]))
                    i += 1
                return f(i, j, acc, max_length)
        return f(0, 0, set(), 0)
        '''
