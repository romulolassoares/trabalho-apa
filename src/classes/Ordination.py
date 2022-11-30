from classes.HeapSort import HeapSort
from classes.MergeSort import MergeSort
from classes.QuickSort import QuickSort

class Ordination:
   def __init__(self) -> None:
      pass
   
   def heap_sort(self, arr):
      hp = HeapSort()
      hp.heap_sort(arr)
      
   def merge_sort(self, arr):
      mg = MergeSort()
      n = len(arr)
      mg.merge_sort(arr, 0, n-1)
      
   def quick_sort(self, arr):
      quick = QuickSort()
      n = len(arr)
      quick.quick_sort(arr, 0, n, 0)
      
   def quick_sort_random(self, arr):
      quick = QuickSort()
      n = len(arr)
      quick.quick_sort(arr, 0, n, 1)
      
   def quick_sort_m(self, arr):
      quick = QuickSort()
      n = len(arr)
      quick.quick_sort(arr, 0, n, 2)