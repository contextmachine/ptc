import unittest
import numpy as np
from ptctools import convert
import open3d as o3d


class MyTestCase(unittest.TestCase):

    def test_e57read_points(self):
        search_path = 'data'
        save_path = 'results'
        check_path = 'ply'
        name = 'a'
        geoms = convert(name, path=search_path, save_path=save_path, vox_size=0.3)
        ptc = o3d.io.read_point_cloud(check_path + '/' + name + '.ply')
        self.assertTrue(np.all(np.allclose(np.asarray(ptc.points), np.asarray(geoms.points))))


if __name__ == '__main__':
    unittest.main()
