from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print('Hola Mundo!, mi rank es: ', rank)
