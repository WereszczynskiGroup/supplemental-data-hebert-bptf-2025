# MM/GBSA Input Files

To use, strip nucleosome, BPTF+nucleosome, and PHD+nucleosome trajectories to the last 7000 frames and a step size of 10. This will create trajectories where each frame corresponds to 1 nanosecond. Also, strip trajectories of all but DNA and corresponding H4 tail.

Each subfolder contains the complex, ligand, and receptor prmtop files, the MM/GBSA input file decomp.in, and a file with a sample command that runs an analysis on a trajectory. Analysis of the results assumes each simulation run was done separately, i.e. run MMPBSA.py on bptf_ncp1.xtc, bptf_ncp2.xtc, etc.

These input files also contain sample PDBs for examples of input structures for the complex trajectory.
