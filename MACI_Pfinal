# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project

# Forward and backwards compatible use of the RoboDK API:
# Remove these 2 lines to follow python programming guidelines
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox
# Link to RoboDK
RDK = Robolink()

robot = RDK.Item("KUKA KR 10 R1100 sixx")
targref = RDK.Item("refTar")
def box_calc(size_xyz, pallet_xyz):
    """Calculates a list of points to store parts in a pallet"""
    [size_x, size_y, size_z] = size_xyz
    [pallet_x, pallet_y, pallet_z] = pallet_xyz    
    xyz_list = []
    for h in range(int(pallet_z)):
        for j in range(int(pallet_y)):
            for i in range(int(pallet_x)):
                xyz_list = xyz_list + [[(i+0.5)*size_x, (j+0.5)*size_y, -(h+0.5)*size_z]]
    return xyz_list

def square(lado = 50):
    robot.MoveL(targref.Pose()*transl(lado))
    robot.MoveL(targref.Pose()*transl(0,lado))
    robot.MoveL(targref.Pose()*transl(-lado))
    robot.MoveL(targref.Pose()*transl(0,-lado))
    robot.MoveL(targref.Pose()*transl(lado))
    robot.MoveJ(targref.Pose()*transl(0,0,-100))

def canonica(radio1 = 50,radio2 = 50,x1 = 0,y1 = 0):
    r1=radio1
    r2=radio2
    theta = -pi/2
    while (theta <=3*pi/2):
        x = x1 + r1*cos(theta)
        y = y1 + r2*sin(theta)
        pos = targref.Pose()*transl(x,y,0)
        robot.MoveJ(pos)
        theta +=pi/50
    robot.MoveJ(targref.Pose()*transl(0,0,-100))

posiciones = box_calc([100,50,80],[3,5,2])

print(posiciones)

"""
for i in range(len(posiciones)):
    robot.MoveJ(targref.Pose()*transl(posiciones[i]))
"""

#square()
#canonica(25,25)
