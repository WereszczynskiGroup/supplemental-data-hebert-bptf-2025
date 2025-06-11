import MDAnalysis as mda
import numpy as np
import os
from MDAnalysis.lib.distances import distance_array
from MDAnalysis.lib import distances as contacts
import sys
# === CONFIGURATION ===
prefix = sys.argv[1]
output_dir = "shl_contacts"

# Make sure output directory exists
os.makedirs(output_dir, exist_ok=True)


# === PREPARE ANALYSIS ===
        # Load the topology and trajectory
u = mda.Universe(f"{prefix}.prmtop", f"{prefix}all.xtc")


print("Beginning SHL-resolved contact analysis...")

# Define the residue ranges
residues_h4 = u.select_atoms('(resid 647-670) and not (name H*)')
residues_h3 = u.select_atoms('(resid 1134-1169) and not (name H*)')
residues_h2a1 = u.select_atoms('(resid 397-412) and not (name H*)')
residues_h2b1 = u.select_atoms('(resid 525-558) and not (name H*)')
residues_dna = u.select_atoms('(resid 1-6 or resid 289-294) and not (name H*)')

    # Loop over the frames after frame 3000
def contacts_within_cutoff(u, group_a, group_b, group_a1, group_b1, group_c, radius=4.5):
    timeseries = []
    for ts in u.trajectory[0::]:
        dist1 = contacts.distance_array(group_a.positions, group_c.positions)
        dist2 = contacts.distance_array(group_b.positions, group_c.positions)
        dist3 = contacts.distance_array(group_a1.positions, group_c.positions)
        dist4 = contacts.distance_array(group_b1.positions, group_c.positions)
        n1_contacts = (dist1 < radius).sum()
        n2_contacts = (dist2 < radius).sum()
        n3_contacts = (dist3 < radius).sum()
        n4_contacts = (dist4 < radius).sum()
        timeseries.append([ts.frame, n1_contacts, n2_contacts, n3_contacts, n4_contacts])
    return np.array(timeseries)
    # Save the contact time series to a .dat file

conts = contacts_within_cutoff(u, residues_h2a1, residues_h2b1, residues_h3, residues_h4, residues_dna, radius=4.5)
np.savetxt(f'./shl_contacts/{prefix}_shl2_-7.0.dat', conts, fmt='%d %d %d %d %d', header='#DNA 1-6,289-294\n#Frame H2A H2B H3 H4 (contacts)')
print('Contacts in SHL -7.0 written.')

shl = -6.5
for i in np.arange(7,138,5):
    residues_dna = u.select_atoms(f'(resid {i}-{i+4} or resid {295-i-4}-{295-i}) and not (name H*)')
    conts = contacts_within_cutoff(u, residues_h2a1, residues_h2b1, residues_h3, residues_h4, residues_dna, radius=4.5)
    np.savetxt(f'./shl_contacts/{prefix}_shl2_{shl}.dat', conts, fmt='%d %d %d %d %d', header=f'#DNA {i}-{i+4},{295-i-4}-{295-i}\n#Frame H2A H2B H3 H4 (contacts)')
    print(f'Contacts in SHL {shl} written.')
    shl = shl + 0.5

residues_dna = u.select_atoms('resid 142-153 and not (name H*)')

conts = contacts_within_cutoff(u, residues_h2a1, residues_h2b1, residues_h3, residues_h4, residues_dna, radius=4.5)
np.savetxt(f'./shl_contacts/{prefix}_shl2_7.0.dat', conts, fmt='%d %d %d %d %d', header='#DNA 142-153\nFrame H2A H2B H3 H4 (contacts)')
print('Contacts in SHL 7.0 written.')
