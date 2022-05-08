from shutil import copyfile
import os

image_path = "path"
txt_path = "path"

image_files = os.listdir(image_path)
txt_files = os.listdir(txt_path)

output_image_path ="path"
output_txt_path = "path"
count = 0
for image_file in image_files:
    if count<len(image_files)/10*8:
        copyfile(image_path+image_file, output_image_path+"train\\"+image_file)
    elif count<len(image_files)/10*9:
        copyfile(image_path+image_file, output_image_path+"val\\"+image_file)
    else:
        copyfile(image_path+image_file, output_image_path+"test\\"+image_file)
    count+=1

count = 0
for txt_file in txt_files:
    if count < len(txt_files) / 10 * 8:
        copyfile(txt_path + txt_file, output_txt_path + "train\\" + txt_file)
    elif count < len(txt_files) / 10 * 9:
        copyfile(txt_path + txt_file, output_txt_path + "val\\" + txt_file)
    else:
        copyfile(txt_path + txt_file, output_txt_path + "test\\" + txt_file)
    count += 1
