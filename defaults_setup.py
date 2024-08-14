from re import T
import bpy

# Scene Settings Here
# RENDER
# COLOR MANAGEMENT
bpy.context.scene.render.engine = 'CYCLES'
bpy.context.scene.cycles.feature_set = 'EXPERIMENTAL'
bpy.context.scene.cycles.device = 'CPU'
bpy.context.scene.view_settings.view_transform = 'Filmic'
bpy.context.scene.view_settings.look = 'High Contrast'
# LIGHT PATHS
bpy.context.scene.cycles.max_bounces = 6
bpy.context.scene.cycles.diffuse_bounces = 2
bpy.context.scene.cycles.glossy_bounces = 2
bpy.context.scene.cycles.transmission_bounces = 6
bpy.context.scene.cycles.volume_bounces = 0
bpy.context.scene.cycles.transparent_max_bounces = 2
bpy.context.scene.cycles.caustics_reflective = False
bpy.context.scene.cycles.caustics_refractive = False
# PERFORMANCE
bpy.context.scene.cycles.use_auto_tile = False
bpy.context.scene.cycles.debug_use_spatial_splits = True
bpy.context.scene.render.use_persistent_data = True
# SAMPLING
# bpy.context.scene.cycles.preview_adaptive_threshold = 0.2
bpy.context.scene.cycles.preview_samples = 16
# bpy.context.scene.cycles.adaptive_threshold = 0.05
bpy.context.scene.cycles.samples = 64
bpy.context.scene.cycles.use_preview_denoising = False
bpy.context.scene.cycles.use_denoising = False
# OUTPUT
# FORMAT
bpy.context.scene.render.resolution_x = 1080
bpy.context.scene.render.resolution_y = 1080
bpy.context.scene.render.resolution_percentage = 50
bpy.context.scene.render.pixel_aspect_x = 1
bpy.context.scene.render.use_border = True
# OUTPUT
bpy.context.scene.render.filepath = "//"
bpy.context.scene.render.image_settings.file_format = 'PNG'
bpy.context.scene.render.image_settings.color_mode = 'RGB'
bpy.context.scene.render.image_settings.color_depth = '16'
# FRAME RANGE
bpy.context.scene.frame_end = 1
# SCENE
# UNITS
bpy.context.scene.unit_settings.length_unit = 'MILLIMETERS'
bpy.context.scene.render.film_transparent = True


# PREFERENCES
# INTERFACE
bpy.context.preferences.view.ui_scale=1.25
bpy.context.preferences.view.show_splash=False
bpy.context.preferences.view.show_developer_ui=True
bpy.context.preferences.view.show_tooltips=True
bpy.context.preferences.view.show_tooltips_python=True
bpy.context.preferences.view.show_navigate_ui=False
bpy.context.preferences.view.color_picker_type='SQUARE_SV'
bpy.context.preferences.view.header_align='TOP'
bpy.context.preferences.view.render_display_type='NONE'
bpy.context.preferences.view.show_statusbar_memory=False
bpy.context.preferences.view.show_statusbar_stats=False
bpy.context.preferences.view.show_statusbar_version=False
bpy.context.preferences.view.use_text_antialiasing=False
# THEMES
bpy.context.preferences.themes['Default'].view_3d.vertex_size=8
bpy.context.preferences.themes['Default'].view_3d.face_back[0]=1.0
bpy.context.preferences.themes['Default'].view_3d.face_back[1]=0.250980406999588
bpy.context.preferences.themes['Default'].view_3d.face_back[2]=0.250980406999588
bpy.context.preferences.themes['Default'].view_3d.face_back[3]=0.3333333432674408
bpy.context.preferences.themes['Default'].view_3d.view_overlay[0]=0.0
bpy.context.preferences.themes['Default'].view_3d.view_overlay[1]=1.0
bpy.context.preferences.themes['Default'].view_3d.view_overlay[2]=1.0
bpy.context.preferences.themes['Default'].node_editor.noodle_curving=0

