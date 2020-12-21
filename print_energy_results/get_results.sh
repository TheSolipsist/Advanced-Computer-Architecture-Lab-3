#!/bin/bash

mcpat_outputs='../Lab_3/mcpat_step2_results'
gem5_outputs='../my_gem5/spec_results_step2'
print_energy='../my_mcpat/Scripts/print_energy.py'


for file in $(ls $mcpat_outputs/*.txt)
do
  name=$(echo $file | rev | cut -d'/' -f1 | rev | cut -d'.' -f1)
  echo "$name"
  python2 $print_energy $mcpat_outputs/$name.txt $gem5_outputs/$name/stats.txt > "$name.txt"
done
