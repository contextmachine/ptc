import open3d as o3d

import numpy as np

from utils import search

names = list(search('ply_transformed/', prefix='.ply'))
clouds = o3d.geometry.PointCloud()
print(names)
for name in names:
    ptc = o3d.io.read_point_cloud('/Users/andrewastakhov/ptc_processiing/ply_transformed/' + name + '.ply')
    print(ptc)
    clouds += ptc
o3d.io.write_point_cloud("cloud.ply", clouds)
o3d.visualization.draw_geometries([clouds])
