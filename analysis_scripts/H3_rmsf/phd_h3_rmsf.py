import sys
import os
import subprocess
import numpy as np

prmtop = 'phd_ncp.prmtop'

for i in np.arange(1,6):

    h3rmsf = f"""parm {prmtop}
    trajin phd_ncp{i}.xtc 3001 10000 10
    rms Run1 :1045-1054,1062-1076,1083-1111,1119-1128,1178-1189,1197-1211,1219-1246,1254-1264,342-369,694-721@CA first		
    atomicfluct :999-1133&!@H= byres out ./NCP_histrmsf/EnoB{i}_h3_1.dat
    atomicfluct :1134-1268&!@H= byres out ./NCP_histrmsf/EnoB{i}_h3_2.dat
    go
    clear all
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

os.chdir('./NCP_histrmsf')
average = f"""readdata EnoB1_h3_1.dat
readdata EnoB2_h3_1.dat
readdata EnoB3_h3_1.dat
readdata EnoB4_h3_1.dat
readdata EnoB5_h3_1.dat
avg EnoB1_h3_1.dat:2 EnoB2_h3_1.dat:2 EnoB3_h3_1.dat:2 EnoB4_h3_1.dat:2 EnoB5_h3_1.dat:2 oversets out EnoB_h3_1.dat
go
quit
"""


file_path = "average.in"
with open(file_path, "w") as file:
    file.write(average)


command = "cpptraj -i average.in"
subprocess.run(command, shell=True, check=True)
remove = "rm average.in"
subprocess.run(remove, shell=True, check=True)

average = f"""readdata EnoB1_h3_2.dat
readdata EnoB2_h3_2.dat
readdata EnoB3_h3_2.dat
readdata EnoB4_h3_2.dat
readdata EnoB5_h3_2.dat
avg EnoB1_h3_2.dat:2 EnoB2_h3_2.dat:2 EnoB3_h3_2.dat:2 EnoB4_h3_2.dat:2 EnoB5_h3_2.dat:2 oversets out EnoB_h3_2.dat
go
quit
"""

file_path = "average.in"
with open(file_path, "w") as file:
    file.write(average)


command = "cpptraj -i average.in"
subprocess.run(command, shell=True, check=True)
remove = "rm average.in"
subprocess.run(remove, shell=True, check=True)
