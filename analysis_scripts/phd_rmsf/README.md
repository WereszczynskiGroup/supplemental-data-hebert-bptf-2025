# PHD finger RMSFs

This script is written for use with the trajectories uploaded to Zenodo from this work.

They will use cpptraj to align the heavy atoms of the PHD finger and calculate the RMSFs of the first 59 PHD finger residues.

To use with readers from NCP-bound systems, you will want to strip the nucleosome from the simulation first and save a corresponding prmtop file matching the prefix with the output stripped trajectories. To execute, navigate to the corresponding simulation directory and run the following, as an example:

python /directory/to/phd_rmsf.py phd_peptide

Substitute "phd_peptide" with another prefix where appropriate.

This will generate folders and files corresponding to the prefix of the trajectories, including files with average and standard deviation values of each residue's RMSF value.
