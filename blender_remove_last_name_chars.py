import bpy
objects = bpy.context.selected_objects
num_chars = 3
for o in objects:
    o.name = o.name[:-num_chars]