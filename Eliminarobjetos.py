from robodk.robolink import *  # RoboDK API
from robodk.robomath import *
RDK = Robolink()

def cleanup(objects, startswith="Part "):
    """Deletes all objects where the name starts with "startswith", from the provided list of objects."""    
    for item in objects:
        if item.Name().startswith(startswith):
            item.Delete()

all_objects = RDK.ItemList(ITEM_TYPE_OBJECT, False)

for item in all_objects:
    print("todos ",item.Name())

for item in all_objects:
    if item.Name().startswith("Part "):
        print("seleccionados", item.Name())
cleanup(all_objects, 'Part ')
