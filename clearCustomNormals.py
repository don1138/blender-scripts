import bpy

selection = bpy.context.selected_objects

#Clear custom normal data
for geo in selection:
        bpy.context.view_layer.objects.active = geo
        if geo.type == 'MESH': #Only do this for meshes
            bpy.ops.mesh.customdata_custom_splitnormals_clear()
