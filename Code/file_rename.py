import os

def rename_files(path):
    files=os.listdir(path)
    num=1
    for file in files:
        used_name,extension=os.path.splitext(file)
        new_name = str(num)+extension
        os.rename(file,new_name)
        num+=1

if __name__ == '__main__':
    filePath=os.getcwd()
    rename_files(filePath)