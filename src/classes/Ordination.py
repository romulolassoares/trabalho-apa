from classes.HeapSort import HeapSort
from classes.MergeSort import MergeSort

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