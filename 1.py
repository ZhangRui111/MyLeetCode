"""
tag: 数组；哈希表
1. 两数之和
https://leetcode-cn.com/problems/two-sum/
"""


# def twoSum(nums, target):
#     """
#     violent enumeration
#     :param nums:
#     :param target:
#     :return:
#     """
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     return []


def twoSum(nums, target):
    """
    hash table
    :param nums:
    :param target:
    :return:
    """
    hashtable = dict()
    for i, num in enumerate(nums):
        if (target - num) in hashtable:  # i.e., if (target - num) in hashtable.keys()
            return [hashtable[target - num], i]
        hashtable[num] = i
    return []


def main():
    print(twoSum(nums=[2, 7, 11, 15], target=9))
    print(twoSum(nums=[3, 2, 4], target=6))


if __name__ == '__main__':
    main()
