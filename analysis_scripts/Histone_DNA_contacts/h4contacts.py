import MDAnalysis as mda
from MDAnalysis.analysis import contacts
import numpy as np
import sys
import os
os.makedirs('Hist_contacts',exist_ok=True)
#------------------------------------------------------------------------------------#
# Contact Analysis DNA-base pairs and protein
#------------------------------------------------------------------------------------#
prmtop = sys.argv[1]
prefix = sys.argv[2]
for i in np.arange(1,6):
        # Load the topology and trajectory
    u = mda.Universe(prmtop, f"{prefix}{i}.xtc")

    # Define the residue ranges
    residues_1 = u.select_atoms('resid 1-294 and not name H*')
    residues_2 = u.select_atoms('(resid 295-396 or resid 647-748) and not name H*')

        # Loop over the frames after frame 3000
    def contacts_within_cutoff (u, group_a, group_b, radius=4.5):
        timeseries = []
        for ts in u.trajectory[3000::10]:
                # Calculate distance matrix between the two groups
            dist = contacts.distance_array(group_a.positions, group_b.positions)

            # Count the number of contacts below the cutoff distance
            n_contacts = contacts.contact_matrix(dist, radius).sum()
            timeseries.append([ts.frame, n_contacts])
        return np.array(timeseries)
        # Save the contact time series to a .dat file

    conts = contacts_within_cutoff(u, residues_1, residues_2, radius=4.5)
    np.savetxt(f'./Hist_contacts/{prefix}H4_{i}.dat', conts, fmt='%d %d', header='Frame Contacts')
    print(f'H4 evaluation in trajectory {i} written.')
