import bpy

for obj in bpy.context.selected_objects:
    
    mat_name = obj.active_material.name
    find_it = "Or "
    repl_it = "OR "
    mat_name = mat_name.replace(find_it, repl_it)
    obj.active_material.name = mat_name
    print(mat_name)
