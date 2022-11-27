class HeapSort:
   def __init__(self) -> None:
      pass
   
   def __rebuild_down_up(self, arr, start, end):
    root = start
    while root * 2 + 1 <= end:
        child = root * 2 + 1
        if child + 1 <= end and arr[child] < arr[child + 1]:
            child += 1
        if child <= end and arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
            root = child
        else:
            return

   def __build_heap(self, arr):
      n = len(arr)
      start = (n - 2) // 2
      while start >= 0:
         self.__rebuild_down_up(arr, start, n - 1)
         start -= 1

   def heap_sort(self, arr):
      self.__build_heap(arr)
      end = len(arr) - 1
      while end > 0:
         arr[end], arr[0] = arr[0], arr[end]
         self.__rebuild_down_up(arr, 0, end - 1)
         end -= 1