import sys
import os
import subprocess
import numpy as np
os.makedirs('PHD_rmsf', exist_ok=True)
prefix = sys.argv[1]

for i in np.arange(1,6):

    h3rmsf = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc 3001 10000 10
    rms Run1 :1-59&!@H= first		
    atomicfluct :1-59&!@H= byres out ./PHD_rmsf/{prefix}_phdrmsf{i}.dat
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

os.chdir('./PHD_rmsf')
average = f"""readdata {prefix}_phdrmsf1.dat
readdata {prefix}_phdrmsf2.dat
readdata {prefix}_phdrmsf3.dat
readdata {prefix}_phdrmsf4.dat
readdata {prefix}_phdrmsf5.dat
avg {prefix}_phdrmsf1.dat:2 {prefix}_phdrmsf2.dat:2 {prefix}_phdrmsf3.dat:2 {prefix}_phdrmsf4.dat:2 {prefix}_phdrmsf5.dat:2 oversets out {prefix}_phdrmsf.dat
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

