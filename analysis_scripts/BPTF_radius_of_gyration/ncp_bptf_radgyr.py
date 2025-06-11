# For running on BPTF systems without a nucleosome

import subprocess
import numpy as np
import os

os.makedirs('bptf_radgyr', exist_ok=True)

for i in np.arange(1,6):

    angle = f"""parm bptf_ncp.prmtop
    trajin bptf_ncp{i}.xtc
    radgyr All :1269-1436&!@H= mass out ./bptf_radgyr/bptf_ncp_bptfRG{i}.dat
    go
    quit
    """

    file_path = "angle.in"
    with open(file_path, "w") as file:
        file.write(angle)


    command = "cpptraj -i angle.in"
    subprocess.run(command, shell=True, check=True)
    remove = "rm angle.in"
    subprocess.run(remove, shell=True, check=True)
