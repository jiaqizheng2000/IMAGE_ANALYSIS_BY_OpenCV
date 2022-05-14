import os
from one_image_process_May_high import one_image_processing_high,to_csv_high
from one_image_process_May_low import one_image_processing_low,to_csv_low
Base_path='D:/IMAGE_ANALYSIS'

datapath_high='images/high_heights'
datapath_low='images/low_heights'

store_path_high=os.path.join(Base_path,"Results/height_all_high_heights.csv")
store_path_low=os.path.join(Base_path,"Results/height_all_low_heights.csv")

def data_to_csv_high(datapath,storepath):
    full_path = os.path.join(Base_path, datapath)
    name = os.listdir(full_path)
    print(len(name))
    name.sort(key=lambda x: int(x.split('.')[0].split('_')[1]+x.split('.')[0].split('_')[2]))

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)):
        one_image_processing_high(full_name[i])

    to_csv_high(storepath)

def data_to_csv_low(datapath,storepath):
    full_path = os.path.join(Base_path, datapath)
    name = os.listdir(full_path)
    print(len(name))
    name.sort(key=lambda x: int(x.split('.')[0].split('_')[1]+x.split('.')[0].split('_')[2]))

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)):
        one_image_processing_low(full_name[i])

    to_csv_low(storepath)

if __name__=='__main__':
    # data_to_csv_high(datapath_high,store_path_high)
    data_to_csv_low(datapath_low,store_path_low)