# VIEWPORT
bpy.context.preferences.view.show_object_info=True
bpy.context.preferences.view.show_view_name=True
bpy.context.preferences.view.show_playback_fps=True
bpy.context.preferences.view.mini_axis_type='MINIMAL'
# EDITING
bpy.context.preferences.edit.material_link='OBJECT'
bpy.context.preferences.edit.node_margin=0
# ANIMATION
bpy.context.preferences.edit.keyframe_new_interpolation_type='LINEAR'
# NAVIGATION
bpy.context.preferences.inputs.use_rotate_around_active=False
bpy.context.preferences.inputs.use_auto_perspective=True
bpy.context.preferences.inputs.use_mouse_depth_navigate=False
bpy.context.preferences.view.smooth_view=0
bpy.context.preferences.view.rotation_angle=5
# SYSTEM
bpy.context.preferences.edit.undo_steps=128
# SAVE & LOAD
bpy.context.preferences.filepaths.use_relative_paths=False
bpy.context.preferences.filepaths.use_file_compression=True
bpy.context.preferences.filepaths.use_load_ui=True
bpy.context.preferences.filepaths.use_tabs_as_spaces=True
bpy.context.preferences.filepaths.use_scripts_auto_execute=False
bpy.context.preferences.filepaths.save_version=0
bpy.context.preferences.filepaths.recent_files=20
bpy.context.preferences.filepaths.use_auto_save_temporary_files=False
bpy.context.preferences.filepaths.show_recent_locations=True
bpy.context.preferences.filepaths.show_system_bookmarks=True
bpy.context.preferences.filepaths.use_filter_files=True
bpy.context.preferences.filepaths.show_hidden_files_datablocks=False
# FILE PATHS
bpy.context.preferences.filepaths.font_directory='PATH_TO/Fonts/'
bpy.context.preferences.filepaths.texture_directory='PATH_TO/Materials/'
bpy.context.preferences.filepaths.script_directory='PATH_TO/Scripts/'
bpy.context.preferences.filepaths.render_output_directory='//'
bpy.context.preferences.filepaths.render_cache_directory='//'

# Add a list of asset libraries to add here
asset_libraries = [
    "/Users/USER_NAME/Documents/Blender/Assets/Blender Materials",
    "/Users/USER_NAME/Documents/Blender/Assets/Community",
    "/Users/USER_NAME/Documents/Blender/Assets/QMM",
    "/Users/USER_NAME/Documents/Blender/Assets/B3DMatPack1,2",
    "/Users/USER_NAME/Documents/Blender/Assets/Matlib VX",
    "/Users/USER_NAME/Documents/Blender/Assets/MetaAndrocto",
    "/Users/USER_NAME/Documents/Blender/Assets/B4A",
    "/Users/USER_NAME/Documents/Blender/Assets/Generators",
    "/Users/USER_NAME/Documents/Blender/Assets/PSA",
    "/Users/USER_NAME/Documents/Blender/Assets/Sanctus",
    "/Users/USER_NAME/Library/Application Support/Blender/3.3/scripts/addons/Bagapie",
    "/Users/USER_NAME/Documents/Blender/Assets/Poly Haven"
]

# bpy.context.preferences.addons['cycles'].preferences.compute_device_type = "OPTIX" # ('NONE', 'CUDA', 'OPTIX', 'HIP', 'ONEAPI')
# for device in  bpy.context.preferences.addons['cycles'].preferences.devices:
#     device.use = True

# bpy.context.preferences.inputs.ui_scale=1.0
# bpy.context.preferences.inputs.use_zoom_to_mouse=True
# bpy.context.preferences.inputs.use_numeric_input_advanced=True
# bpy.context.preferences.view.show_splash=True

#Set Workspace Area Defaults

for screen in bpy.data.screens:
    for area in screen.areas:
        if area.type == "VIEW_3D":
            for space in area.spaces:
                space.show_gizmo = False


