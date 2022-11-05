import bpy

from mathutils import Vector
from math import radians, sin, cos, tan, sqrt, floor

context = bpy.context

def loxodrome_points(spirals, revs, angle_step=10):
    a = 1 / spirals
    degs = floor(360 * revs / 2)
    segs = [radians(d) for d in range(-degs, degs, angle_step)]
    points = []
    for t in segs:
        den = sqrt(1 + a * a * t * t)
        x = cos(t) / den
        y = sin(t) / den
        z = - a * t / den
        l = Vector((x, y, z))
        points.append(l)     
    return points

ang = 20
spirals = 16
revs = 64
points = loxodrome_points(spirals, revs, angle_step=ang)
# quick n dirty
lazy = 360 // ang

import bmesh
bm = bmesh.new()

loxodata = bpy.data.meshes.new("loxo")
verts = [bm.verts.new(p) for p in points]
faces = [[i, i+1, i+lazy, i+lazy-1] for i in range(len(points)-lazy-1)]
for f in faces:
    bm.faces.new([verts[i] for i in f])
bm.to_mesh(loxodata)
loxodrome = bpy.data.objects.new("Loxodrome", loxodata)    
context.scene.collection.objects.link(loxodrome)
