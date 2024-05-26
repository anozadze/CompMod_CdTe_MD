import ovito
from ovito.data import *
import numpy as np

# Load the two input files
node1 = ovito.io.import_file("PerfCryst")
node2 = ovito.io.import_file("GrownCryst2")

# Get the particle positions from the two files
data1 = node1.compute()
data2 = node2.compute()
positions1 = data1.particles.positions
positions2 = data2.particles.positions

def align_positions(positions1, positions2):
    """
    Align the particle positions by removing any extra particles from the larger system.
    
    Parameters:
    positions1 (numpy.ndarray): Particle positions of the first system.
    positions2 (numpy.ndarray): Particle positions of the second system.
    
    Returns:
    tuple: Two numpy arrays containing the aligned particle positions.
    """
    if len(positions1) > len(positions2):
        positions1 = positions1[:len(positions2)]
    elif len(positions2) > len(positions1):
        positions2 = positions2[:len(positions1)]
    return positions1, positions2

def calculate_rmsd(positions1, positions2):
    """
    Calculate the root-mean-square deviation (RMSD) between two sets of particle positions,
    excluding the z-coordinates.
    
    Parameters:
    positions1 (numpy.ndarray): Particle positions of the first system.
    positions2 (numpy.ndarray): Particle positions of the second system.
    
    Returns:
    float: The RMSD value.
    """
    # Exclude the z-coordinates
    positions1_xy = positions1[:, :2]
    positions2_xy = positions2[:, :2]

    # Calculate the RMSD
    diff = positions1_xy - positions2_xy
    rmsd = np.sqrt(np.mean(np.sum(diff * diff, axis=1)))
    
    return rmsd

# Align the particle positions
positions1, positions2 = align_positions(positions1, positions2)

# Calculate the RMSD
rmsd = calculate_rmsd(positions1, positions2)
print(f"RMSD between 'PerfCryst' and 'GrownCryst' (excluding z-coordinates): {rmsd:.4f}")
