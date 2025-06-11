# For running on BPTF systems without a nucleosome

import sys
import subprocess
import numpy as np
import os

os.makedirs('bptf_rmsd', exist_ok=True)
prefix = sys.argv[1]

for i in np.arange(1,6):

    rms = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc
    rms 2f6jex1 :1-59&!@H= first mass out ./bptf_rmsd/{prefix}_phd{i}rmsd.dat
    rms 2f6jexbromodomain1 :66-168&!@H= first mass out ./bptf_rmsd/{prefix}_bromo{i}rmsd.dat
    rms 2f6jexbptf1 :1-168&!@H= first mass out ./bptf_rmsd/{prefix}_bptf{i}rmsd.dat
    go
    quit
    """

    file_path = "rms.in"
    with open(file_path, "w") as file:
        file.write(rms)


    command = "cpptraj -i rms.in"
    subprocess.run(command, shell=True, check=True)
    remove = "rm rms.in"
    subprocess.run(remove, shell=True, check=True)
