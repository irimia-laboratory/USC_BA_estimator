import nibabel.freesurfer.mghformat as mgh
from utils.preprocess import downsample
import numpy as np
import os

def dataLoader(filePaths):
	# retrieves, downsamples and creates a numpy array given a list of file paths to freesurfer processed brain.mgz
    # filePaths: a list of filePaths
    # returns a numpy array with brain scans of size 128, 128, 128
    
    brains = []
	
    for idx, mgzPath in enumerate(filePaths):    
        if not os.path.exists(mgzPath):
            print("Could not find:", mgzPath)
            continue
        
        # load mgz file
        mghFile = mgh.load(mgzPath)
        mghFileD = mghFile.get_fdata()
        
        #append to a list
        brains.append(downsample(mghFileD))
        
    brains = np.asarray(brains)
    
    return brains
	
	