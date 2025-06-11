import sys
import os
import subprocess
import numpy as np
import os

os.makedirs('Hbonds', exist_ok=True)
prefix = sys.argv[1]

for i in np.arange(1,6):

    h3rmsf = f"""parm {prefix}.prmtop
    trajin {prefix}{i}.xtc 3001 10000 10
    hbond dnah3bond :1-294,999-1268 series out Hbonds/{prefix}dnah3bond{i}series.dat nointramol
    hbond h3bond :999-1268 series out Hbonds/{prefix}h3bond{i}series.dat nointramol
    hbond dnah4bond :1-396,647-748 series out Hbonds/{prefix}dnah4bond{i}series.dat nointramol
    hbond h4bond :295-396,647-748 series out Hbonds/{prefix}h4bond{i}series.dat nointramol
    hbond dnah2abond :1-294,397-524,738-876 series out Hbonds/{prefix}dnah2abond{i}series.dat nointramol
    hbond h2abond :397-524,738-876 series out Hbonds/{prefix}h2abond{i}series.dat nointramol
    hbond dnah2bbond :1-294,525-646,877-998 series out Hbonds/{prefix}dnah2bbond{i}series.dat nointramol
    hbond h2bbond :525-646,877-998 series out Hbonds/{prefix}h2bbond{i}series.dat nointramol
    hbond dnaseries :1-294 series out Hbonds/{prefix}dnaseries{i}.dat nointramol
    hbond h3t_1bond :1-294,999-1034 series out Hbonds/{prefix}tail1h3{i}.dat nointramol
    hbond h3tbond :1-294,1134-1169 series out Hbonds/{prefix}tail2h3{i}.dat nointramol
    hbond h4t_1bond :1-294,295-324 series out Hbonds/{prefix}h4_tail1{i}.dat nointramol
    hbond h4tbond :1-294,647-676 series out Hbonds/{prefix}h4_tail2{i}.dat nointramol
    hbond h2ta_1bond :1-294,397-412 series out Hbonds/{prefix}h2a_1{i}.dat nointramol
    hbond h2tabond :1-294,749-765 series out Hbonds/{prefix}h2a{i}.dat nointramol
    hbond h2tb_1bond :1-294,525-558 series out Hbonds/{prefix}h2b_1{i}.dat nointramol
    hbond h2tbbond :1-294,877-910 series out Hbonds/{prefix}h2b{i}.dat nointramol
    go
    quit
    """

    file_path = "hbond.in"
    with open(file_path, "w") as file:
        file.write(h3rmsf)


    command = "cpptraj -i hbond.in"
    subprocess.run(command, shell=True, check=True)
    remove = "rm hbond.in"
    subprocess.run(remove, shell=True, check=True)
