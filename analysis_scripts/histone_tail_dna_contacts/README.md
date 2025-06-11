# Histone tail contacts with DNA

These scripts are written for use with the trajectories uploaded to Zenodo from this work.

They will use MDAnalysis to calculate histone tail contacts with DNA with a 4.5 Angstrom cutoff between heavy atoms. They will output a different files for each histone tail.

To use any of these scripts, navigate to the corresponding simulation directory and execute as, for example:

python /directory/to/h3_bothtails.py bptf_ncp

Substitute "bptf_ncp" for "phd_ncp" or "nucleosome" as appropriate.

This will generate folders and files corresponding to the prefix of the trajectories.
