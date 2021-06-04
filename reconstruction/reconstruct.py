import os
import nrrd
from drawing import *
import json


def reconstruction(metadata, anno_data, root, output_dir, background, alg):
    path = os.path.join(output_dir, str(metadata[root]['id']) + '.obj')
    h = metadata[root]['color'].lstrip('#')
    color = tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))
    anno = anno_data == int(root)
    if metadata[root]['children']:
        for i in metadata[root]['children']:
            anno = anno | reconstruction(metadata, anno_data, str(i), output_dir, background, alg)
    if alg == 'mayavi':
        draw3d_mayavi(anno, color, path)
    elif alg == 'vf':
        draw3d_vf(anno, path)
    print(root + ' completed.')
    return anno


def main(image_path, metadata_path, start, output_dir, alg):
    anno_data, anno_header = nrrd.read(image_path)
    with open(metadata_path) as f:
        metadata = json.load(f)
    reconstruction(metadata, anno_data, start, output_dir, anno_data < 0, alg)


if __name__ == '__main__':
    main('../input/annotation_10.nrrd', '../input/Mouse.json', '10704', '../output/stl', 'vf')
