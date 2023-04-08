from values import val
from matplotlib import pyplot as plt

from phys import traj

# Displays the trajectories
def sim():
    points = traj(val)

    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.axis('equal')
    ax.plot3D(points[0][0], points[0][1], points[0][2], color='orange')
    ax.scatter(points[0][0][0], points[0][1][0], points[0][2][0], c = 'orange')
    ax.plot3D(points[1][0], points[1][1], points[1][2], color='green')
    for i in range(2, len(points)):
        ax.plot3D(points[i][0], points[i][1], points[i][2])

    return fig