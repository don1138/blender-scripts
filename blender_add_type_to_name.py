import bpy
objects = bpy.context.selected_objects
for i, o in enumerate(objects):
     o.name = "{}_{}".format(o.type, o.name)