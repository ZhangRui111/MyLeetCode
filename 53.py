"""
tag: 数组；动态规划；分治
53. 最大子序和
https://leetcode-cn.com/problems/maximum-subarray/
"""


def maxSubArray(nums):
    n_nums = len(nums)

    if n_nums == 1:
        return nums[0]

    dp = list()
    dp.append(nums[0])  # 状态dp[i]定义为数组nums中以num[i]结尾的最大连续子序列和
    for i in range(1, n_nums):
        dp.append(max(dp[i-1] + nums[i], nums[i]))
    print(dp)
    return max(dp)


def main():
    print(maxSubArray([-2, 1, -3]))
    print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(maxSubArray([1]))


if __name__ == '__main__':
    main()
