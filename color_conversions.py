# Color Conversion Using mathutils.Color()

import bpy
import mathutils


col_src = bpy.data.materials["Material"].diffuse_color
colr = col_src[0]
colg = col_src[1]
colb = col_src[2]
col_array = [colr,colg,colb]
col = mathutils.Color(col_array)


def srgb_to_linearrgb(c):
    if   c < 0:       return 0
    elif c < 0.04045: return c/12.92
    else:             return ((c+0.055)/1.055)**2.4

def hex_to_rgb(h,alpha=1):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)] + [alpha])

def hex_to_rgb_sm(h):
    r = (h & 0xff0000) >> 16
    g = (h & 0x00ff00) >> 8
    b = (h & 0x0000ff)
    return tuple([srgb_to_linearrgb(c/0xff) for c in (r,g,b)])


# https://www.cyril-richon.com/blog/2019/1/23/python-srgb-to-linear-linear-to-srgb

def srgb2lin(s):
    if s <= 0.0404482362771082:
        lin = s / 12.92
    else:
        lin = pow(((s + 0.055) / 1.055), 2.4)
    return lin

def lin2srgb(lin):
    if lin > 0.0031308:
        s = 1.055 * (pow(lin, (1.0 / 2.4))) - 0.055
    else:
        s = 12.92 * lin
    return s


# https://developerfacts.com/answer/214359-converting-hex-color-to-rgb-and-vice-versa

def hex_to_rgb(value):
    """Return (red, green, blue) for the color given as #rrggbb."""
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def rgb_to_hex(red, green, blue):
    """Return color as #rrggbb for the given color values."""
    return '#%02x%02x%02x' % (red, green, blue)

hex_to_rgb("#ffffff")           #==> (255, 255, 255)
hex_to_rgb("#ffffffffffff")     #==> (65535, 65535, 65535)
rgb_to_hex(255, 255, 255)       #==> '#ffffff'
rgb_to_hex(65535, 65535, 65535) #==> '#ffffffffffff'


# MINE

def srbg_to_hex(v):
    r = lin2srgb(v[0]) * 255
    g = lin2srgb(v[1]) * 255
    b = lin2srgb(v[2]) * 255
    hex = r,g,b
    return hex

def srbg_to_hex_int(v):
    r = int(lin2srgb(v[0]) * 255)
    g = int(lin2srgb(v[1]) * 255)
    b = int(lin2srgb(v[2]) * 255)
    hex = r,g,b
    return hex


print(f"\nColor R:   {colr} {col.r}")
print(f"Color G:   {colg} {col.g}")
print(f"Color B:   {colb} {col.b}")
print(f"Color RGB: {col}")

print(f"\nColor H:   {col.h}")
print(f"Color S:   {col.s}")
print(f"Color V:   {col.v}")
print(f"Color HSV: {col.hsv}")

print("\nLINEAR UNCORRECTED")
print("Color:       %d, %d, %d" % (col * 255.0)[:])
print("Hexadecimal: %.2x%.2x%.2x" % (int(col.r * 255), int(col.g * 255), int(col.b * 255)))

print("\nLINEAR TO SRGB CORRECTED")
print("Color:       %d, %d, %d" % (srbg_to_hex(col)[:]))
print("Hexadecimal: %.2x%.2x%.2x" % (srbg_to_hex_int(col)[:]))
print("Hexadecimal: #%x%x%x" % (srbg_to_hex_int(col)[:]))

# print("%x" % 255)


#    Color R:    0.38132569193840027 0.38132569193840027
#    Color G:    0.6172063946723938 0.6172063946723938
#    Color B:    0.04091537371277809 0.04091537371277809
#    Color RGB: <Color (r=0.3813, g=0.6172, b=0.0409)>

#    Color H:    0.23488472402095795
#    Color S:    0.9337087869644165
#    Color V:    0.6172063946723938
#    Color HSV: (0.23488472402095795, 0.9337087869644165, 0.6172063946723938)

#    LINEAR UNCORRECTED
#    Color:       97, 157, 10
#    Hexadecimal: 619d0a

#    LINEAR TO SRGB CORRECTED
#    Color:       165, 205, 57
#    Hexadecimal: a5cd39
#    Hexadecimal: a5cd39
#    ff



# as well as r/g/b attribute access you can adjust them by h/s/v
#col.s *= 0.5

# you can access its components by attribute or index
#print("Color R:", col.r)
#print("Color G:", col[1])
#print("Color B:", col[-1])
#print("Color HSV: %.2f, %.2f, %.2f", col[:])

# components of an existing color can be set
#col[:] = 0.0, 0.5, 1.0

# components of an existing color can use slice notation to get a tuple
#print("Values: %f, %f, %f" % col[:])

# colors can be added and subtracted
#col += mathutils.Color((0.25, 0.0, 0.0))

# Color can be multiplied, in this example color is scaled to 0-255
# can printed as integers
#print("Color: %d, %d, %d" % (col * 255.0)[:])

# This example prints the color as hexadecimal
#print("Hexadecimal: %.2x%.2x%.2x" % (int(col.r * 255), int(col.g * 255), int(col.b * 255)))

#    Formatting

#    d 	for integers (doesn't round up or down, just ignores the decimal numbers)
#    f 	for floating point numbers
#    b 	for binary numbers
#    o 	for octal numbers
#    x 	for octal hexadecimal numbers
#    s 	for string
#    e 	for floating point in exponent format
#
#    %f    1.000000
#    %.1f  1.0
#    %.2f  1.00
#    %d    1
