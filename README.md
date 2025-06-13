# MM/GBSA Input Files

To use, strip nucleosome, BPTF+nucleosome, and PHD+nucleosome trajectories to the last 7000 frames and a step size of 10. This will create trajectories where each frame corresponds to 1 nanosecond.

Each subfolder contains the complex, ligand, and receptor prmtop files, the MM/GBSA input file decomp.in, and a file with a sample command that runs an analysis on a trajectory. Analysis of the results assumes each simulation run was done separately, i.e. run MMPBSA.py on bptf_ncp1.xtc, bptf_ncp2.xtc, etc.

Three-trajectory MM/GBSA was also run using bptf1.xtc and nucleosome1.xtc with bptf_ncp1.xtc, phd_finger1.xtc and nucleosome1.xtc with phd_ncp1.xtc, etc. The order doesn't really matter as long as all 5 trajectories are sampled.
