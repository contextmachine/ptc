import sys
import typing

import numpy as np
import open3d as o3d
import pye57
import os
import time

from open3d.cpu.pybind.geometry import KDTreeSearchParamKNN

import utils
import logging, syslog


def convert(name, path, save_path='ply', write=True, **kwargs):
    prefix = path
    s = time.time()
    ptcm = o3d.geometry.PointCloud()

    for ptc in merge(pye57.E57(prefix + "/" + name + ".e57", 'r'), **kwargs):
        ptcm += ptc
    if write:
        o3d.io.write_point_cloud(save_path + "/" + name + '.ply', ptcm)
    else:
        pass
    e = time.time() - s
    s, m = divmod(e, 60)
    print(f'\n\nSucsess. time: {s} min {m} sec')
    return ptcm


def multi_read(search_path='data', voxel_size=0.05, **kwargs) -> typing.List[o3d.geometry.PointCloud]:
    names = list(utils.search(search_path, prefix='e57'))
    print(names)
    geoms = []
    invalid = []
    for i, name in enumerate(names):
        try:
            print(f'\n\n[{i}] {name} :\n')
            pcd = convert(name, path=search_path, **kwargs)

            geoms.append(pcd)
        except:
            invalid.append((name, sys.exc_info()))

    if len(invalid) > 0:
        for k, v in invalid:
            print(f'Invalid case: {k}\nTrace: {v}')

    return geoms




def merge(scan, vox_size=0.05, knn=30):

    for i in utils.progressbar(range(scan.scan_count), "computing", 40):

        n = scan.read_scan_raw(i)
        ptci = o3d.geometry.PointCloud()

        if 'cartesianX' in n.keys():
            n = scan.read_scan(i, colors=True, transform=False, ignore_missing_fields=True)
            na = np.stack((n['cartesianX'], n['cartesianY'], n['cartesianZ']), axis=-1) + np.asarray(
                scan.get_header(i).translation)
            ptci.points = o3d.utility.Vector3dVector(na)
        else:
            try:

                n = scan.read_scan(i, colors=True, ignore_missing_fields=True)
            except:
                n = scan.read_scan(i, colors=True, transform=False, ignore_missing_fields=True)
            na = np.stack((n['cartesianX'], n['cartesianY'], n['cartesianZ']), axis=-1)
            ptci.points = o3d.utility.Vector3dVector(na)

        if 'colorRed' in n.keys():
            cols = np.stack([n['colorRed'], n['colorGreen'], n['colorBlue']], axis=-1) * (1 / 255)
            ptci.colors = o3d.utility.Vector3dVector(cols)

        else:
            pass

        #prefix.cout = "down sampling"


        dptci = ptci.random_down_sample(0.7)

        #prefix.cout = "estimate normals"
        dptci.estimate_normals(KDTreeSearchParamKNN(knn))

        yield dptci
