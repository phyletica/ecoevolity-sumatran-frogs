#! /bin/sh

output_dir="../ecoevolity-simulations/plots"
for sim_type in exonic full full_doubled
do
    prefix="pyco-sumsims-${sim_type}-"
    pyco-sumsims -f -o "$output_dir" -p "$prefix" ../ecoevolity-simulations/${sim_type}_sim/batch0??/results.csv.gz
done
