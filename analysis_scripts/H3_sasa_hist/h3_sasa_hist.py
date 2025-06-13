import sys
import os
import subprocess
import numpy as np
os.makedirs('./SASA', exist_ok=True)
prefix = sys.argv[1]

h3rmsf = f"""parm {prefix}.prmtop
trajin {prefix}1.xtc 3001 10000 1
trajin {prefix}2.xtc 3001 10000 1
trajin {prefix}3.xtc 3001 10000 1
trajin {prefix}4.xtc 3001 10000 1
trajin {prefix}5.xtc 3001 10000 1
surf :999-1034 run1 out SASA/{prefix}H3SASAall.dat
go
quit
"""

file_path = "h3rmsf.in"
with open(file_path, "w") as file:
    file.write(h3rmsf)


command = "cpptraj -i h3rmsf.in"
subprocess.run(command, shell=True, check=True)
remove = "rm h3rmsf.in"
subprocess.run(remove, shell=True, check=True)
