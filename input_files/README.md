# Input Files
- Starting conformation PDB files

**Simulation engine neutrality:**  
While most systems in this lab are prepared using AMBER tools (e.g., `tleap`), this directory structure is designed to support setup workflows for other MD engines as well.


Included here are starting conformations of each simulation. Each system was run with the ff19SB protein force field, OPC water, and Li-Merz ions for OPC water. In addition, any systems with H3 must use the m3l.lib file for trimethylated lysine.

All systems were neutralized with sodium ions and had extra Na+ and Cl- ions added to create a concentration of 150 mM NaCl.

Nucleosome systems use BSC1 force fields for DNA.

Systems with PHD fingers and BPTF must use the Zinc Amber Force Field. The zinc centers must be edited in the PDB file according to the ZAFF tutorial: 
- https://ambermd.org/tutorials/advanced/tutorial20/ZAFF.php

Lysine 4 on one H3 (residue 1002 in these nucleosome PDBs) was trimethylated. The library loaded when creating the prmtop files can be found here:
http://pc164.materials.uoi.gr/dpapageo/amberparams.php

We obtained reader-NCP complexes by aligning the H3 tail residues in UCSF Chimera and splicing the ones from the BPTF crystal structure onto the nucleosome while maintaining the binding mode.
