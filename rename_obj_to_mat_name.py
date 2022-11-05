import bpy

for obj in bpy.context.selected_objects:
    
    mat_name = obj.active_material.name
    obj.name = mat_name
