#https://developer.blender.org/diffusion/B/browse/master/release/scripts/modules/addon_utils.py
#https://blender.stackexchange.com/questions/32409/how-to-enable-and-disable-add-ons-via-python

#import bpy
#import addon_utils

#addon_utils.enable("cad_mesh_dimensions")
#addon_utils.disable("CAD Mesh Dimensions")
#addon_utils.disable_all()

#for addon in bpy.context.preferences.addons:
#    print(addon.module)
#    print(addon.bl_idname)
#    addon_utils.enable(addon)
#    addon_utils.disable(addon)

#PRINT LIST OF NAMES AS ARRAY

#print(bpy.context.preferences.addons.keys())

#PRINT LIST FROM BL_INFO

import bpy
import sys

context = bpy.context

for mod_name in context.preferences.addons.keys():
    mod = sys.modules[mod_name]
    name = mod.bl_info.get('name')
    cat = mod.bl_info.get('category')
    vers = mod.bl_info.get('version')
    print(cat + " > " + name)
