from random import randint
class QuickSort:
    def __init__(self) -> None:
        pass

    def __partition(self, arr, start, end):
        pivot = arr[end - 1]
        for i in range(start, end):
            if arr[i] > pivot:
                end += 1
            else:
                end += 1
                start += 1
                arr[i], arr[start - 1] = arr[start - 1], arr[i]
        return start - 1
    
    def __partition_random(self, arr, start, end):
        rand = randint(start, end)
        arr[rand], arr[end - 1] = arr[end - 1], arr[rand]
        pivot = arr[end - 1]
        for i in range(start, end):
            if arr[i] > pivot:
                end += 1
            else:
                end += 1
                start += 1
                arr[i], arr[start - 1] = arr[start - 1], arr[i]
        return start - 1
    
    def quick_sort(self, arr, start, end):
        if start < end:
            p = self.__partition(arr, start, end)
            self.quick_sort(arr, start, p)
            self.quick_sort(arr, p + 1, end)
        # return arr
        
    def quick_sort_rand(self, arr, start, end):
        if start < end:
            p = self.__partition_random(arr, start, end)
            self.quick_sort(arr, start, p)
            self.quick_sort(arr, p + 1, end)


