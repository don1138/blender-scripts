# ENABLE/DISABLE ADD-ONS

import bpy

# 1.) Get array of active add-ons:
# print(bpy.context.preferences.addons.keys())

# 2.) Copy the output from teminal and past to replace the array below:
modules = [
    'add_mesh_extra_objects',
    'amaranth',
    'cycles',
    'io_mesh_ply',
    'io_mesh_stl',
    'io_scene_fbx',
    'io_scene_gltf2',
    'io_scene_obj',
    'io_vector',
    'mesh_f2',
    'mesh_looptools',
    'mesh_tiny_cad',
    'mesh_tools',
    'node_wrangler',
]

# 3.) Run this script to enable (or disable) the addons listed in "modules" array
message = ""
for m in modules:
    try:
        bpy.ops.preferences.addon_enable(module=m)
        # bpy.ops.preferences.addon_disable(module=m)
    except:
        message = message + m + ", "
        continue
