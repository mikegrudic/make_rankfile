# make_rankfile
So your hybid MPI/OpenMP application isn't assigning thread affinity correctly, and you've tried every automated option. Time for the nuclear option: a rankfile that explicitly tells each MPI rank what cores its OpenMP threads get.

# Instructions
To generate your rankfile, run the script in the command line with the following format:
```
python make_rankfile.py <number of cores per node> <number of nodes in MPI configuration> <number of OpenMP threads per MPI rank>
```

