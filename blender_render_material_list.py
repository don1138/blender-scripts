import bpy

fileMaterials = bpy.data.materials
print(len(fileMaterials))
renderMaterials = []
for material in fileMaterials:
	if material.name[:4] == 'mtl_':
		renderMaterials.append(material)
		print('Added: '.format(material.name))

scene = bpy.context.scene
renderFolder = scene.render.filepath
obj = bpy.context.active_object
for material in renderMaterials:
	obj.data.materials[0] = material
	print('Mat: '.format(material.name))
	scene.render.filepath = renderFolder + (material.name) + '.'
	bpy.ops.render.render(animation = False,write_still = True)

scene.render.filepath = renderFolder