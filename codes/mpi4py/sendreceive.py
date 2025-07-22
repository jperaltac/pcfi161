from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    # en codigo de verdad este dato podria venir de un archivo, o cualquier otro lado.
    numData = 10
    comm.send(numData, dest=1)
    data = np.linspace(0.0, 3.14, numData)
    comm.Send(data, dest=1)

elif rank == 1:
    numData = comm.recv(source=0)  #recibe un objeto generico de python
    print('Number of data to receive: ', numData)
    data = np.empty(numData, dtype='d')
    comm.Recv(data, source=0) #recibe un objeto tipo buffer (arreglos, como numpy)

    print('data received: ', data)
