import sys
import numpy as np
from time import time
from random import randint
import pandas as pd

from functions import create_array
from classes.Ordination import Ordination

animation = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%"]

def menu():
    print("--- MENU ---")
    print("1: Heap Sort")
    print("2: Merge Sort")
    print("3: Quick Sort")
    print("4: Quick Sort Rand")
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
    end_time = time()
    
    elapsed_time = end_time - start_time
    print(f"Array ordenado {arr}")
    print("Elapsed {:.5f} seconds".format(elapsed_time))
    
def multiple_run():
    # sizes = [1000, 5000]
    sizes = [ 100, 1000, 5000, 10000, 50000, 100000]
    order = Ordination()
    agm_dict = {
        'merge': order.merge_sort,
        # 'heap': order.heap_sort,
        # 'quick': order.quick_sort,
        # 'quick random': order.quick_sort_random,
        # 'quick med': order.quick_sort_m,
    }
    

    tests_size = 10
    for agm in agm_dict.keys():
        for size in sizes:
            results = []
            for t in range(tests_size): 
                arr = create_array(size,0.5)
                # Calculate time for ordination
                start_time = time()
                agm_dict[agm](arr)
                end_time = time()
                elapsed_time = (end_time - start_time)
                
                results.append([t, size, elapsed_time])
                sys.stdout.write(f"{agm} - {size}: {animation[t % len(animation)]} \r")
                sys.stdout.flush()
            df = pd.DataFrame(results)
            df.rename(columns={0: 't', 1: 'Size', 2: 'Time'}, inplace=True)
            df.to_csv(f"./results/{agm}_{size}.csv", sep=',', encoding='utf-8', index=False)
    

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