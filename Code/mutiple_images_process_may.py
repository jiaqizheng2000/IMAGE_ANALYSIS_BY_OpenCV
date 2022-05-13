import os
from one_image_process_May import one_image_processing,to_csv
Base_path='D:/IMAGE_ANALYSIS'

datapath_high='images/high_heights'
datapath_low='images/low_heights'

store_path_high=os.path.join(Base_path,"Results/height_all_high_heights.csv")
store_path_low=os.path.join(Base_path,"Results/height_all_low_heights.csv")

def data_to_csv(datapath,storepath):
    full_path = os.path.join(Base_path, datapath)
    name = os.listdir(full_path)
    print(len(name))
    name.sort(key=lambda x: int(x.split('.')[0].split('_')[1]+x.split('.')[0].split('_')[2]))

    full_name = []
    for i in range(len(name)):
        full_name.append(os.path.join(full_path,name[i]))

    for i in range(len(full_name)):
        one_image_processing(full_name[i])

    to_csv(storepath)

if __name__=='__main__':
    # data_to_csv(datapath_high,store_path_high)
    data_to_csv(datapath_low,store_path_low)