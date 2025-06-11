# For running on BPTF systems without a nucleosome

import sys
import subprocess
import numpy as np
import os

os.makedirs('bptf_angle', exist_ok=True)
prefix = sys.argv[1]

for i in np.arange(1,6):

    angle = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc
    vector VA mask :7-48@CA :49-56@CA
    vector VB mask :148-153,137-142@CA :125-130,160-165@CA
    vectormath vec1 VA vec2 VB dotangle out ./bptf_angle/{prefix}_angle{i}.dat
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
