import bpy
from pathlib import Path

folder = Path("path/to/your/folder")
blend_files = [f for f in folder.glob("*.blend") if f.is_file()]

# Append all materials from all blends within the folder
for filepath in blend_files:
    with bpy.data.libraries.load(filepath, link=False) as (data_from, data_to):
        data_to.materials = data_from.materials
