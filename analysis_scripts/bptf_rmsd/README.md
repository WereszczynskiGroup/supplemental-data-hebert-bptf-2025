# BPTF RMSD measurement

There are two scripts, one for use on NCP systems and one for use on systems without NCPs. They are written for use with the trajectories uploaded to Zenodo from this work.

To use, navigate to the corresponding simulation directories and execute as follows.

For unbound BPTF:

python /directory/to/bptf_rmsd.py bptf


For peptide-bound BPTF:
python /directory/to/bptf_rmsd.py bptf_peptide


For NCP-bound BPTF:
python /directory/to/ncp_bptf_rmsd.py

This will generate folders and files corresponding to the prefix of the trajectories. It will output different files corresponding to the PHD finger, the bromodomain, and the BPTF complex.
