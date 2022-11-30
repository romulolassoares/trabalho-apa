import sys
import numpy as np
import pandas as pd

from time import time
from random import randint

from functions import create_array
from classes.Ordination import Ordination
from classes.Loader import Loader

def menu():
    print("--- MENU ---")
    print("1: Heap Sort")
    print("2: Merge Sort")
    print("3: Quick Sort")
    print("4: Quick Sort Rand")
    print("5: Quick Sort Med")
    print("------------")
    option = int(input("Select a Option: "))
    return option

def main():
    op = menu()
    order = Ordination()
    arr = create_array(30,mess)
    start_time = time()
    if op == 1:
        order.heap_sort(arr)
    elif op == 2:
        order.merge_sort(arr)
    elif op == 3:
        order.quick_sort(arr)
    elif op == 4:
        order.quick_sort_random(arr)
    elif op == 5:
        order.quick_sort_m(arr)
    end_time = time()
    
    elapsed_time = end_time - start_time
    print(f"Array ordenado {arr}")
    print("Elapsed {:.5f} seconds".format(elapsed_time))
    
def multiple_run():
    # sizes = [1000, 5000]
    sizes = [1000, 5000, 10000, 50000, 100000, 500000]
    order = Ordination()
    agm_dict = {
        'merge': order.merge_sort,
        'heap': order.heap_sort,
        'quick': order.quick_sort,
        'quick random': order.quick_sort_random,
        'quick med': order.quick_sort_m,
    }
    results = []

    tests_size = 10
    for agm in agm_dict.keys():
        loader_agm = Loader(
            f"・ Loading \033[1m{agm.upper()}\033[0m",
            f"・ The \033[1m{agm.upper()}\033[0m is done!!!",
            0.05
        ).start()
        for size in sizes:
            for t in range(tests_size):
                arr = create_array(size,0.5)
                # Calculate time for ordination
                start_time = time()
                agm_dict[agm](arr)
                end_time = time()
                # Save values to results array
                results.append([t, size, end_time - start_time])
        loader_agm.stop()
        df = pd.DataFrame(results)
        df.rename(columns={0: 't', 1: 'Size', 2: 'Time'}, inplace=True)
        df.to_csv(
            f"./results/{agm}.csv",
            sep=',',
            encoding='utf-8',
            index=False
        )

try:
    start_funct = int(sys.argv[1])
except IndexError:
    start_funct = 1
    
try:
    mess = float(sys.argv[2])
except IndexError:
    mess = 0.1


if start_funct == 1:
    main()
elif start_funct == 2:
    multiple_run()