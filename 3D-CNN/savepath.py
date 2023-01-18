
import numpy as np
import os 

def filename_brainnpy(path_of_mgz, time_split):
   
    dic = {}
    dic['Jan'] = ['01']
    dic['Feb'] = ['02']
    dic['Mar'] = ['03']
    dic['Apr'] = ['04']
    dic['May'] = ['05']
    dic['Jun'] = ['06']
    dic['Jul'] = ['07']
    dic['Aug'] = ['08']
    dic['Sep'] = ['09']
    dic['Oct'] = ['10']
    dic['Nov'] = ['11']
    dic['Dec'] = ['12']
    brain_save_path = os.path.join(path_of_mgz, 'brains_' + time_split[4] + '-' + str(dic[str(time_split[1])][0]) +
                               '-' +time_split[2] +'_'+time_split[3].split(":")[0] + '-' +
                              time_split[3].split(":")[1] + '-' + time_split[3].split(":")[2] + '.npy')
    return brain_save_path
    
def filename_pred(path_of_mgz, time_split):
   
    dic = {}
    dic['Jan'] = ['01']
    dic['Feb'] = ['02']
    dic['Mar'] = ['03']
    dic['Apr'] = ['04']
    dic['May'] = ['05']
    dic['Jun'] = ['06']
    dic['Jul'] = ['07']
    dic['Aug'] = ['08']
    dic['Sep'] = ['09']
    dic['Oct'] = ['10']
    dic['Nov'] = ['11']
    dic['Dec'] = ['12']
    brain_save_path_1 = os.path.join(path_of_mgz, 'BA_' + time_split[4] + '-' + str(dic[str(time_split[1])][0]) +
                               '-' +time_split[2] +'_'+time_split[3].split(":")[0] + '-' +
                              time_split[3].split(":")[1] + '-' + time_split[3].split(":")[2] + '.npy')
    brain_save_path_2 = os.path.join(path_of_mgz, 'BA_' + time_split[4] + '-' + str(dic[str(time_split[1])][0]) +
                               '-' +time_split[2] +'_'+time_split[3].split(":")[0] + '-' +
                              time_split[3].split(":")[1] + '-' + time_split[3].split(":")[2] + '.csv')                          
    return brain_save_path_1, brain_save_path_2
    
# if __name__ == '__main__':
#     tmp = time.ctime().split(" ")
#     data = filename(tmp)
    #return 0