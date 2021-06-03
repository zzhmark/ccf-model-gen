import os
import numpy as np
import nrrd
from mayavi import mlab
import json


def reconstruction(metadata, anno_data, root, output_dir, background):
    path = os.path.join(output_dir, str(metadata[root]['id']) + '.obj')
    if metadata[root]['children']:
        anno = background.copy()
        for i in metadata[root]['children']:
            anno = anno | reconstruction(metadata, anno_data, str(i), output_dir, background)
        draw3d(anno, path)
    else:
        anno = anno_data == int(root)
        draw3d(anno, path)
    print(root + ' completed.')
    return anno


def draw3d(data, path):
    mlab.contour3d(data.astype(np.int32), line_width=8)
    mlab.savefig(path)
    mlab.clf()


def main(image_path, metadata_path, output_dir):
    anno_data, anno_header = nrrd.read(image_path)
    with open(metadata_path) as f:
        metadata = json.load(f)
    reconstruction(metadata, anno_data, '375', output_dir, anno_data < 0)


if __name__ == '__main__':
    main('../input/annotation_25.nrrd', '../input/Mouse.json', '../output/obj')



