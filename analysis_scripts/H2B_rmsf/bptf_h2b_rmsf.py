import sys
import os
import subprocess
import numpy as np

prmtop = 'bptf_ncp.prmtop'

for i in np.arange(1,6):

    h3rmsf = f"""parm {prmtop}
    trajin bptf_ncp{i}.xtc 3001 10000 10
    rms Run1 :1045-1054,1062-1076,1083-1111,1119-1128,1178-1189,1197-1211,1219-1246,1254-1264,342-369,694-721@CA first		
    atomicfluct :525-646&!@H= byres out ./NCP_histrmsf/E{i}h2b1.dat
    atomicfluct :877-998&!@H= byres out ./NCP_histrmsf/E{i}h2b2.dat
    go
    quit
    """

# Save the content to "sectstruc.in"
    file_path = "h3rmsf.in"
    with open(file_path, "w") as file:
        file.write(h3rmsf)


    command = "cpptraj -i h3rmsf.in"
    subprocess.run(command, shell=True, check=True)
    remove = "rm h3rmsf.in"
    subprocess.run(remove, shell=True, check=True)

os.chdir('./NCP_histrmsf')
average = f"""readdata E1h2b1.dat
readdata E2h2b1.dat
readdata E3h2b1.dat
readdata E4h2b1.dat
readdata E5h2b1.dat
avg E1h2b1.dat:2 E2h2b1.dat:2 E3h2b1.dat:2 E4h2b1.dat:2 E5h2b1.dat:2 oversets out Eh2b1.dat
go
quit
"""

# Save the content to "sectstruc.in"
file_path = "average.in"
with open(file_path, "w") as file:
    file.write(average)


command = "cpptraj -i average.in"
subprocess.run(command, shell=True, check=True)
remove = "rm average.in"
subprocess.run(remove, shell=True, check=True)

average = f"""readdata E1h2b2.dat
readdata E2h2b2.dat
readdata E3h2b2.dat
readdata E4h2b2.dat
readdata E5h2b2.dat
avg E1h2b2.dat:2 E2h2b2.dat:2 E3h2b2.dat:2 E4h2b2.dat:2 E5h2b2.dat:2 oversets out Eh2b2.dat
go
quit
"""

# Save the content to "sectstruc.in"
file_path = "average.in"
with open(file_path, "w") as file:
    file.write(average)


command = "cpptraj -i average.in"
subprocess.run(command, shell=True, check=True)
remove = "rm average.in"
subprocess.run(remove, shell=True, check=True)
