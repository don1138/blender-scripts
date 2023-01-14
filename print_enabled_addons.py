#PRINT LIST OF NAMES

#import bpy

#for addon in bpy.context.preferences.addons:
#    print(addon.module)


#PRINT LIST OF NAMES AS ARRAY

#print(bpy.context.preferences.addons.keys())


#PRINT LIST FROM BL_INFO

import bpy
import sys
import re

context = bpy.context

for mod_name in context.preferences.addons.keys():
    mod = sys.modules[mod_name]
    name = mod.bl_info.get('name')
    cat = mod.bl_info.get('category')
    vers = mod.bl_info.get('version')
    print(f"{cat} > {name}\n{mod}")

    # Parse 'mod' to get key names
#    qlist = re.findall("\'(.*?)\'",str(mod))
#    qval = qlist[0]
#    print(f"'{qval}',")
