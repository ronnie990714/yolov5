import os
import json
import time

class_dict = {"탑": 0, "블라우스": 1, "티셔츠": 2, "니트웨어": 3, "셔츠": 4, "브라탑": 5, "후드티": 6, "청바지": 7, "팬츠": 8, "스커트": 9,
              "래깅스": 10, "조거팬츠": 11, "코트": 12, "재킷": 13, "점퍼": 14, "패딩": 15, "베스트": 16, "가디건": 17, "짚업": 18, "드레스": 19, "점프수트": 20}
object=[0,3,4,5,6,10,11,12,13,14,15,16,17,18,20]

path = "path"
output_path = "path"

json_files = os.listdir(path)
start_time=time.time()

for file_name in json_files:
    if(file_name[-4:] == "json"):
        with open(path + "\\" + file_name, "r", encoding="UTF-8") as json_file:
            json_data = json.load(json_file)
        image_width = json_data['이미지 정보']['이미지 너비']
        image_height = json_data['이미지 정보']['이미지 높이']
        for k, v in json_data['데이터셋 정보']['데이터셋 상세설명']['렉트좌표'].items():
            if(v[0]):
                try:
                    classNum = json_data['데이터셋 정보']['데이터셋 상세설명']['라벨링'][str(k)][0]['카테고리']
                except:
                    continue
                object_width = v[0]['가로']
                object_height = v[0]['세로']
                with open(output_path + "\\" + file_name[:-4] + "txt", "a", encoding="UTF-8") as txt_file:
                    txt_file.write(
                        f"{class_dict[classNum]}\t{round((v[0]['X좌표']+object_width/2)/image_width, 6)}\t{round((v[0]['Y좌표']+object_height/2)/image_height, 6)}\t{round(object_width/image_width, 6)}\t{round(object_height/image_height, 6)}\n")

print("all done! running time : {}".format(time.time()-start_time))