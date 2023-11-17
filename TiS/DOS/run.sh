#! /bin/bash
# Density of states (DOS) of TiS
#####################################

mpirun -np 4 pw.x < TiS.scf.in > TiS.scf.out
mpirun -np 4 pw.x < TiS.nscf.in > TiS.nscf.out
mpirun -np 4 dos.x < TiS.dos.in > TiS.dos.out
