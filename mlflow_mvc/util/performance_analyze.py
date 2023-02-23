"""Debug Functions Module"""

from functools import wraps
import time

def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        #logging.info(f'Function Name: {func.__name__}')
        #logging.info(f"args: {args}")
        #logging.info(f"kwargs: {args}")
        print(f"Took {total_time:.4f} seconds")
        return result
    return timeit_wrapper