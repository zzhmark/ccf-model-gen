from mayavi import mlab
import numpy as np
import voxelfuse as vf


def draw3d_mayavi(data, color, path):
    mlab.contour3d(data.astype(np.int32), line_width=.0001, color=color, transparent=True, opacity=.3)
    mlab.savefig(path)
    mlab.clf()


def draw3d_vf(data, path):
    model = vf.VoxelModel(data)
    mesh = vf.Mesh.fromVoxelModel(model)
    # mesh = mesh.setResolution()
    mesh.export(path)