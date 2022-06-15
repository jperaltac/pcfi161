#Desde el 1 hasta el 1_000_000 cuales son primos
from mpi4py import MPI
import time
import numpy as np
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
if rank == 0:
    start = time.time()

N = 10000000
lst = np.array(range(2, N))
splt = [lst[i::size] for i in range(size)]
my_lst = comm.scatter(splt)

def primo(n):
    raiz = int(np.sqrt(n)) + 1
    if n <= 3:
        return True
    for i in range(2, raiz):
        if n % i == 0:
            return False
    return True

primos = []
for n in my_lst:
    if primo(n):
        primos.append(n)
total = comm.gather(primos)
if rank == 0:
    t = []
    for n in range(size):
        t.extend(total[n])
    print("hay {} primos entre 1 y 10000000".format(len(t)))
    print("{} seg".format(time.time() - start))

# 2     27.8768
# 4     15.1678
# 8     10.7246
