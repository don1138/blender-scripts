# Create X number of directories
# Same name for parent and child directories

# python create_weekly_folders.py

# import bpy
import os

# Run in assigned directory
parent_dir = 'DIRECTORY_PATH/_2023_cards/'
os.mkdir(parent_dir)
# Run in current directory
#directory_path = os.getcwd()
#parent_dir = os.path.basename(directory_path)
sub_d2 = "SOURCES"

for start_week in range(1, 53):
    _dir = f"2023-wk{start_week}"
    sub_dir_1 = parent_dir + _dir
    sub_dir_2 = f'{sub_dir_1}/{_dir}'

    f_week = os.path.join(parent_dir, _dir)
    f_renders = os.path.join(sub_dir_1, _dir)
    f_sources = os.path.join(sub_dir_1, sub_d2)

    os.mkdir(f_week)
    os.mkdir(f_renders)
    os.mkdir(f_sources)
