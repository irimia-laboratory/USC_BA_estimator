
import numpy as np
import os 

def repadding(saliency_map_list, coordinates):
   
    repadded_saliency_maps=[]
    for i in range(len(saliency_map_list)):
      buf=saliency_map_list[i]
      co=coordinates[i]
      x=int(co[0])
      y=int(co[1])
      z=int(co[2])
      buf=np.pad(buf, ((x-41,128-(x+41)), (y-43,128-(y+43)), (z-50,128-(z+50))), 'constant')#82x86x100 x is the center of 82; y 
      repadded_saliency_maps.append(buf)
    repadded_saliency_maps = np.asarray(repadded_saliency_maps)
                              
    return repadded_saliency_maps

    
# if __name__ == '__main__':
#     tmp = time.ctime().split(" ")
#     data = filename(tmp)
    #return 0