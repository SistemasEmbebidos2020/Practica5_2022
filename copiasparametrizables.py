from robodk.robolink import *  # RoboDK API
from robodk.robomath import *

from time import sleep
RDK = Robolink()

robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT)
if not robot.Valid():
    quit()
reference = robot.Parent()
robot.setPoseFrame(reference)
cubo = RDK.Item("box")
def box_calc(size_xyz, pallet_xyz):
    [size_x, size_y, size_z] = size_xyz
    [pallet_x, pallet_y, pallet_z] = pallet_xyz
    xyz_list = []
    for h in range(int(pallet_z)):
        for j in range(int(pallet_y)):
            for i in range(int(pallet_x)):
                xyz_list = xyz_list + [[(i+0.5)*size_x, (j+0.5)*size_y, (h+0.5)*size_z]]
    return xyz_list

def parts_setup(positions, size_xyz):    #positions = xyz_list
    [size_x, size_y, size_z] = size_xyz
    nparts = len(positions)
    cstep = 1.0/(nparts - 1)
    for i in range(nparts):
        newpart = RDK.Paste()  #pega el nuevo objeto con referencia la estacion
        newpart.Scale([size_x/100, size_y/100, size_z/100]) #escala el objeto  (100mm cube)
        newpart.setName('Part ' + str(i+1)) #cambia de nombre al nuevo objeto
        newpart.setPose(transl(positions[i])) #cambia posicion con respecto a su padre
        newpart.setVisible(True, False) #pone visible al objeto pero invisible a su referencia
        newpart.Recolor([1-cstep*i, cstep*i, 0.2, 1]) #cambia de color al objeto en valores RGBA
    return 2

xyzsize = [200,130,50]
xyzpallet = [2,3,5]
cubo.Copy()
xyz = box_calc(xyzsize,xyzpallet)
parts_setup(xyz,xyzsize)
