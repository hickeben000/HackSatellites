import matplotlib.pyplot as plt
import pandas as pd
import glob 
from mpl_toolkits.mplot3d import Axes3D

"""
Henry's Code
"""

# Load data
df = pd.read_csv("/Users/henrycronley/Downloads/CelestialChoreography/Data/RpoPlan.csv")

# 3D Trajectory Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(df["positionDepRelToChiefLvlhX"], 
        df["positionDepRelToChiefLvlhY"], 
        df["positionDepRelToChiefLvlhZ"], label="Trajectory", color='blue', linestyle='-', linewidth=1)

# Add labels to the beginning and end of the trajectory
start_x, start_y, start_z = df["positionDepRelToChiefLvlhX"].iloc[0], df["positionDepRelToChiefLvlhY"].iloc[0], df["positionDepRelToChiefLvlhZ"].iloc[0]
end_x, end_y, end_z = df["positionDepRelToChiefLvlhX"].iloc[-1], df["positionDepRelToChiefLvlhY"].iloc[-1], df["positionDepRelToChiefLvlhZ"].iloc[-1]

# Add colored dots to indicate the start and end points
ax.scatter(start_x, start_y, start_z, color='green', s=40, label='Start Point')  # Green dot for start
ax.scatter(end_x, end_y, end_z, color='red', s=40, label='End Point')  # Red dot for end

# Customize the plot appearance
ax.set_title("3D Trajectory Plot of RPO Plan", fontsize=15) 
ax.set_xlabel("Radial (km)", fontsize=12)
ax.set_ylabel("Intrack (km)", fontsize=12)
ax.set_zlabel("Crosstrack (km)", fontsize=12)
ax.legend()
ax.grid(True)

plt.show()