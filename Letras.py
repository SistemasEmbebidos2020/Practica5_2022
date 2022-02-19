from robodk.robolink import *  # RoboDK API
from robodk.robomath import *
from time import sleep
RDK = Robolink()

robot = RDK.Item('',ITEM_TYPE_ROBOT)
if not robot.Valid():
    quit()
reference = robot.Parent()
robot.setPoseFrame(reference)
frameletras = RDK.Item("FrameLetras")
robot.setPoseFrame(frameletras)
reftar = RDK.Item("Letras").Pose()

def letraA():
    k=10
    A00 = transl(0       ,0        , 0  ) 
    A0 = transl(5*k       ,10*k         , 0  ) 
    A1 = transl(10*k     , 0          , 0  ) 
    A2 = transl(10*k     , 0          , 20*k) 
    A3 = transl(1.95*k  , 3.68*k     , 20*k) 
    A4 = transl(1.95*k  , 3.68*k     , 0) 
    A5 = transl(8.10*k  , 3.68*k     , 0) 
    A6 = transl(8.10*k  , 3.68*k     , 20*k)
    A = [A00,A0, A1, A2, A3, A4, A5, A6]
    robot.setSpeed(50,20)
    RDK.RunProgram('WeldOn(-1)')
    sleep(1)
    robot.MoveJ(A[0]*roty(-pi))
    RDK.RunProgram('WeldOn(1)')
    sleep(1)
    for i in range(2):
        robot.MoveL(A[i+1]*roty(-pi))
    RDK.RunProgram('WeldOn(0)')
    sleep(1)
    for i in range(3):
        robot.MoveJ(A[i+3]*rotx(-pi))
    RDK.RunProgram('WeldOn(1)')
    sleep(1)
    robot.MoveJ(A[6]*rotx(-pi))
    RDK.RunProgram('WeldOn(0)')
    sleep(1)
    robot.MoveJ(A[7]*rotx(-pi))
letraA()
