from robolink import *    # RoboDK API 
from robodk import *      # Robot toolbox 
from time import sleep
RDK = Robolink() 
rob = robodk 
 
robot = RDK.ItemUserPick('',ITEM_TYPE_ROBOT)    #adquirir todos los parámetros d el robot 
if not robot.Valid(): 
    quit() 
reference = robot.Parent()  # devuelve el artículo robot.setPoseFrame(reference)#establece el marco de referencia de un robot pose_ref=robot.Pose()  #devuelve la posición actual del robot con matriz 
 
def elipse(): 
    Ref1 = RDK.Item("Letras",ITEM_TYPE_TARGET) 
    RefTar = Ref1.Pose() 
    b1 = rob.pose_2_xyzrpw(RefTar)     
    t = -pi/2     
    x0= b1[0]     
    y0= b1[1]     
    z0= b1[2]     
    a=20     
    b=10 
    RDK.RunProgram('WeldOn(-1)')     
    robot.MoveJ(RefTar*roty(-pi))
    robot.setSpeed(2050,2000)    
    while (t <=3*pi/2):         
        pos = transl(x0 + a*cos(t), y0 + b*sin(t), z0)*roty(-pi)         
        robot.MoveJ(pos)    
        if (t==-pi/2):       
            sleep(2) 
            RDK.RunProgram('WeldOn')        
        t +=pi/360 
 
elipse() 
RDK.RunProgram('WeldOn(0)') 
