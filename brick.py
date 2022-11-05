import bpy

brick = bpy.ops.mesh.primitive_cube_add(size=2.0, location=(0.0, 0.0, 0.0), scale=(0.096837, 0.046037, 0.028575))
bpy.context.active_object.name = "Brick"
bpy.context.active_object.data.name = "Brick"
bpy.context.object.location[2] = 0.028575
bpy.ops.object.transform_apply(location=True, rotation=False, scale=True)
bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='MEDIAN')
