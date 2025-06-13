# H3 Solvent Accessible Surface Area, post-equilibration

This script is written for use with the trajectories uploaded to Zenodo from this work.

It will use cpptraj to read all five trajectories and calculate SASA for modified H3 residues 1-35.

To use, navigate to the directory with the trajectories and execute the code. For example, to calculate SASA for the H3 tail bound to BPTF, navigate to the BPTF_Nucleosome directory and run:

python /directory/to/h3_sasa_hist.py bptf_ncp

Substitute "bptf_ncp" for "phd_ncp" or "nucleosome" as appropriate.

This will generate folders and files corresponding to the prefix of the trajectories. These data files are meant for use with the plotting script that will create SASA histograms.
