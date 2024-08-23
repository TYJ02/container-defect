import json
import os
import cv2 as cv
from progress.bar import Bar


# json library turn list to json format
serial_class = {
            "0": {
                    "color": "255, 0, 255", #RGB
                    "label":"0"                  
                }
        }

ocr_class = {
            "0": {
                    "color": "255, 0, 255", #RGB
                    "label":"0"                  
                },
            "1": {
                    "color":"255, 0, 0", #RGB
                    "label": "1"
                },
            "2": {
                    "color": "255, 0, 255", #RGB
                    "label":"2"                  
                },
            "3": {
                    "color":"255, 0, 0", #RGB
                    "label": "3"
                },
            "4": {
                    "color": "255, 0, 255", #RGB
                    "label":"4"                  
                },
            "5": {
                    "color":"255, 0, 0", #RGB
                    "label": "5"
                },
            "6": {
                    "color": "255, 0, 255", #RGB
                    "label":"6"                  
                },
            "7": {
                    "color":"255, 0, 0", #RGB
                    "label": "7"
                },
            "8": {
                    "color": "255, 0, 255", #RGB
                    "label":"8"                  
                },
            "9": {
                    "color":"255, 0, 0", #RGB
                    "label": "9"
                },
            "10": {
                    "color": "255, 0, 255", #RGB
                    "label": "a"
                },
            "11": {
                    "color":"255, 0, 0", #RGB
                    "label":"b"                  
                },
            "12": {
                    "color": "255, 0, 255", #RGB
                    "label": "c"
                },
            "13": {
                    "color": "255, 0, 255", #RGB
                    "label":"d"                  
                },
            "14": {
                    "color":"255, 0, 0", #RGB
                    "label": "e"
                },
            "15": {
                    "color": "255, 0, 255", #RGB
                    "label":"f"                  
                },
            "16": {
                    "color":"255, 0, 0", #RGB
                    "label": "g"
                },
            "17": {
                    "color": "255, 0, 255", #RGB
                    "label":"h"                  
                },
            "18": {
                    "color":"255, 0, 0", #RGB
                    "label": "i"
                },
            "19": {
                    "color": "255, 0, 255", #RGB
                    "label":"j"                  
                },
            "20": {
                    "color":"255, 0, 0", #RGB
                    "label": "k"
                },
            "21": {
                    "color": "255, 0, 255", #RGB
                    "label":"l"                  
                },
            "22": {
                    "color":"255, 0, 0", #RGB
                    "label": "m"
                },
            "23": {
                    "color": "255, 0, 255", #RGB
                    "label":"n"                  
                },
            "24": {
                    "color":"255, 0, 0", #RGB
                    "label": "o"
                },
            "25": {
                    "color": "255, 0, 255", #RGB
                    "label":"p"                  
                },
            "26": {
                    "color":"255, 0, 0", #RGB
                    "label":"r"                  
                },
            "27": {
                    "color": "255, 0, 255", #RGB
                    "label": "s"
                },
            "28": {
                    "color":"255, 0, 0", #RGB
                    "label":"t"                  
                },
            "29": {
                    "color": "255, 0, 255", #RGB
                    "label": "u"
                },
            "30": {
                    "color":"255, 0, 0", #RGB
                    "label":"v"                  
                },
            "31": {
                    "color": "255, 0, 255", #RGB
                    "label": "w"
                },
            "32": {
                    "color":"255, 0, 0", #RGB
                    "label":"x"                  
                },
            "33": {
                    "color": "255, 0, 255", #RGB
                    "label": "y"
                },
            "34": {
                    "color":"255, 0, 0", #RGB
                    "label": "z"
                },
            }      

damage_class = {
            "0": {
                    "color": "255, 0, 255", #RGB
                    "label":"container"                  
                },
            "1": {
                    "color":"255, 0, 0", #RGB
                    "label": "axis"
                },
            "2": {
                    "color": "255, 0, 255", #RGB
                    "label":"concave"                  
                },
            "3": {
                    "color":"255, 0, 0", #RGB
                    "label": "dentado"
                },
            "4": {
                    "color":"255, 0, 0", #RGB
                    "label": "perforation"
                }
            }

'''
[
    {
        "filename": "a.jpg",
        "obj_array":  [
            {
                "bbox": "100,100,40,40",
                "center": "120,120",
                "color": "0,255,0",
                "label": "a",
                "label_index": 0,
                "landmark": "",
                "landmark_len": 0

            }
        ]
     }       
]
'''

def make_bbox(x,y,w,h):

    # math operation to turn ratio to int value
    center = str(round(x)) + "," + str(round(y))
    x = round(x - w/2)
    y = round(y - h/2)
    w = round(w)
    h = round(h)
    box = str(x) + "," + str(y) + "," + str(w) + "," + str(h)
    return center, box

# def convert_label():
    # when dealing with labelled data in cira core only

def labelling(item):
    global ocr_class
    color = ocr_class[item]["color"]
    label = ocr_class[item]["label"]
    return color, label

def generate():
    folder = os.getcwd()
    imgfolder = os.path.join(folder, 'img')
    print(imgfolder)
    gen_output = []
    with Bar("progressing ...") as bar:
        for file in os.listdir(imgfolder):
            print(file)
            if file.endswith('.jpg'):
                continue
            else:
                filename = file
                dict_single_img = {}
                objects = []
                id = file.rstrip(".txt")
                imgid = id + ".jpg"
                filename = imgid 
                imgpath = os.path.join(imgfolder, imgid)
                print(imgpath)
                img = cv.imread(imgpath)
                height, width, channels = img.shape
                print(width, height)

                # read file lines into list --> for each line, turn into an element in single image
                txt_path = os.path.join(imgfolder, file)

                with open(txt_path, 'r') as f:
                    reader = f.readlines()

                print(reader)
                for line in reader:
                    line = line.rstrip('\n')
                    line = line.split(' ')
                    dict_sigle_bbox = {}
                    color, label = labelling(line[0])
                    label_index = int(line[0])
                    landmark = ""
                    landmark_len = 0
                    x = float(line[1])*width
                    y = float(line[2])*height
                    w = float(line[3])*width
                    h = float(line[4])*height
                    center, box = make_bbox(x,y,w,h)
                    dict_sigle_bbox["bbox"] = box
                    dict_sigle_bbox["center"] = center
                    dict_sigle_bbox["color"] = color
                    dict_sigle_bbox["label"] = label
                    dict_sigle_bbox["label_index"] = label_index
                    dict_sigle_bbox["landmark"] = landmark
                    dict_sigle_bbox["landmark_len"] = landmark_len
                    objects.append(dict_sigle_bbox)
                    
                dict_single_img["filename"] = filename
                dict_single_img["obj_array"] = objects

            gen_output.append(dict_single_img)
            bar.next()

    gt_path = os.path.join(folder, "gt.gt") 
    with open(gt_path, "w") as g:
        json_output = json.dumps(gen_output, indent=4)
        g.write(json_output)


if __name__ == "__main__":
    generate()
