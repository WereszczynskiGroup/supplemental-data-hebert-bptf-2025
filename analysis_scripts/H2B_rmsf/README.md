# Histone H2B RMSF

There are three scripts, one for each NCP system. They are written for use with the trajectories uploaded to Zenodo from this work.

They will use cpptraj to align the nucleosome to the H3 core helices, calculate RMSFs of each histone H2B, and create files with average RMSF values and their standard deviation.

To use, navigate to the corresponding simulation directories and execute each python script with its corresponding system.

This will generate folders and files corresponding to the prefix of the trajectories.
