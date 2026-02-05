# Importar bibliotecas necesarias
from robodk.robolink import *  # API de RoboDK
from robodk.robomath import *
import time

# Establecer conexión con RoboDK
RDK = Robolink()

# Seleccionar el robot y su referencia
robot = RDK.ItemUserPick('', ITEM_TYPE_ROBOT)
if not robot.Valid():
    quit()
reference = robot.Parent()
robot.setPoseFrame(reference)

# Obtener el cubo para copiarlo
cubo = RDK.Item("box")

# Función para calcular las posiciones de los objetos en la caja
def box_calc(size_xyz, pallet_xyz):
    # Descomponer las listas de tamaño y posición del paletizado
    [size_x, size_y, size_z] = size_xyz
    [pallet_x, pallet_y, pallet_z] = pallet_xyz

    # Inicializar lista vacía para almacenar las posiciones
    xyz_list = []

    # Iterar sobre el volumen del paletizado y calcular la posición de cada objeto
    for h in range(int(pallet_z)):
        for j in range(int(pallet_y)):
            for i in range(int(pallet_x)):
                # Calcular la posición del objeto actual
                xyz_list.append([(i + 0.5) * size_x, (j + 0.5) * size_y, (h + 0.5) * size_z])

    return xyz_list

# Función para configurar las partes en el paletizado
def parts_setup(positions, size_xyz):
    # Descomponer la lista de tamaño del objeto
    [size_x, size_y, size_z] = size_xyz

    # Calcular el número de objetos y el paso de escala
    nparts = len(positions)
    cstep = 1.0 / (nparts - 1)

    # Iterar sobre los objetos y configurarlos
    for i in range(nparts):
        # Crear un nuevo objeto con referencia a la estación
        newpart = RDK.Paste()
        newpart.Scale([size_x / 100, size_y / 100, size_z / 100])  # Escala el objeto (100mm cube)
        newpart.setName('Part ' + str(i + 1))  # Cambiar de nombre al nuevo objeto
        newpart.setPose(transl(positions[i]))  # Cambiar posición con respecto a su padre
        newpart.setVisible(True, False)  # Poner visible al objeto pero invisible a su referencia
        newpart.Recolor([1 - cstep * i, cstep * i, 0.2, 1])  # Cambiar de color al objeto en valores RGBA

    return 2

# Tamaño del objeto y paletizado
xyzsize = [200, 130, 50]
xyzpallet = [2, 3, 5]

# Copiar el cubo
cubo.Copy()

# Calcular las posiciones de los objetos en la caja
xyz = box_calc(xyzsize, xyzpallet)

# Configurar las partes en el paletizado
parts_setup(xyz, xyzsize)
