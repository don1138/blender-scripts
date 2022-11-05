import bpy
import numpy
n = 512
scale = 1
golden_angle = numpy.pi * (3 - numpy.sqrt(5))
theta = golden_angle * numpy.arange(n)
z = numpy.linspace(1 - 1.0 / n, 1.0 / n - 1, n)
#z = numpy.zeros(n)
radius = numpy.sqrt(1 - z * z) * scale

points = numpy.zeros((n, 3))
points[:,0] = radius * numpy.cos(theta)
points[:,1] = radius * numpy.sin(theta)
points[:,2] = z * scale

import bpy
import bmesh
from math import radians
context = bpy.context
scene = context.scene
vl = context.view_layer

bm = bmesh.new()

meshdata = bpy.data.meshes.new("goldie")
verts = [bm.verts.new(p) for p in points]
"make vert normals point out"
for v in verts:
    v.normal = -v.co.normalized()
#bmesh.ops.convex_hull(bm, input=verts)
bm.to_mesh(meshdata)
goldie = bpy.data.objects.new("goldie", meshdata)   
scene.collection.objects.link(goldie)
vl.objects.active = goldie
goldie.select_set(True)
#make a dupe
#bpy.ops.mesh.primitive_cone_add(location=(0,0,0))
#plane = vl.objects.active
#plane.hide = True
#plane.scale *= 32 / n
#plane.rotation_euler = (radians(90), 0, 0)
#bpy.ops.object.transform_apply(scale=True, rotation=True)
#plane.parent = goldie
#goldie.dupli_type = 'VERTS'
#goldie.use_dupli_vertices_rotation = True
