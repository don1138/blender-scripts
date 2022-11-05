# Create X number of directories
# Same name for parent and child directories

import bpy
import os

# Run in assigned directory
parent_dir = '/Users/Don/Desktop/TEST/'
# Run in current directory
#directory_path = os.getcwd()
#parent_dir = os.path.basename(directory_path)
start_week = 35
sub_d2 = "SOURCES"

while start_week <= 52:
    _dir = "2022-wk" + str(start_week)
    sub_dir_1 = parent_dir + _dir
    sub_dir_2 = sub_dir_1 + '/' + _dir

    path = os.path.join(parent_dir, _dir)
    path_1 = os.path.join(sub_dir_1, _dir)
    path_2 = os.path.join(sub_dir_2, sub_d2)

    os.mkdir(path)
    os.mkdir(path_1)
    os.mkdir(path_2)

    start_week += 1
