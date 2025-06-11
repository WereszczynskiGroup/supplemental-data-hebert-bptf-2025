# Histone contacts with DNA by residue

These scripts are written for use with the trajectories uploaded to Zenodo from this work.

They will use MDAnalysis to calculate histone contacts with DNA with a 4.5 Angstrom cutoff between heavy atoms.

To use any of these scripts, navigate to the corresponding simulation directory and execute as, for example:

python /directory/to/h3contacts.py bptf_ncp

Substitute "bptf_ncp" for "phd_ncp" or "nucleosome" as appropriate.

This will generate folders and files corresponding to the prefix of the trajectories. This will give the contacts for either the histone tails (h3tails.py, h4tails.py, etc.) or the entire histone over time starting from the first post-equilibration frame.
