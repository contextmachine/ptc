import cmd
cmd.Cmd("conda activate open3d")
import open3d as o3d


from ptctools import multi_read





def load_ptc(path):
    return o3d.io.read_point_cloud(path)


def main(data_path='data', save_path='ply',write=False):
    invalids = []
    ptcs = []
    mr=multi_read(search_path=data_path,write=write)


    for g in mr:
        try:
            print(+1)
            ptcs.append(g.voxel_down)
        except:
            print(0)
            invalids.append(g)
    print(2)
    o3d.io.write_point_cloud(ptcs, save_path+"/"+"res.ply")
    """
    o3d.visualization.draw(ptcs,
                           bg_color=(0.2, 0.2, 0.2, 1),
                           show_skybox=False, show_ui=True,
                           point_size=1,
                           rpc_interface=True)"""
    return ptcs


if __name__ == "__main__":
    import argparse
    """
    ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    
    """
    parser = argparse.ArgumentParser(description='A test program.')

    parser.add_argument("-p", "--data_path", help="Set path to e57 data folder.", type=str, default='data')
    parser.add_argument("-s", "--save_path", help="Set folder path to save .ply .", type=str, default='ply')
    parser.add_argument("-v", "--voxel_size", help="enter a value for pre-compression", type=float, default=0.05)
    parser.add_argument("-w", "--write_parts", help="write parts from file", type=bool, default=False)

    args = parser.parse_args()

    main( data_path=args.data_path, save_path=args.save_path, write=args.write_parts)
