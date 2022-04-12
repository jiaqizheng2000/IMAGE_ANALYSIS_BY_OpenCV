import os
from one_image_process_vinicius import one_image_processing_vincius,to_csv_vinicius
from One_image_process_Evap import one_image_processing_Evap,to_csv_Evap
Base_path='D:/image_analyse'

datapath_vinicius_12='images/12'
datapath_vinicius_17='images/17'
datapath_vinicius_23='images/23'
datapath_vinicius_29='images/29'

datapath_evap_21='images/Evap.data/0321'
datapath_evap_22='images/Evap.data/0322'

store_path_vinicius_12=os.path.join(Base_path,"Results/height_all_Vinicius_12.csv")
store_path_vinicius_17=os.path.join(Base_path,"Results/height_all_Vinicius_17.csv")
store_path_vinicius_23=os.path.join(Base_path,"Results/height_all_Vinicius_23.csv")
store_path_vinicius_29=os.path.join(Base_path,"Results/height_all_Vinicius_29.csv")

store_path_evap_path_21=os.path.join(Base_path,"Results/height_all_evap_21.csv")
store_path_evap_path_22=os.path.join(Base_path,"Results/height_all_evap_22.csv")

def data_vinicine_to_csv(datapath,storepath):
    full_path=os.path.join(Base_path,datapath)
    name=os.listdir(full_path)

    name.sort(key=lambda x: int(x.split('.')[0].split('(')[1]))
    print(name)

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)-1):
        one_image_processing_vincius(full_name[i])


    to_csv_vinicius(storepath)

def data_evap_to_csv(datapath,storepath):
    full_path = os.path.join(Base_path, datapath)
    name = os.listdir(full_path)
    print(name)
    name.sort(key=lambda x: int(x.split('.')[0].split('_')[2]))

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)-1):
        one_image_processing_Evap(full_name[i])

    to_csv_Evap(storepath)

if __name__=='__main__':

    data_vinicine_to_csv(datapath_vinicius_12,store_path_vinicius_12)
    data_vinicine_to_csv(datapath_vinicius_17,store_path_vinicius_17)
    data_vinicine_to_csv(datapath_vinicius_23,store_path_vinicius_23)
    data_vinicine_to_csv(datapath_vinicius_29,store_path_vinicius_29)

    data_evap_to_csv(datapath_evap_21,store_path_evap_path_21)
    data_evap_to_csv(datapath_evap_21,store_path_evap_path_22)
