import bpy

def main(operator, context):
    node_selected = context.selected_nodes

    if node_selected:
        bpy.ops.node.hide_socket_toggle()
    else:
        operator.report({'ERROR'}, "Nothing selected")
        return

class NODE_OT_Operator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "node.simple_operator"
    bl_label = "Hide Node Sockets Operator"

    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR'

    def execute(self, context):
        main(self, context)
        return {'FINISHED'}

def register():
    bpy.utils.register_class(NODE_OT_Operator)

def unregister():
    bpy.utils.unregister_class(NODE_OT_Operator)

if __name__ == "__main__":
    register()