for i in bpy.data.screens['Layout'].areas:
    if i.type == "VIEW_3D":
        for j in i.spaces:
            j.shading.show_cavity = True
            j.overlay.show_stats = True

for i in bpy.data.screens['Modeling'].areas:
    if i.type == "VIEW_3D":
        for j in i.spaces:
            j.shading.show_cavity = True
            j.shading.cavity_type = 'BOTH'
            j.shading.cavity_ridge_factor = 0.225
            j.shading.cavity_valley_factor = 0.475
            j.shading.curvature_ridge_factor = 0.691
            j.shading.curvature_valley_factor = 0.745
            j.overlay.show_stats = False

# Addons to Enable
modules = [
    'BackfaceHiding',
    'Boxcutter',
    'EdgeFlow',
    'Fast-Loop-master',
    'HOps',
    'Light_luminous_intensity',
    'MACHIN3tools',
    'MESHmachine',
    'Modifier Shortcut Keys',
    'NodePreview',
    'Real Camera',
    'SwitchUnits',
    'TexTools_1_5',
    'UvSquares-master',
    'add_curve_extra_objects',
    'add_mesh_BoltFactory',
    'add_mesh_extra_objects',
    'amaranth',
    'asset_browser_utilities',
    'attach_align',
    'bend_face',
    'blender-qle',
    'blender-qmc-plus',
    'blender-qmm',
    'cad_mesh_dimensions',
    'camera_overlays',
    'connect_face',
    'cut_corner',
    'cycles',
    'drop_it',
    'face_cutter',
    'forgotten_tools',
    'gridmodeler',
    'io_curve_svg',
    'io_import_images_as_planes',
    'io_mesh_ply',
    'io_mesh_stl',
    'io_mesh_uv_layout',
    'io_scene_fbx',
    'io_scene_gltf2',
    'io_scene_obj',
    'kekit',
    'kitops',
    'kitops-toggle-display',
    'magic_uv',
    'math_formula',
    'mesh_copier',
    'mesh_f2',
    'mesh_hidesato_offset_edges-041',
    'mesh_looptools',
    'mesh_origin_to_selected',
    'mesh_tiny_cad',
    'mesh_tools',
    'node_arrange',
    'node_counter_stats',
    'node_image_texture_properties',
    'node_wrangler',
    'object_boolean_tools',
    'object_print3d_utils',
    'quad_swords_bisect',
    'quick_bridge',
    'resize_nodes',
    'safe_ngon',
    'select_sim',
    'shaderswitcheraddon',
    'simple-tabs',
    'simple_renaming_panel',
    'space_view3d_modifier_tools_mod',
    'sun_position',
    'thumbMate',
]

# Default Setup
##Delete Everything
# bpy.ops.object.select_all(action='SELECT')
# bpy.ops.object.delete(use_global=False)

##Add New Camera Straigt on and X rotation locked
# bpy.ops.object.camera_add(enter_editmode=False, location=(0, -6, 1.6764), rotation=(1.57079632679,0, 0), scale=(1, 1, 1))
##Deselect All
# bpy.ops.object.select_all(action='DESELECT')

#Change to Layout Screen
bpy.context.window.workspace = bpy.data.workspaces['Layout']

###############################################################################
#
# DO NOT EDIT BELOW HERE
#
###############################################################################

for lib in asset_libraries:
    bpy.ops.preferences.asset_library_add(directory=lib)

message = ""
for m in modules:
    try:
        bpy.ops.preferences.addon_enable(module=m)
    except:
        message = message + m + ", "
        continue

def draw(self, context):
    self.layout.label(text=message)

if message != "":
    bpy.context.window_manager.popup_menu(draw, title="Not Installed", icon='INFO')

bpy.ops.text.unlink()




# bpy.ops.wm.save_homefile()
# bpy.ops.wm.save_userpref()
