import os
import shutil

txt_path="path"
image_input_path="path"
image_output_path="path"

txt_files=os.listdir(txt_path)
img_files=os.listdir(image_input_path)
txt_file_list=[]

for txt_file in txt_files:
    txt_file_list.append(os.path.splitext(txt_file)[0])

for img_file in img_files:
    img_file_name=os.path.splitext(img_file)[0]
    if(img_file_name in txt_file_list):
        shutil.copyfile(image_input_path+"\\"+img_file,image_output_path+"\\"+img_file)

