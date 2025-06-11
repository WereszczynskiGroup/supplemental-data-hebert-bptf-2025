# H3 tail solvent accessible surface area

These scripts are written for use with the trajectories uploaded to Zenodo from this work.

They will use cpptraj to calculate the SASA of the H3 tail in each trajectory.

To use, navigate to the corresponding simulation directory and execute as, for example:

python /directory/to/h3_tail_sasa.py bptf_ncp

python /directory/to/h3k4me3_tail_sasa.py bptf_ncp

Substitute "bptf_ncp" for "phd_ncp" or "nucleosome" as appropriate.

This will generate folders and files corresponding to the prefix of the trajectories. Every residue will have its own time series data file.
