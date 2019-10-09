#!/bin/bash
#PBS -l nodes=1:ppn=1
#PBS -l walltime=0:02:00
#PBS -q pace-ice
#PBS -N mbudati3_calc
#PBS -o stdout
#PBS -e stderr
cd $PBS_O_WORKDIR
source /nv/pace-ice/bcomer3/sparc_env.sh
python midterm.py

