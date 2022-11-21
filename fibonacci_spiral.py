import bpy
import bmesh
import math

n = 1024 # number of points
c = 0.1 # scale factor

mesh = bpy.data.meshes.new(name='Spiral 2')
bm = bmesh.new()

for i in range(n):
    theta = i * math.radians(137.5)
    r = c * math.sqrt(i)
    bm.verts.new((math.cos(theta) * r, math.sin(theta) * r, 0.0))

bm.to_mesh(mesh)
mesh.update()

from bpy_extras import object_utils
object_utils.object_data_add(bpy.context, mesh)
