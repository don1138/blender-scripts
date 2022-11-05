import bpy

for obj in bpy.context.selected_objects:
    obj.material_slots[0].link = 'OBJECT'