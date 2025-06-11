import sys
import os
import subprocess
import numpy as np

prmtop = 'nucleosome.prmtop'

for i in np.arange(1,6):

    h3rmsf = f"""parm {prmtop}
    trajin nucleosome{i}.xtc 3001 10000 10
    rms Run1 :1045-1054,1062-1076,1083-1111,1119-1128,1178-1189,1197-1211,1219-1246,1254-1264,342-369,694-721@CA first		
    atomicfluct :397-524&!@H= byres out ./NCP_histrmsf/M{i}h2a1.dat
    atomicfluct :749-876&!@H= byres out ./NCP_histrmsf/M{i}h2a2.dat
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
average = f"""readdata M1h2a1.dat
readdata M2h2a1.dat
readdata M3h2a1.dat
readdata M4h2a1.dat
readdata M5h2a1.dat
avg M1h2a1.dat:2 M2h2a1.dat:2 M3h2a1.dat:2 M4h2a1.dat:2 M5h2a1.dat:2 oversets out Mh2a1.dat
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

average = f"""readdata M1h2a2.dat
readdata M2h2a2.dat
readdata M3h2a2.dat
readdata M4h2a2.dat
readdata M5h2a2.dat
avg M1h2a2.dat:2 M2h2a2.dat:2 M3h2a2.dat:2 M4h2a2.dat:2 M5h2a2.dat:2 oversets out Mh2a2.dat
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
