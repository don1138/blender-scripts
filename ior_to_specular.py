import bpy

IOR = 2
Specular = pow(( ( IOR - 1 ) / ( IOR + 1 ) ), 2) / 0.08
print(Specular)