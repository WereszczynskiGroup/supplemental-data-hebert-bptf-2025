# Epock config files

These are the config files generated for analyzing the pocket volume of the PHD finger. However, rather than directly using these, it is recommended to follow this protocol:

1. Load a pdb of the PHD finger with bound H3 peptide.
2. Using the Epock plugin, define inclusion spheres of radius 5.0 Angstroms centered on the first 5 H3 peptide residues.
3. In the Epock plugin, save this inclusion space as a config file.
4. Close VMD and reload the same pdb as before. Also load a PHD finger trajectory.
5. Using VMD's RMSD trajectory alignment tool, align the PHD finger's residues 6 to 50. Be sure to align the trajectory to the PDB, and not the other way around!
6. Delete the PDB molecule from VMD.
7. Open the Epock plugin and load the config file from before. If done properly, the config file should add the inclusion spheres in the same place as before.
8. Run the trajectory fitting tool in Epock and save the resulting time series. 


