import json

import open3d as o3d
from utils import search, progressbar
from ptctools import multi_read
import os, sys
import numpy as np


def main():
    newdir = f"ply_transformed"
    try:
        os.mkdir(newdir)
    except:
        pass

    with open('transforms.json') as f:
        transform = json.load(f)
    if not (transform['name'] == "pt_cloud"):
        raise Exception(f"Применен неверный объект трансвормации: {transform['name']}")
    else:

        matrix = np.asarray(transform['matrix'])
        render_ = []
        for name in search(path="ply", prefix="ply"):
            print(name)
            ptc = o3d.io.read_point_cloud("ply/" + name + '.ply')
            print(ptc)

            cols = np.asarray(ptc.colors)
            nptc = np.asarray(ptc.points)

            n = nptc - np.array([[1000, 1000, 0]])
            d = n * 1000

            ptc2 = o3d.geometry.PointCloud()
            ptc2.points = o3d.utility.Vector3dVector(d)
            ptc2.colors = o3d.utility.Vector3dVector(cols)
            print("normals")
            ptc2.estimate_normals()
            print("normals done")
            ptc2.normalize_normals()
            render_.append(ptc2)
            o3d.io.write_point_cloud("/Users/andrewastakhov/ptc_processiing/ply_transformed/" + name + ".ply", ptc2)
            print("files write")
            print(f"{name} Success! ")
        o3d.visualization.draw_geometries([render_])


if __name__ == "__main__":
    main()
