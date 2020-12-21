#!/bin/bash

mcpat_outputs='../mcpat_step2_results'
gem5_outputs='../../my_gem5/spec_results_step2'
energy_outputs='../print_energy_results'

output='results.json'
echo [ > $output

for file in $(ls $mcpat_outputs/*.txt)
do
  name=$(echo $file | rev | cut -d'/' -f1 | rev | cut -d'.' -f1)
  energy=$(cat $energy_outputs/$name.txt | grep energy | cut -d' ' -f3)
  runtime=$(cat $energy_outputs/$name.txt | grep runtime | cut -d' ' -f9)
  area=$(cat $mcpat_outputs/$name.txt | grep Area | head -1 | cut -d' ' -f5)

  echo { >> $output
  echo \"benchmark\": \"$name\", >> $output
  echo \"energy\": $energy, >> $output
  echo \"runtime\": $runtime, >> $output
  echo \"area\": $area >> $output
  echo }, >> $output
done

echo ] >> $output
