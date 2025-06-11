# Histone-DNA hydrogen bonds

This script is written for use with the trajectories uploaded to Zenodo from this work.

It uses cpptraj to evaluate the hydrogen bonds between each histone and DNA, as well as the hydrogen bonds between DNA strands and hydrogen bonds between DNA and histone tails.

To use, navigate to the corresponding simulation directory and execute as, for example:

python /directory/to/calc_hbonds.py bptf_ncp

Substitute "bptf_ncp" for "phd_ncp" or "nucleosome" as appropriate.

This will generate folders and files corresponding to the prefix of the trajectories. Every component series will have its own time series data file.

DNA is treated as two separate molecules, so the nointramol flag in cpptraj will not apply. When plotting hydrogen bonds, we will manually subtract the hydrogen bonds between the DNA strands.
