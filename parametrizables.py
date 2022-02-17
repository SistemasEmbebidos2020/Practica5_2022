from robolink import *    # RoboDK API 
from robodk import *      # Robot toolbox 
from time import*
RDK = Robolink() 
 
robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT)    #adquirir todos los parámetros d el robot 
if not robot.Valid(): 
    quit() 


def elipse(): 
    frameletras = RDK.Item("FrameLetras") 
    robot.setPoseFrame(frameletras)
    Ref1 = RDK.Item("Letras") 
    RefTar = Ref1.Pose()    
    a=20     
    b=10 
    RDK.RunProgram('WeldOn(-1)')     
    robot.MoveJ(RefTar*roty(pi))
    robot.setSpeed(2050,2000)    
    while (t <=3*pi/2):         
        pos = RefTar*transl(a*cos(t),b*sin(t), 0)*roty(pi)
        robot.MoveJ(pos)    
        if (t==-pi/2):
            RDK.RunProgram('WeldOn')          
            sleep(2)      
        t +=pi/360 
 
elipse() 
RDK.RunProgram('WeldOn(0)') 
