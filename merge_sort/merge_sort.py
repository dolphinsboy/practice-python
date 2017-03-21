#-*-coding:utf8-*-
class MergeSort(object):

    def __init__(self, numbers):
        self.numbers = numbers
        self.count = len(numbers)

    def sort(self):
        low = 0
        high = self.count - 1
        self.merge_sort(low, high)

    def merge_sort(self, low, high):
        if low < high:
            mid = (low+high)/2
            #分治
            self.merge_sort(low, mid)
            self.merge_sort(mid+1, high)
            #合并
            self.merge(low, mid, high)

    def merge(self, low, mid, high):
        b = []
        i = low
        j = mid + 1

        while i <= mid and j <= high:
            if self.numbers[i] <= self.numbers[j]:
                b.append(self.numbers[i])
                i += 1
            else:
                b.append(self.numbers[j])
                j += 1

        while i <= mid:
            b.append(self.numbers[i])
            i += 1

        while j <= high:
            b.append(self.numbers[j])
            j += 1
        #覆盖原数组相同位置的数据
        for idx, val in enumerate(b):
            self.numbers[low+idx]  = val
