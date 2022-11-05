# https://github.com/BillG18/Snap-Match/

import bpy

"""Prototype for color matching functions."""
import colorsys


def RGB255(RGB):
    """Help function to convert RGB to 255 scale."""
    return [round((RGB[0]*255), 2),
            round((RGB[1]*255), 2),
            round((RGB[2]*255), 2)]


def complementary(R, G, B):
    """Calculate complementery color from RGB values (0-255)."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS = [((HLS[0] + 0.5) % 1), HLS[1], HLS[2]]
    RGB = colorsys.hls_to_rgb(HLS[0], HLS[1], HLS[2])
    return RGB255(RGB)


def analagous(R, G, B):
    """Calculate analagous colors, returns 2 colors."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS_1 = [((((HLS[0]*360) + 30) % 360)/360), HLS[1], HLS[2]]
    HLS_2 = [((((HLS[0]*360) - 30) % 360)/360), HLS[1], HLS[2]]
    RGB_1 = colorsys.hls_to_rgb(HLS_1[0], HLS_1[1], HLS_1[2])
    RGB_2 = colorsys.hls_to_rgb(HLS_2[0], HLS_2[1], HLS_2[2])
    return [RGB255(RGB_1), RGB255(RGB_2)]


def triadic(R, G, B):
    """Calculate triadic colors, returns 2 colors."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS_1 = [((((HLS[0]*360) + 120) % 360)/360), HLS[1], HLS[2]]
    HLS_2 = [((((HLS[0]*360) - 120) % 360)/360), HLS[1], HLS[2]]
    RGB_1 = colorsys.hls_to_rgb(HLS_1[0], HLS_1[1], HLS_1[2])
    RGB_2 = colorsys.hls_to_rgb(HLS_2[0], HLS_2[1], HLS_2[2])
    return [RGB255(RGB_1), RGB255(RGB_2)]


def split_complementary(R, G, B):
    """Calculate split-complementary colors, returns 2 colors."""
    RGB = [(R/255), (G/255), (B/255)]
    HLS = colorsys.rgb_to_hls(RGB[0], RGB[1], RGB[2])
    HLS = [((HLS[0] + 0.5) % 1), HLS[1], HLS[2]]
    RGB = colorsys.hls_to_rgb(HLS[0], HLS[1], HLS[2])
    HLS_1 = [((((HLS[0]*360) + 30) % 360)/360), HLS[1], HLS[2]]
    HLS_2 = [((((HLS[0]*360) - 30) % 360)/360), HLS[1], HLS[2]]
    RGB_1 = colorsys.hls_to_rgb(HLS_1[0], HLS_1[1], HLS_1[2])
    RGB_2 = colorsys.hls_to_rgb(HLS_2[0], HLS_2[1], HLS_2[2])
    return [RGB255(RGB_1), RGB255(RGB_2)]


if __name__ == '__main__':
    print(complementary(97, 157, 10))
    print(analagous(97, 157, 10))
    print(triadic(97, 157, 10))
    print(split_complementary(97, 157, 10))
