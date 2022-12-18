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
  "name"        : "Quick Switch Units",
  "description" : "Change Measurement Units",
  "author"      : "don1138",
  "version"     : (1, 0, 1),
  "blender"     : (3, 0, 0),
  "location"    : "3D Viewport > Sidebar > View > Switch Units",
  "warning"     : "",
  "doc_url"     : "https://github.com/don1138/blender-scripts",
  "tracker_url" : "",
  "support"     : "COMMUNITY",
  "category"    : "3D View"
}


import bpy


unit_values = [
    {'meters':      ['METRIC', 'METERS', 1, False, 0.1, 1000, .001]},
    {'centimeters': ['METRIC', 'CENTIMETERS', .01, False, 0.1, 1000, .001]},
    {'millimeters': ['METRIC', 'MILLIMETERS', .001, False, 0.1, 1000, .0001]},
    {'feet':        ['IMPERIAL', 'FEET', 1, True, 0.01905, 304.8, .001]},
    {'inches':      ['IMPERIAL', 'INCHES', 1, False, 0.00079375, 254, 0.001]},
]


def set_all_units(units):
    uv_dict = unit_values[units]
    unit_key = list(uv_dict.keys())[0]
    unit_value = uv_dict[unit_key]
    us = bpy.context.scene.unit_settings
    us.system = unit_value[0]
    us.length_unit = unit_value[1]
    us.scale_length = unit_value[2]
    us.use_separate = unit_value[3]
    for _ in bpy.data.screens:
        for a in bpy.context.screen.areas:
            if a.type == 'VIEW_3D':
                for s in a.spaces:
                    if s.type == 'VIEW_3D':
                        s.clip_start = unit_value[4]
                        s.clip_end = unit_value[5]
                        s.overlay.grid_scale = unit_value[6]


class SwitchUnitsMeter(bpy.types.Operator):
    """Switch Units to Meters"""
    bl_label = "M"
    bl_idname = 'view.su_meters'

    def execute(self, context):
        set_all_units(0)
        return {'FINISHED'}


class SwitchUnitsCentimeter(bpy.types.Operator):
    """Switch Units to Centimeters"""
    bl_label = "Cm"
    bl_idname = 'view.su_centimeters'

    def execute(self, context):
        set_all_units(1)
        return {'FINISHED'}


class SwitchUnitsMillimeter(bpy.types.Operator):
    """Switch Units to Millimeters"""
    bl_label = "Mm"
    bl_idname = 'view.su_millimeters'

    def execute(self, context):
        set_all_units(2)
        return {'FINISHED'}


class SwitchUnitsFeet(bpy.types.Operator):
    """Switch Units to Feet"""
    bl_label = "Ft"
    bl_idname = 'view.su_feet'

    def execute(self, context):
        set_all_units(3)
        return {'FINISHED'}


class SwitchUnitsInches(bpy.types.Operator):
    """Switch Units to Inches"""
    bl_label = "In"
    bl_idname = 'view.su_inches'

    def execute(self, context):
        set_all_units(4)
        return {'FINISHED'}


class SwitchUnitsPanel(bpy.types.Panel):
    """Creates Switch Units Panel 3D View > Sidebar > View"""
    bl_label = "Switch Units"
    bl_idname = "SCENE_PT_layout"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "View"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.operator("view.su_meters")
        row.operator("view.su_centimeters")
        row.operator("view.su_millimeters")
        row.operator("view.su_feet")
        row.operator("view.su_inches")


classes = [
    SwitchUnitsMeter,
    SwitchUnitsCentimeter,
    SwitchUnitsMillimeter,
    SwitchUnitsFeet,
    SwitchUnitsInches,
    SwitchUnitsPanel
]


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
