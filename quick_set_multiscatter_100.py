# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####


bl_info = {
    "name"       : "QSM (Quick Set Multiscatter)",
    "description": "Sets Principled BDSF Distribution to Multiscatter GGX",
    "author"     : "Don Schnitzius",
    "version"    : (1, 0, 0),
    "blender"    : (4, 00, 0),
    "location"   : "3D Viewport > Sidebar > MAT > Quick Set Mutliscatter",
    "warning"    : "",
    "doc_url"    : "https://github.com/don1138/blender-set-multiscatter",
    "support"    : "COMMUNITY",
    "category"   : "Material"
}


import bpy


# MESSAGE BOX
no_bsdf = "No Principled BSDF Shader Found"
no_glass = "No Glass Shader Found"
no_glossy = "No Glossy Shader Found"
no_material = "No Compatable Material Found"
no_need = "Distribution is already Multiscaller GGX"
no_node = "No Compatable Nodes Found"


# SHADERS WITH DISTRIBUTION INPUTS
node_bl_idnames = {
    "ShaderNodeBsdfAnisotropic",
    "ShaderNodeBsdfGlass",
    "ShaderNodeBsdfPrincipled",
}


def ShowMessageBox(message="", title="", icon='INFO'):
    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


class SetAll(bpy.types.Operator):
    """Set Glass, Glossy, and Principled BDSF Distribution to Multiscatter GGX"""
    bl_label = "Set All"
    bl_idname = 'mat.set_all'

    def execute(self, context):
        set_all(self, context)
        return {'FINISHED'}


def set_all(self, context):
    if material := bpy.context.object.active_material:
        AN = material.node_tree.nodes
        found_nodes = False
        for n in AN:
            if n.bl_idname in node_bl_idnames:
                if n.distribution != 'MULTI_GGX':
                    n.distribution = 'MULTI_GGX'
                else:
                    ShowMessageBox(no_need, "Already Set")                    
                found_nodes = True
        if not found_nodes:
            ShowMessageBox(no_node, "Unable To Comply")
    else:
        ShowMessageBox(no_material, "Unable To Comply")
    return {'FINISHED'}


class SetPrincipledBDSF(bpy.types.Operator):
    """Set Principled BDSF Distribution to Multiscatter GGX"""
    bl_label = "Set Principled BDSF"
    bl_idname = 'mat.set_bsdf'

    def execute(self, context):
        set_bdsf(self, context)
        return {'FINISHED'}


def set_bdsf(self, context):
    if material := bpy.context.object.active_material:
        AN = material.node_tree.nodes
        found_principled_bsdf = False
        for n in AN:
            if isinstance(n, bpy.types.ShaderNodeBsdfPrincipled):
                if n.distribution != 'MULTI_GGX':
                    n.distribution = 'MULTI_GGX'
                else:
                    ShowMessageBox(no_need, "Already Set")                    
                found_principled_bsdf = True
        if not found_principled_bsdf:
            ShowMessageBox(no_bsdf, "Unable To Comply")
    else:
        ShowMessageBox(no_node, "Unable To Comply")
    return {'FINISHED'}
  

class SetPrincipledGlass(bpy.types.Operator):
    """Set Glass Distribution to Multiscatter GGX"""
    bl_label = "Set Glass"
    bl_idname = 'mat.set_glass'

    def execute(self, context):
        set_glass(self, context)
        return {'FINISHED'}


def set_glass(self, context):
    if material := bpy.context.object.active_material:
        AN = material.node_tree.nodes
        found_glass = False
        for n in AN:
            if isinstance(n, bpy.types.ShaderNodeBsdfGlass):
                if n.distribution != 'MULTI_GGX':
                    n.distribution = 'MULTI_GGX'
                else:
                    ShowMessageBox(no_need, "Already Set")                    
                found_glass = True
        if not found_glass:
            ShowMessageBox(no_glass, "Unable To Comply")
    else:
        ShowMessageBox(no_material, "Unable To Comply")
    return {'FINISHED'}


class SetPrincipledGlossy(bpy.types.Operator):
    """Set Glossy Distribution to Multiscatter GGX"""
    bl_label = "Set Glossy"
    bl_idname = 'mat.set_glossy'

    def execute(self, context):
        set_glossy(self, context)
        return {'FINISHED'}


def set_glossy(self, context):
    if material := bpy.context.object.active_material:
        AN = material.node_tree.nodes
        found_glossy = False
        for n in AN:
            if isinstance(n, bpy.types.ShaderNodeBsdfAnisotropic):
                if n.distribution != 'MULTI_GGX':
                    n.distribution = 'MULTI_GGX'
                else:
                    ShowMessageBox(no_need, "Already Set")                    
                found_glossy = True
        if not found_glossy:
            ShowMessageBox(no_glossy, "Unable To Comply")
    else:
        ShowMessageBox(no_material, "Unable To Comply")
    return {'FINISHED'}


# PARENT PANEL
class QSMPanel(bpy.types.Panel):
    bl_idname = "QSM_PT_Panel"
    bl_label = "Quick Set Multiscatter"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MAT"
    # bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        layout = self.layout

        srow = layout.row()
        srow.scale_y = 1.25
        srow.operator("mat.set_all", text="Set All")

        srow = layout.row()
        srow.scale_y = 1.25
        srow.operator("mat.set_bsdf", text="Set Principled BDSF")

        srow = layout.row()
        srow.scale_y = 1.25
        srow.operator("mat.set_glass", text="Set Glass")

        srow = layout.row()
        srow.scale_y = 1.25
        srow.operator("mat.set_glossy", text="Set Glossy")


# IMPORT CLASSES
classes = [
    QSMPanel,
    SetAll,
    SetPrincipledBDSF,
    SetPrincipledGlass,
    SetPrincipledGlossy,
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    # The path of this blend file (if saved)
    __file__ = bpy.data.filepath
    register()
