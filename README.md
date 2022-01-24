# make_rankfile
So your hybrid MPI/OpenMP application isn't assigning thread affinity correctly, and you've tried every automated option. Time for the nuclear option: a rankfile that explicitly tells each MPI rank what cores its OpenMP threads get.

# Instructions
To generate your rankfile, run the script in the command line with the following format:
```
python make_rankfile.py <number of cores per node> <number of nodes in MPI configuration> <number of OpenMP threads per MPI rank>
```

For example, if I am on a system with 128 cores per node, and I want to run a job on 4 nodes with 4 OpenMP threads per MPI rank, I would run:
```
python make_rankfile.py 128 4 4
```

This will generate the file `rankfile_4_4.txt`. Then, when running the job, Include the `-rankfile` argument to `mpirun`:
```
export OMP_NUM_THREADS=4;
mpirun -np 128 -rankfile rankfile_4_4.txt ./MY_EXECUTABLE
```

Note that this script assumes the normal, usually most cache-efficient configuration of assigning MPI ranks to continguous blocks of cores.
