import MDAnalysis as mda
from MDAnalysis.analysis import contacts
import numpy as np
import sys
import os

os.makedirs('debye', exist_ok=True)

#------------------------------------------------------------------------------------#
# Contact Analysis DNA-base pairs and protein
#------------------------------------------------------------------------------------#

for i in np.arange(1,6):
        # Load the topology and trajectory
    u = mda.Universe('bptf_ncp.prmtop', 'bptf_ncp'+str(i)+'.xtc')

    # Define the residue ranges
    residues_1 = u.select_atoms('resid 1-294')
    residues_2 = u.select_atoms('resid 1269-1438')

        # Loop over the frames after frame 30000
    def contacts_within_cutoff (u, group_a, group_b, radius=7.8):
        timeseries = []
        for ts in u.trajectory[0::1]:
                # Calculate distance matrix between the two groups
            dist = contacts.distance_array(group_a.positions, group_b.positions)

            # Count the number of contacts below the cutoff distance
            n_contacts = contacts.contact_matrix(dist, radius).sum()
            timeseries.append([ts.frame, n_contacts])
        return np.array(timeseries)
        # Save the contact time series to a .dat file

    conts = contacts_within_cutoff(u, residues_1, residues_2, radius=7.8)
    np.savetxt(f"./debye/bptf_debye{i}.dat", conts, fmt='%d %d', header='#Frame Contacts')
    print(f'Debye evaluation in trajectory {i} written.')
