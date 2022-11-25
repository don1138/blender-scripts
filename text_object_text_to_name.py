# Only works on one text object at a time
# If multiple text objects selected, only first object name is used

import bpy

objects = bpy.context.selected_objects

for o in objects:
    bpy.ops.object.editmode_toggle()
    bpy.ops.font.select_all()
    bpy.ops.font.text_copy()
    n = bpy.context.window_manager.clipboard
    bpy.ops.object.editmode_toggle()
    o.name = o.data.name = f"{n} label"
