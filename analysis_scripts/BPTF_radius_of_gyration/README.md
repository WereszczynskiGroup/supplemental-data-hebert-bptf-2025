# BPTF Radius of Gyration measurement

There are two scripts, one for use on NCP systems and one for use on systems without NCPs. They are written for use with the trajectories uploaded to Zenodo from this work.

To use, navigate to the corresponding simulation directories and execute as follows.

For unbound BPTF:

python /directory/to/bptf_radgyr.py bptf


For peptide-bound BPTF:
python /directory/to/bptf_radgyr.py bptf_peptide


For NCP-bound BPTF:
python /directory/to/ncp_bptf_radgyr.py bptf_ncp

This will generate folders and files corresponding to the prefix of the trajectories.
