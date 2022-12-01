from random import randint
import numpy as np
class QuickSort:
    def __init__(self) -> None:
        pass
    
    # def __acha_pivo(self, arr, n1, n2, pto):
    #     left = n1
    #     right = n2
    #     pos = left + 1
    #     pto = 0
    #     while(true):
    #         if pos > right:
    #             return pto
    #         elif arr[pos] >= arr[pos-1]:
    #             pos = pos + 1
    #         else:
    #             pto = pos + 1
    #             return pto
                

    def __median_of_five(self, arr, start, end):
        middle50 = (start + end - 1) // 2
        middle25 = (start + middle50) //2
        middle75 = (middle50 + end - 1) // 2
        a = arr[start]
        b = arr[middle25]
        c = arr[middle50]
        d = arr[middle75]
        e = arr[end - 1]
        if b < a:
            a, b = b, a
        if d < c:
            c, d = d, c
        if c < a:
            b, d = d, b
            c = a
        a = e
        if b < a:
            a, b = b, a
        if a < c:
            b, d = d, b
            a = c
        if d < a:
            return d
        else:
            return a
        

    def __set_pivot(self, arr, start, end, op):
        if op == 1:
            rand = randint(start, end-1)
            arr[rand], arr[end - 1] = arr[end - 1], arr[rand]
        elif op == 2:
            n = end-start
            e = start
            if n <= 5:
                e = end-1
            else:
                e = self.__median_of_five(arr, start, end)
            arr[e], arr[end - 1] = arr[end - 1], arr[e]
        return arr

    def __partition(self, arr, start, end, op):
        arr = self.__set_pivot(arr, start, end, op)
        pivot = arr[end - 1]
        for i in range(start, end):
            if arr[i] > pivot:
                end += 1
            else:
                end += 1
                start += 1
                arr[i], arr[start - 1] = arr[start - 1], arr[i]
        return start - 1
    
    def quick_sort(self, arr, start, end, op):
        if start < end:
            p = self.__partition(arr, start, end, op)
            self.quick_sort(arr, start, p, op)
            self.quick_sort(arr, p + 1, end, op)


