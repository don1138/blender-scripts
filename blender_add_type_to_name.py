import bpy
objects = bpy.context.selected_objects
for o in objects:
    o.name = f"{o.type}_{o.name}"
