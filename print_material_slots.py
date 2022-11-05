#https://docs.blender.org/api/3.1/bpy.types.bpy_prop_collection.html

import bpy

matslots = bpy.context.object.material_slots
matslots_type = type(matslots)
matslots_keys = matslots.keys()
matslots_items = matslots.items()
matslots_values = matslots.values()

print("matslots =",matslots)
print("\nmatslots_type =",matslots_type)
print("\nmatslots_keys =",matslots_keys)
print("\nmatslots_items =",matslots_items)
print("\nmatslots_values =",matslots_values)
print("\n")
