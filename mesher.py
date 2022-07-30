from sys import stderr

import open3d as o3d
from CGAL.CGAL_Point_set_3 import Point_set_3
from CGAL.CGAL_Polyhedron_3 import Polyhedron_3

from utils import search
import numpy as np
from  CGAL.CGAL_Advancing_front_surface_reconstruction import advancing_front_surface_reconstruction

def compare(a, b):
    np.concatenate((np.asarray(a.points), np.asarray(b.points)))
    np.asarray(a.colors)
    np.asarray(a.normals)

def cgl():
    points = Point_set_3("/Users/andrewastakhov/ptc_processiing/ply_transformed/" + "arc" + ".ply")
    if points.empty():
        stderr.write("Error: cannot read file ../data/oni.xyz\n")
        exit()

    P = Polyhedron_3()

    advancing_front_surface_reconstruction(points, P)


    P.write_to_file("oni.ply")
def main():
    #advancing_front_surface_reconstruction()
    ptc = o3d.io.read_point_cloud("/Users/andrewastakhov/ptc_processiing/ply_transformed/" + "arc" + ".ply")
    n = np.asarray(ptc.points) * 1e-3
    ptc.points = o3d.utility.Vector3dVector(n)

    # o3d.io.write_point_cloud("/Users/andrewastakhov/ptc_processiing/compared.ply", ptcs)
    print("down")
    ptce=ptc.voxel_down_sample(0.1)
    ptce.estimate_normals()
    o3d.io.write_point_cloud("/Users/andrewastakhov/ptc_processiing/compared.ply", ptce)
    print("norms")

    radii = [0.8]
    print("meshing")
    rec_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(ptce, o3d.utility.DoubleVector([0.1, 0.3]))
    o3d.io.write_triangle_mesh(f"/Users/andrewastakhov/ptc_processiing/mesh/arc.ply", rec_mesh)
    #rec_mesh.compute_vertex_normals()
    print("laplac")
    mesh_out = rec_mesh.filter_smooth_laplacian(10)
    print('filter with average with 1 iteration')
    o3d.io.write_triangle_mesh(f"/Users/andrewastakhov/ptc_processiing/mesh/arc2.ply", mesh_out)

    return mesh_out


if __name__ == "__main__":
    mesh_out = main()
    #o3d.visualization.draw_geometries([mesh_out])
