import os
import pyperf
import pandas as pd
import time
from massql.msql_fileloading import load_data  # Replace 'your_module' with the actual module containing load_data

def benchmark_load_data_cache():
    input_filename = "/home/alberto/repos/data/OxPAPC_Targeted_662_20eV_2ul.mzML" 
    cache = "feather"

    load_data(input_filename, cache=cache)
    

def main():
    runner = pyperf.Runner(values=1, processes=2)

    results_no_cache = runner.bench_func("load_data_cache", benchmark_load_data_cache, inner_loops=2)


if __name__ == "__main__":
    main()
