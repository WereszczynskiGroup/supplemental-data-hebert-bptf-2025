# For running on BPTF systems without a nucleosome

import subprocess
import numpy as np
import os

os.makedirs('bptf_angle', exist_ok=True)

for i in np.arange(1,6):

    angle = f"""parm bptf_ncp.prmtop
    trajin bptf_ncp{i}.xtc
    vector VA mask :1275-1316@CA :1317-1324@CA
    vector VB mask :1416-1421,137-142@CA :1393-1398,1428-1433@CA
    vectormath vec1 VA vec2 VB dotangle out ./bptf_angle/bptf_ncp_angle{i}.dat
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
