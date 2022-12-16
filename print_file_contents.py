import bpy

print("# IMAGES")
for i in bpy.data.images:
    print(i.name)

print("")

print("# COLLECTIONS")
for i in bpy.data.collections:
    print(i.name)

print("")

print("# MATERIALS")
for i in bpy.data.materials:
    print(i.name)

print("")

print("# NODE GROUPS")
for i in bpy.data.node_groups:
    print(i.name)

print("")

print("# OBJECTS")
for i in bpy.data.objects:
    print(i.name)

print("")

print("# WORLDS")
for i in bpy.data.worlds:
    print(i.name)

print("")
