import os
from one_image_process_vinicius import one_image_processing_vincius,to_csv_vinicius
Base_path='D:/IMAGE_ANALYSIS'

datapath_vinicius_12='images/12'
datapath_vinicius_17='images/17'
datapath_vinicius_23='images/23'
datapath_vinicius_29='images/29'

store_path_vinicius_12=os.path.join(Base_path,"Results/height_all_Vinicius_12.csv")
store_path_vinicius_17=os.path.join(Base_path,"Results/height_all_Vinicius_17.csv")
store_path_vinicius_23=os.path.join(Base_path,"Results/height_all_Vinicius_23.csv")
store_path_vinicius_29=os.path.join(Base_path,"Results/height_all_Vinicius_29.csv")

def data_vinicine_to_csv(datapath,storepath):
    full_path=os.path.join(Base_path,datapath)
    name=os.listdir(full_path)

    name.sort(key=lambda x: int(x.split('.')[0].split('(')[1]))
    print(name)

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)):
        one_image_processing_vincius(full_name[i])


    to_csv_vinicius(storepath)

if __name__=='__main__':

    data_vinicine_to_csv(datapath_vinicius_12,store_path_vinicius_12)
    data_vinicine_to_csv(datapath_vinicius_17,store_path_vinicius_17)
    data_vinicine_to_csv(datapath_vinicius_23,store_path_vinicius_23)
    data_vinicine_to_csv(datapath_vinicius_29,store_path_vinicius_29)


