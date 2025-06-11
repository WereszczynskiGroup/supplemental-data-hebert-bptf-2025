# H4 tail contacts with DNA by residue

This script is written for use with the trajectories uploaded to Zenodo from this work.

They will use MDAnalysis to iteratively calculate individual H4 residue contacts with DNA with a 4.5 Angstrom cutoff between heavy atoms. Specifically, this is for H4 near the modified H3.

To use, navigate to the corresponding simulation directory and execute as, for example:

python /directory/to/H4_byres_contacts.py bptf_ncp

Substitute "bptf_ncp" for "phd_ncp" or "nucleosome" as appropriate.

This will generate folders and files corresponding to the prefix of the trajectories. Every residue will have its own time series data file.
