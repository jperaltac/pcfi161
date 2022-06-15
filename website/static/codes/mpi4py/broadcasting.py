from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()


#Solo un rank tiene la data
if rank == 0:
    data = {'key1' : [1, 2, 3],
            'key2' : ('abc', 'xyz')}
else:
    data = None

#Broadcasting desde el rank=0 a los otros rank.

data = comm.bcast(data, root=0)
print('Rank: ', rank, ', data: ', data)
