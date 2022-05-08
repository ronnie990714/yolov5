import readline
from shutil import copyfile
import os
import shutil

input_path="path"
output_path="path"

label_list=['0','2','3','4','5','6','10','11','12','13','14','15','16','17','18','20']
txt_files=os.listdir(input_path)
# print(txt_files)

for txt_file in txt_files:
    f_name=input_path+"\\"+txt_file
    f=open(f_name,"r",encoding="UTF8")
    for i in f.readlines():
        label=i.split('\t').pop(0)
        if(label in label_list):
            shutil.copyfile(f_name,output_path+"\\"+txt_file)
