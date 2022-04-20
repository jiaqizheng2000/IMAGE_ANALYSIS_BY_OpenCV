import os
from One_image_process_Evap_4_10 import one_image_processing_evap_4_10,to_csv_evap_4_10
Base_path='D:/IMAGE_ANALYSIS'

datapath_evap_0410='images/Evap.data/0410'
datapath_evap_0411='images/Evap.data/0410'

store_path_evap_path_10=os.path.join(Base_path,"Results/height_all_evap_04_10.csv")
store_path_evap_path_11=os.path.join(Base_path,"Results/height_all_evap_04_11.csv")

def data_evap_to_csv(datapath,storepath):
    full_path = os.path.join(Base_path, datapath)
    name = os.listdir(full_path)
    print(name)
    name.sort(key=lambda x: int(x.split('.')[0].split('_')[2]))

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)-1):
        one_image_processing_evap_4_10(full_name[i])

    to_csv_evap_4_10(storepath)

if __name__=='__main__':
    data_evap_to_csv(datapath_evap_0410,store_path_evap_path_10)
    data_evap_to_csv(datapath_evap_0411,store_path_evap_path_11)