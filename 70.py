"""
tag: 动态规划
70. 爬楼梯
https://leetcode-cn.com/problems/climbing-stairs/
"""


# def climbStairs(n: int) -> int:
#     """ Recursion (time-consuming) """
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return climbStairs(n-1) + climbStairs(n-2)


def climbStairs(n: int) -> int:
    """ DP """
    a, b = 1, 2
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(3, n+1):  # [3, n], i.e., n+1 is not reached
        tmp = a + b
        a = b
        b = tmp
    return b


def main():
    print(climbStairs(2))
    print(climbStairs(3))


if __name__ == '__main__':
    main()
