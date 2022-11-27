import sys
import numpy as np
from time import time
from random import randint

from functions import create_array
from classes.Ordination import Ordination

def menu():
    print("--- MENU ---")
    print("1: Heap Sort")
    print("2: Merge Sort")
    print("------------")
    option = int(input("Select a Option: "))
    return option

def main():
    op = menu()
    order = Ordination()
    arr = create_array(10,mess)
    
    start_time = time()
    if op == 1:
        order.heap_sort(arr)
    elif op == 2:
        order.merge_sort(arr)
    end_time = time()
    
    elapsed_time = end_time - start_time
    print(f"Array ordenado {arr}")
    print("Elapsed {:.5f} seconds".format(elapsed_time))
    
def multiple_run_heap_sort():
    print("entrou")
    sizes = [1000, 5000, 10000, 50000, 100000, 500000]
    order = Ordination()
    for size in sizes:
        arr = create_array(size,0.5)
        start_time = time()
        order.heap_sort(arr)
        end_time = time()
        elapsed_time = (end_time - start_time)
        print(f"Size {size} it took {elapsed_time:.5f} s")

try:
    start_funct = int(sys.argv[1])
except IndexError:
    print("You did not specify a file")
    start_funct = 1
    
try:
    mess = float(sys.argv[2])
except IndexError:
    print("You did not specify a file")
    mess = 0.1


if start_funct == 1:
    main()
elif start_funct == 2:
    multiple_run_heap_sort()