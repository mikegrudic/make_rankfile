#!/usr/bin/env python                                                                                                     
from sys import argv

cores_per_node = int(argv[1])
num_nodes = int(argv[2])
num_omp = int(argv[3])

F = open("rankfile_%d_%d.txt"%(num_nodes, num_omp),'w')

for i in range(cores_per_node*num_nodes // num_omp):
    F.write("rank %d=+n%d slot=%d-%d\n"%(i,i // (cores_per_node/num_omp), (num_omp*i)%cores_per_node,(num_omp*i+num_omp - 1)%cores_per_node))

F.close()
