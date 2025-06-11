import sys
import subprocess
import numpy as np
import os

os.makedirs('H3_SASA', exist_ok=True)
prefix = sys.argv[1]

for i in np.arange(1,6):

    sasa = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc
    surf :999-1034 run1 out H3_SASA/{prefix}_h3k4me3sasa{i}.dat
    go
    quit
    """

    file_path = "sasa.in"
    with open(file_path, "w") as file:
        file.write(sasa)


    command = "cpptraj -i sasa.in"
    subprocess.run(command, shell=True, check=True)
    remove = "rm sasa.in"
    subprocess.run(remove, shell=True, check=True)
