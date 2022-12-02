from random import randint
import numpy as np
class QuickSort:
    def __init__(self) -> None:
        pass
    
    def __acha_pivo(self, arr, n1, n2, pto):
        left = n1
        right = n2-1
        pos = left + 1
        pto = 0
        while(True):
            if pos > right:
                return pto
            elif arr[pos] >= arr[pos-1]:
                pos = pos + 1
            else:
                pto = pos + 1
                return pto
                

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
        

    def __set_pivot(self, arr, left, right, op):
        if op == 1:
            rand = randint(left, right-1)
            arr[rand], arr[right - 1] = arr[right - 1], arr[rand]
        elif op == 2:
            n = right-left
            e = left
            if n <= 5:
                e = right-1
            else:
                e = self.__median_of_five(arr, left, right)
            arr[e], arr[right - 1] = arr[right - 1], arr[e]
        elif op == 3:
            pto = self.__acha_pivo(arr, left, right, 0)
        return arr

    def __partition(self, arr, left, right, op):
        arr = self.__set_pivot(arr, left, right, op)
        pivot = arr[right - 1]
        for i in range(left, right):
            if arr[i] > pivot:
                right += 1
            else:
                right += 1
                left += 1
                arr[i], arr[left - 1] = arr[left - 1], arr[i]
        return left - 1
    
    def quick_sort(self, arr, righ, left, op):
        if righ < left:
            p = self.__partition(arr, righ, left, op)
            self.quick_sort(arr, righ, p, op)
            self.quick_sort(arr, p + 1, left, op)


