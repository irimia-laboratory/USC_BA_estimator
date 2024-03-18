import numpy as np
import os
from scipy.ndimage import zoom


def downsample(brain):
    # downsamples the brain scan to fit neural network
    # brain: a single brain scan of size 256, 256, 256
    # returns a single brain scan of size 128, 128, 128
       
    brain = zoom(brain, (0.5, 0.5, 0.5))
    #brain = np.expand_dims(brain, axis=0)
    return brain
