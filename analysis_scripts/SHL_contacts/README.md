# Histone Contacts by Superhelical Location

These scripts are written for use with the trajectories uploaded to Zenodo from this work.

They will use MDAnalysis to iteratively calculate DNA contacts by superhelical location with histone tails with a 4.5 Angstrom cutoff between heavy atoms.

To use, combine the last 7000 frames of each trajectory into one with the convention {prefix}all.xtc. For example, for NCPs with BPTF, combine all 5 trajectories into one file called "bptf_ncpall.xtc". Move to the corresponding simulation directory and execute as, for example:

python /directory/to/1shl.py bptf_ncp

python /directory/to/2shl.py bptf_ncp

Substitute "bptf_ncp" for "phd_ncp" or "nucleosome" as appropriate.

This will generate folders and files corresponding to the prefix of the trajectories. Each SHL will have a time series showing histone tail contacts over time at the given SHL. Outputs from 1shl.py will be for the modified H3 side of the dyad, and 2shl.py for the other side.
