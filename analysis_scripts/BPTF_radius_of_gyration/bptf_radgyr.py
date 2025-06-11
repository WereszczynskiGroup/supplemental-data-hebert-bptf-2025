# For running on BPTF systems without a nucleosome

import sys
import subprocess
import numpy as np
import os

os.makedirs('bptf_radgyr', exist_ok=True)
prefix = sys.argv[1]

for i in np.arange(1,6):

    rg = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc
    radgyr All :1-168&!@H= mass out ./bptf_radgyr/{prefix}_bptfRG{i}.dat
    go
    quit
    """

    file_path = "rg.in"
    with open(file_path, "w") as file:
        file.write(rg)


    command = "cpptraj -i rg.in"
    subprocess.run(command, shell=True, check=True)
    remove = "rm rg.in"
    subprocess.run(remove, shell=True, check=True)
