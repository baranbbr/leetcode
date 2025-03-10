class Solution:
    def fib(self, n: int) -> int:
        # given n, calculate F(n)
        # e.g. when n=3 output is 2
        if n == 0 or n == 1:
            return n

        n1, n2 = 0, 1
        for i in range(2, n + 1):
            temp = n2
            n2 = n1 + n2
            n1 = temp
        return n2


if '__main__' == __name__:
    s = Solution()
    print(s.fib(2))
    print(s.fib(3))
    print(s.fib(4))

# 0, 1, 1, 2, 3, 5, 8
