#! /bin/sh

username="$USER"
if [ "$username" == "aubjro" ]
then
    module load gcc/6.1.0
fi

if [ -n "$PBS_JOBNAME" ]
then
    source ${PBS_O_HOME}/.bash_profile
    cd $PBS_O_WORKDIR

    module load gcc/5.3.0
fi

simname="full_doubled_sim"
cfgpath="../../ecoevolity-configs/${simname}.yml"
outputdir="../../ecoevolity-simulations/${simname}/batch002"
rngseed=914542314
nreps=100

mkdir -p "$outputdir"

simcoevolity --seed="$rngseed" -n "$nreps" -o "$outputdir" --relax-missing-sites --relax-constant-sites --relax-triallelic-sites --charsets "$cfgpath"
