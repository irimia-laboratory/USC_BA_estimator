
import numpy as np
import os
from datetime import datetime
def filename_brainnpy(path_of_mgz):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    date_time = date_time.split(", ")
    month, day, year = date_time[0].split("/")
    brain_save_path = os.path.join(path_of_mgz, 'brains_' + year + '-' + month + '-' + day + '-' + date_time[1] + '.npy')
    coordinates_save_path = os.path.join(path_of_mgz, 'coordinates_' + year + '-' + month + '-' + day + '-' + date_time[1] + '.npy')
    coordinates_save_path_csv = os.path.join(path_of_mgz, 'coordinates_' + 'brains_' + year + '-' + month + '-' + day + '-' + date_time[1] + '.csv')
    return brain_save_path, coordinates_save_path, coordinates_save_path_csv

def filename_pred(path_of_mgz):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    date_time = date_time.split(", ")
    month, day, year = date_time[0].split("/")
    brain_save_path_csv = os.path.join(path_of_mgz, 'BA_' + year + '-' + month + '-' + day + '-' + date_time[1] + '.csv')
    return brain_save_path_csv

def filename_smap(path_of_mgz):
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    date_time = date_time.split(", ")
    month, day, year = date_time[0].split("/")
    brain_smap_save_path = os.path.join(path_of_mgz, 'Saliency_maps_' + year + '-' + month + '-' + day + '-' + date_time[1] + '.npy')
    return brain_smap_save_path

# if __name__ == '__main__':
#     tmp = time.ctime().split(" ")
#     data = filename(tmp)
    #return 0
