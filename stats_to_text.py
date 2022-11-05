import bpy

c1 = bpy.context.window_manager.clipboard = str(bpy.context.scene.statistics(bpy.context.view_layer))
c1.encode("utf8")
c2 = c1.replace(",", "")
bpy.context.window_manager.clipboard = c2
bpy.ops.text.new()
bpy.ops.text.paste()