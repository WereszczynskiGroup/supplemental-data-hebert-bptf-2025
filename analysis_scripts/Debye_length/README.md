# Reader-DNA Debye length check

There are two scripts, one for use on PHD-bound NCP systems and one for use on BPTF-bound NCP systems. They are written for use with the trajectories uploaded to Zenodo from this work.

They will measure the distance between atoms in DNA and the corresponding reader, and record the number of atoms within 7.8 Angstroms of each other.

To use, navigate to the corresponding simulation directories and execute as follows.

For PHD-bound NCP:

python /directory/to/phd_debye_length.py


For BPTF-bound NCP:
python /directory/to/bptf_debye_length.py


This will generate folders and files corresponding to the prefix of the trajectories.
