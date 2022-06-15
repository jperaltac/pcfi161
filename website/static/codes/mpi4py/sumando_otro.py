from math import log, exp
from mpi4py import MPI
comm = MPI.COMM_WORLD

rank = comm.Get_rank()
size = comm.Get_size()

time = MPI.Wtime()

N = 1E8

lst = list(range(1000, int(N)))
split_lst = [lst[_i::size] for _i in range(size)]
my_lst = comm.scatter(split_lst)

print("La lista del rank ", rank, " tiene : ", len(my_lst), " elementos.")


#Ahora cada rank hace su trabajo
suma = 0.0
for k in my_lst:
    suma = suma + exp(-(k/(suma+1))**2)/log(1/(k+1)/log(1+exp(-suma)))
print("Rank ", rank, " sumo ", suma, " en ", MPI.Wtime()-time, " segundos.")

total = comm.gather(suma, root=0)
if rank == 0:
    print("La suma total es de ", sum(total))
