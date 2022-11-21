import bpy
objects = bpy.context.selected_objects
base_name = "new_name"
for (i,o) in enumerate(objects):
    o.name = "{}_{:03d}".format(base_name, i)
