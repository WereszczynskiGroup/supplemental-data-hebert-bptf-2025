# Angle measurements between the bromodomain and PHD finger

There are two scripts, one for use on NCP systems and one for use on systems without NCPs. They are written for use with the trajectories uploaded to Zenodo from this work.

These use cpptraj to define two vectors and use their dot product to evaluate the angle between them.

To use, navigate to the corresponding simulation directories and execute as follows.

For unbound BPTF:

python /directory/to/phd_bromodomain_angle.py bptf


For peptide-bound BPTF:
python /directory/to/phd_bromodomain_angle.py bptf_peptide


For NCP-bound BPTF:
python /directory/to/ncp_phd_bromodomain_angle.py bptf_ncp

This will generate folders and files corresponding to the prefix of the trajectories.
