import os
import pyperf
import pandas as pd
import time
from massql.msql_fileloading import load_data  # Replace 'your_module' with the actual module containing load_data

def benchmark_load_data_no_cache():
    input_filename = "/home/alberto/repos/data/OxPAPC_Targeted_662_20eV_2ul.mzML" 

    load_data(input_filename)
    

def main():
    runner = pyperf.Runner(values=1, processes=2)

    # Run the benchmark
    results_no_cache = runner.bench_func("load_data_no_cache", benchmark_load_data_no_cache, inner_loops=2)


if __name__ == "__main__":
    main()
