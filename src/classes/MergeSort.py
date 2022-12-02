class MergeSort:
   def __ini__(self) -> None:
         pass

   def __intercalate(self, arr, left, middle, right):
      n1 = middle - left + 1
      n2 = right - middle

      left_arr = [0] * (n1)
      right_arr = [0] * (n2)

      for i in range(0, n1):
         left_arr[i] = arr[left + i]

      for j in range(0, n2):
         right_arr[j] = arr[middle + 1 + j]

      i = 0
      j = 0
      k = left

      while i < n1 and j < n2:
         if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
         else:
            arr[k] = right_arr[j]
            j += 1
         k += 1

      while i < n1:
         arr[k] = left_arr[i]
         i += 1
         k += 1

      while j < n2:
         arr[k] = right_arr[j]
         j += 1
         k += 1

   def merge_sort(self, arr, left, right):
      if left < right:
         middle = left + (right - left)//2

         self.merge_sort(arr, left, middle)
         self.merge_sort(arr, middle+1, right)
         self.__intercalate(arr, left, middle, right)