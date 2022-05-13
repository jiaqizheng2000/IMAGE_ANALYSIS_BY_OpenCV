import os
from One_image_process_Evap_0410 import one_image_processing_evap_4_10,to_csv_evap_4_10
from One_image_process_Evap_0321 import one_image_processing_Evap_0321,to_csv_Evap_0321
Base_path='D:/IMAGE_ANALYSIS'

datapath_evap_0321='images/Evap.data/0321'
datapath_evap_0410='images/Evap.data/0410'

store_path_evap_path_0410=os.path.join(Base_path,"Results/height_all_evap_0410_11.csv")
store_path_evap_path_0321=os.path.join(Base_path,"Results/height_all_evap_0321_22.csv")

def data_evap0410_to_csv(datapath,storepath):
    full_path = os.path.join(Base_path, datapath)
    name = os.listdir(full_path)
    print(name)
    name.sort(key=lambda x: int(x.split('.')[0].split('_')[1]+x.split('.')[0].split('_')[2]))

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)):
        one_image_processing_evap_4_10(full_name[i])

    to_csv_evap_4_10(storepath)

def data_evap0321_to_csv(datapath,storepath):
    full_path = os.path.join(Base_path, datapath)
    name = os.listdir(full_path)
    print(name)
    name.sort(key=lambda x: int(x.split('.')[0].split('_')[1]+x.split('.')[0].split('_')[2]))

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)):
        one_image_processing_Evap_0321(full_name[i])

    to_csv_Evap_0321(storepath)

if __name__=='__main__':
    data_evap0410_to_csv(datapath_evap_0410,store_path_evap_path_0410)
    data_evap0321_to_csv(datapath_evap_0321,store_path_evap_path_0321)
