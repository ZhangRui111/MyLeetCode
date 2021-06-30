"""
tag: 数组；排序
912. 排序数组
https://leetcode-cn.com/problems/sort-an-array/
"""


class Solution0:
    """ 库函数 """
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        return nums


class Solution1:
    """ 冒泡排序 """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_nums = len(nums)
        for i in range(n_nums):
            for j in range(n_nums - i - 1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
        return nums

    def sortArrayWithFlag(self, nums: List[int]) -> List[int]:
        n_nums = len(nums)
        flag = True
        for i in range(n_nums):
            if flag:
                flag = False
                for j in range(n_nums - i - 1):
                    if nums[j] > nums[j + 1]:
                        flag = True
                        tmp = nums[j]
                        nums[j] = nums[j + 1]
                        nums[j + 1] = tmp
        return nums


class Solution2:
    """ 简单选择排序 """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_num = len(nums)
        for i in range(n_num):
            min_index = i
            for j in range(i + 1, n_num):
                if nums[j] < nums[min_index]:
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums


class Solution3:
    """ 直接插入排序 """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_num = len(nums)
        for i in range(1, n_num):
            temp = nums[i]
            j = i - 1
            while j >= 0:
                if temp < nums[j]:
                    nums[j + 1] = nums[j]
                    j -= 1
                else:
                    break
            nums[j+1] = temp
        return nums


class Solution4:
    """ 希尔排序（希尔增量） """
    def sortArray(self, nums: List[int]) -> List[int]:
        n_num = len(nums)
        step = len(nums)  # 增量
        while step > 1:
            step = int(step / 2)  # 可替换为其他增量
            for i in range(step):
                # 分组后应用直接插入排序
                for j in range(i + step, n_num, step):
                    temp = nums[j]
                    k = j - step
                    while k >= 0:
                        if temp < nums[k]:
                            nums[k + step] = nums[k]
                            k -= step
                        else:
                            break
                    nums[k + step] = temp
        return nums


class Solution5:
    """ 归并排序 -- 递归写法 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.merge_sort(nums, 0, len(nums) - 1)
        return nums

    def merge_sort(self, nums, l, r):
        if l == r:
            return
        mid = (l + r) // 2
        self.merge_sort(nums, l, mid)
        self.merge_sort(nums, mid + 1, r)
        tmp = []
        i, j = l, mid + 1
        while i <= mid or j <= r:
            if i > mid or (j <= r and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[l: r + 1] = tmp


class Solution6:
    """ 归并排序 -- 迭代写法 """
    def sortArray(self, nums: List[int]) -> List[int]:
        k = 1
        n_num = len(nums)
        while k < n_num:
            self.mergePass(nums, k, n_num)
            k *= 2
        return nums

    def mergePass(self, nums, k, n_num):
        i = 0
        while i < n_num - 2 * k:
            self.merge(nums, i, i + k - 1, i + 2 * k - 1)
            i += 2 * k
        if i + k < n_num:
            self.merge(nums, i, i + k - 1, n_num - 1)

    def merge(self, nums, left, mid, right):
        tmp = []
        i, j = left, mid + 1
        while i <= mid or j <= right:
            if i > mid or (j <= right and nums[j] < nums[i]):
                tmp.append(nums[j])
                j += 1
            else:
                tmp.append(nums[i])
                i += 1
        nums[left: right + 1] = tmp


class Solution7:
    """ 快速排序 -- 交换，递归实现 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            index = self.partation(nums, low, high)
            self.quickSort(nums, low, index - 1)
            self.quickSort(nums, index + 1, high)

    def partation(self, nums, low, high):
        pivot = nums[low]
        start = low
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            while low < high and nums[low] <= pivot:
                low += 1
            if low >= high:
                break
            self.swap(nums, low, high)
        self.swap(nums, start, low)
        return low

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


class Solution8:
    """ 快速排序 -- 交换，迭代（栈）实现 """
    def sortArray(self, nums: List[int]) -> List[int]:
        stack = list()
        stack.append(len(nums) - 1)
        stack.append(0)
        while stack:
            low = stack.pop()
            high = stack.pop()
            if low < high:
                index = self.partation(nums, low, high)
                stack.append(index - 1)
                stack.append(low)
                stack.append(high)
                stack.append(index + 1)
        return nums

    def partation(self, nums, low, high):
        pivot = nums[low]
        start = low
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            while low < high and nums[low] <= pivot:
                low += 1
            if low >= high:
                break
            self.swap(nums, low, high)
        self.swap(nums, start, low)
        return low

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


class Solution9:
    """ 快速排序 -- 交换，递归实现 + 三数取中 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            index = self.partation(nums, low, high)
            self.quickSort(nums, low, index-1)
            self.quickSort(nums, index+1, high)

    def partation(self, nums, low, high):
        # 三数取中
        mid = low + (high - low) // 2
        if nums[low] > nums[high]:
            self.swap(nums, low, high)
        if nums[mid] > nums[high]:
            self.swap(nums, mid, high)
        if nums[mid] > nums[mid]:
            self.swap(nums, mid, low)
        # 以下同上
        pivot = nums[low]
        start = low
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            while low < high and nums[low] <= pivot:
                low += 1
            if low >= high:
                break
            self.swap(nums, low, high)
        self.swap(nums, start, low)
        return low

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


class Solution10:
    """ 快速排序 -- 交换，递归实现 + 三数取中 + 三向切分 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            left, right = self.partation(nums, low, high)
            self.quickSort(nums, low, left-1)
            self.quickSort(nums, right+1, high)

    def partation(self, nums, low, high):
        # 三数取中
        mid = low + (high - low) // 2
        if nums[low] > nums[high]:
            self.swap(nums, low, high)
        if nums[mid] > nums[high]:
            self.swap(nums, mid, high)
        if nums[mid] > nums[mid]:
            self.swap(nums, mid, low)
        # 三向切分
        pivot = nums[low]
        left = low
        right = high
        i = low + 1
        while i <= right:
            if nums[i] > pivot:
                self.swap(nums, i, right)
                right -= 1
            elif nums[i] == pivot:
                i += 1
            else:
                self.swap(nums, i, left)
                left += 1
                i += 1
        return left, right

    def swap(self, nums, a, b):
        temp = nums[a]
        nums[a] = nums[b]
        nums[b] = temp


INSERTION_SORT_MAX_LENGTH = 7


class Solution11:
    """ 快速排序 -- 交换，递归实现 + 三数取中 + 三向切分 + 组合：插入排序 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:
            # 插入排序
            if high - low <= INSERTION_SORT_MAX_LENGTH:
                self.insertSort(nums, low, high)
                return

            # 三数取中
            mid = low + (high - low) // 2
            if nums[low] > nums[high]:
                self.swap(nums, low, high)
            if nums[mid] > nums[high]:
                self.swap(nums, mid, high)
            if nums[mid] > nums[mid]:
                self.swap(nums, mid, low)
            # 三向切分
            pivot = nums[low]
            left = low
            right = high
            i = low + 1
            while i <= right:
                if nums[i] > pivot:
                    self.swap(nums, i, right)
                    right -= 1
                elif nums[i] == pivot:
                    i += 1
                else:
                    self.swap(nums, i, left)
                    left += 1
                    i += 1
            self.quickSort(nums, low, left - 1)
            self.quickSort(nums, right + 1, high)

    def insertSort(self, nums, low, high):
        for i in range(low + 1, high + 1):
            temp = nums[i]
            j = i - 1
            while j >= 0:
                if nums[j] > temp:
                    nums[j + 1] = nums[j]
                    j -= 1
                else:
                    break
            nums[j + 1] = temp

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution12:
    """ LeetCode 快速排序 -- 交换，递归实现 """
    def sortArray(self, nums: List[int]) -> List[int]:
        self.randomized_quicksort(nums, 0, len(nums) - 1)
        return nums

    def randomized_quicksort(self, nums, left, right):
        if left < right:
            mid = self.randomized_partition(nums, left, right)
            self.randomized_quicksort(nums, left, mid - 1)
            self.randomized_quicksort(nums, mid + 1, right)

    def randomized_partition(self, nums, left, right):
        pivot_index = random.randint(left, right)
        self.swap(nums, pivot_index, right)
        pivot = nums[right]
        i = left
        for j in range(left, right):
            if nums[j] < pivot:
                self.swap(nums, i, j)
                i += 1
        self.swap(nums, i, right)
        return i

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution13:
    """ 堆排序 -- 下沉建堆 """
    def sortArray(self, nums: List[int]) -> List[int]:
        array = [0] + nums  # 从索引1开始存储
        len_nums = len(nums)
        # 下沉建堆，从第一个非叶子节点开始
        # [len_nums//2, len_nums//2-1, ..., 1]
        for i in reversed(range(1, len_nums // 2 + 1)):
            self.sink(array, i, len_nums)
        # 排序
        end = len_nums
        while end > 1:
            self.swap(array, 1, end)
            end -= 1  # 这一步必须在继续下沉之前
            self.sink(array, 1, end)
        for i in range(len_nums):
            nums[i] = array[i + 1]
        return nums

    def sink(self, array, index, end):
        while index * 2 <= end:
            # 获取最大/最小子节点
            j = index * 2
            if j + 1 <= end and array[j + 1] > array[j]:
                j += 1
            # 交换操作，父节点下沉，与最大/最小的孩子节点交换
            if array[index] < array[j]:
                self.swap(array, index, j)
                # 继续下沉
                index = j
            else:
                break

    def swap(self, nums, a, b):
        nums[a], nums[b] = nums[b], nums[a]


class Solution14:
    """ 计数排序 """
    def sortArray(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        max_num = max(nums)
        min_num = min(nums)

        # 设置 presum 数组长度，然后求出我们的前缀和数组，
        # 这里我们可以把求次数数组和前缀和数组用一个数组处理
        presum = [0] * (max_num - min_num + 1)
        len_presum = len(presum)
        # 次数数组
        for n in nums:
            presum[n - min_num] += 1
        # 前缀和数组
        for i in range(1, len_presum):
            presum[i] = presum[i - 1] + presum[i]

        # 临时数组
        temp = [-1] * len_nums
        # 逆序遍历数组，开始排序,注意偏移量
        for i in reversed(range(len_nums)):
            # 查找 presum 字典，然后将其放到临时数组，注意偏移度
            offset = nums[i] - min_num
            index = presum[offset] - 1
            temp[index] = nums[i]
            # 相应位置减一
            presum[offset] -= 1

        return temp
