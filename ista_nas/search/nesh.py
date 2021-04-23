import torch
import numpy as np
import torch.nn as nn


def nesh_step(Acc,normal_index,reduce_index):
    normals = torch.Tensor(np.array([[0,5,0.4,0.1],[0.6,0.2,0.2],[0.3,0.5,0.2],[0.1,0.9,0.0]]))
    reduces = torch.Tensor(np.array([[0,5,0.4,0.1],[0.6,0.2,0.2],[0.3,0.5,0.2],[0.1,0.9,0.0]]))
    return normals,reduces