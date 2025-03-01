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
        df["positionDepRelToChiefLvlhZ"], label="Trajectory")
ax.set_title("3D Trajectory Plot of RPO Plan") 
ax.set_xlabel("Radial")
ax.set_ylabel("Intrack")
ax.set_zlabel("Crosstrack")
plt.legend()
plt.show() 