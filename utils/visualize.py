import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

def plot3Views(vols, slice1=64):
    # plots all 3 veiws at slice1 for the variable vols
    # brains should be a list of 3D volumes or 4D volume, 
    #and titles should be a list of text with figure captions
    volsShape = np.shape(vols)
        
    fig = plt.figure(figsize=(volsShape[0] * 5, 20))
    gs1 = gridspec.GridSpec(volsShape[0], 3)
    
    for idx, vol in enumerate(vols):
        #plt.figure()
        plt.subplot(volsShape[0], 3, 3*idx +1)
        plt.imshow((vol[:,slice1,:]))
        plt.axis("off")
        plt.subplot(volsShape[0], 3, 3*idx +2)
        plt.imshow((vol[slice1,:,:]))
        plt.axis("off")
        plt.subplot(volsShape[0], 3, 3*idx +3)
        plt.imshow((vol[:,:,slice1]))
        plt.axis("off")
        fig.subplots_adjust(wspace=0, hspace=0)
        #plt.show()
    gs1.update(wspace=0.005, hspace=0.05) # set the spacing between axes. 
    
    return None
    