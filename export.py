import io
import json
import os
from PIL import Image
import torch

test_model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/best.pt')
test_input_path = "C:\\Users\\ronni\\Desktop\\test"
test_output_path = "C:\\Users\\ronni\Desktop\\output"

#define export Model
def exportModel(img_input_path, img_output_path, model_path):
    # initialize
    model = model_path
    model.eval()
    print(img_input_path)
    
    if(img_input_path.split(".").pop(1) == "jpg"):
        with open(img_input_path,'rb') as f:
            data = f.read()
        img_bytes = io.BytesIO(data)
        target_img = Image.open(img_bytes)
        results = model(target_img,size=640)
        data = results.pandas().xyxy[0].to_json(orient="index") 
        data_json = json.loads(data)
        dict_result = dict()

        # save detected result
        for k in data_json:
            label = data_json[k]['name']
            target_area = (data_json[k]['xmin'], data_json[k]['ymin'], data_json[k]['xmax'], data_json[k]['ymax'])
            # find coordinate for crop target image
            detected_image_path = img_output_path + "\\" + img_input_path.split("\\").pop(-1).split(".").pop(0)
            if not os.path.isdir(detected_image_path): # make directory to save image
                os.mkdir(detected_image_path)
            save_image_path = detected_image_path + "\\" + label + ".jpeg"
            target_img.crop(target_area).save(save_image_path)
            dict_result[label]=save_image_path

    return dict_result  # output ex) {'Jeans': 'img_path', 'Coat': 'img_path'}


#for test
test = os.listdir(test_input_path)
print(test)
for file in test:
    print(exportModel(test_input_path+"\\"+file, test_output_path,test_model))
print("done!")
 # for testing - image file