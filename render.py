import bpy

# Render frames 1 to 90
for step in range(1, 91):

    bpy.context.scene.frame_set(step)

    # Render the current open scene
    bpy.context.scene.render.filepath = 'PATH_NAME/frame_%d.png' % step

    # Choose which scene to render
    # bpy.data.scenes["Scene"].render.filepath = 'PATH_NAME/frame_%d.png' % step

    bpy.ops.render.render(write_still=True)

print("Done")
