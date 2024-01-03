from joblib import Parallel, delayed
import math
import time


def sqrt_func(i, j):
    time.sleep(1)
    return math.sqrt(i**j)


output = Parallel(n_jobs=8)(
    delayed(sqrt_func)(i, j) for i in range(5) for j in range(2)
)
print(output)
