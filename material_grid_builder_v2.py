import bpy
import math

# User Variables
factor = 5     # Number of Columns & Rows
offset = 0.4    # 40cm Between Object Centers

# Counter Variables
count = 1
row = 1
col = 1

# Calculations
camera_scale = factor * 0.4
scale_pos = (factor-1)*0.2
scale_neg = scale_pos * -1
loc_x = scale_neg
loc_y = scale_pos

bpys = bpy.context.scene

# Set Camera Orthographic Scale
bpy.data.cameras["Camera"].ortho_scale = camera_scale

# Create New Collection
#new_collection = bpy.data.collections.new("New Materials")
#bpys.collection.children.link(new_collection)

# Get Collection
collection = bpy.data.collections.get("Materials")

# Material List Header
print("\nLIST OF MATERIAL(S)\n=================\n")

# Get List of Collections
def find_collection(context, item):
    collections = item.users_collection
    return collections[0] if len(collections) > 0 else context.scene.collection

for mat in bpy.data.materials:

    # Create Instance of Mannequin Object from Linked Mesh
    mesh = bpy.data.meshes["Manq"]
    obj = bpy.data.objects.new(mat.name, mesh)

    # Give Each Mannequin Instance a Unique Material
    obj.material_slots[0].link = 'OBJECT'
    obj.active_material = mat

    # Add Object to Collection
    bpys.collection.objects.link(obj)
    old_collection = find_collection(bpy.context, obj)
    collection.objects.link(obj)
    old_collection.objects.unlink(obj)

    # Position Objects in a Grid
    obj.location = (round(loc_x,1), round(loc_y,1), 0.0)
    if loc_x < scale_pos - 0.1:
        loc_x += offset
    else:
        loc_x = scale_neg
        loc_y -= offset

    # Strip Underscores from Name
#    mat_name = obj.active_material.name
#    find_it = "_"
#    repl_it = " "
#    mat_name = mat_name.replace(find_it, repl_it)

    # Make Name Title Case
#    obj.name = mat_name.title()
#    obj.active_material.name = mat_name.title()

    # Print Material Name
    print("Row", row, "Col", col, "—", obj.active_material.name)
#    print(round(loc_x,1), round(loc_y,1), "\n")

    # Increment Row/Column Count
    count = count+1
    row = int(math.ceil(count/factor))
    if col < factor:
        col = col+1
    else:
        col = 1
        print("")


# Material List Footer
if col == 1:
    print("=================")
else:
    print("\n=================")
print(count-1, "MATERIAL(S)\n")
