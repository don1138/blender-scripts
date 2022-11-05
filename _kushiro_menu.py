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
# Created by Don Schnitzius


# FOR ALL KUSHIRO ADD_ONS:
# 1. OPEN __init__.py
# 2. FIND "VIEW3D_MT_edit_mesh_context_menu"
# 3. REPLACE WITH "VIEW3D_MT_kushiro_menu"
# 4. SAVE

# LOAD ORDER MATTERS!!!
# TO GET THIS ADD-ON TO WORK PROPERLY:
# 1. DISABLE ALL KUSHIRO ADD-ONS
# 2. ENABLE THIS ADD-ON
# 3. RE-ENABLE ALL KUSHIRO ADD-ONS


import bpy


bl_info = {
    "name": "Kushiro Menu",
    "description": "Collect Kushiro Context Select Add-Ons into Sub Menu",
    "author": "Don Schnitzius",
    "version": (1, 0, 0),
    "blender": (2, 83, 0),
    "location": "View3D > Edit > Context Menu (right click)",
    "category": "3D View",
}


class VIEW3D_MT_kushiro_menu(bpy.types.Menu):
    bl_label = 'Kushiro'

    def draw(self, context):
        layout = self.layout


def menu_func(self, context):
    self.layout.separator()
    self.layout.menu("VIEW3D_MT_kushiro_menu")
    self.layout.separator()


def register():
    bpy.utils.register_class(VIEW3D_MT_kushiro_menu)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func)


def unregister():
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func)
    bpy.utils.unregister_class(VIEW3D_MT_kushiro_menu)


if __name__ == "__main__":
    register()
