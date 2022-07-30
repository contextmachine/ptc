
import open3d as o3d


from ptctools import multi_read


def load_ptc(path):
    return o3d.io.read_point_cloud(path)


def main(data_path='data', save_path='ply', voxel_size=0.005, render_size=0.01):
    invalids = []
    ptcs = []
    mr=multi_read(search_path=data_path, vox_size=voxel_size, save_path=save_path, voxel_size=voxel_size)
    if render_size==voxel_size:
        ptcs = mr
    else:
        for g in mr:
            try:
                g.voxel_down_sample(render_size)
                ptcs.append(g.voxel_down)
            except:
                invalids.append(g)

    o3d.visualization.draw(ptcs,
                           bg_color=(0.2, 0.2, 0.2, 1),
                           show_skybox=False, show_ui=True,
                           point_size=1,
                           rpc_interface=True)
    return ptcs


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='A test program.')

    parser.add_argument("-p", "--data_path", help="Set path to e57 data folder.", type=str, default='data')
    parser.add_argument("-s", "--save_path", help="Set folder path to save .ply .", type=str, default='ply')
    parser.add_argument("-v", "--voxel_size", help="enter a value for pre-compression", type=float, default=0.05)
    parser.add_argument("-r", "--render_size", help="enter a down sample value for render", type=float, default=0.1)

    args = parser.parse_args()

    main(render_size=args.render_size, data_path=args.data_path, save_path=args.save_path, voxel_size=args.voxel_size)
