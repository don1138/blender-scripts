import bpy

# Render frames 1 to 90
for step in range(1, 91):

    bpy.context.scene.frame_set(step)
    bpy.data.scene.render.filepath = 'PATH_NAME/frame_%d.png' % step
    bpy.ops.render.render(write_still=True)
