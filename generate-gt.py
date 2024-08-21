import json
import os
import cv2 as cv


# json library turn list to json format


all_class = {
            "0": {
                    "color": "255, 0, 255", #RGB
                    "label":"a"                  
                },
            "1": {
                    "color":"255, 0, 0", #RGB
                    "label": "b"
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
    center = str(int(x)) + "," + str(int(y))
    x = int(x - w/2)
    y = int(y - h/2)
    w = int(w)
    h = int(h)
    box = str(x) + "," + str(y) + "," + str(w) + "," + str(h)
    return center, box

# def convert_label():
    # when dealing with labelled data in cira core only

def labelling(item):
    global all_class
    color = all_class[item]["color"]
    label = all_class[item]["label"]
    return color, label

def generate():
    folder = os.getcwd()
    imgfolder = os.path.join(folder, 'ing')
    print(imgfolder)
    gen_output = []
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
            width, height, channels = img.shape
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
                x = float(line[1])
                x = float(line[1])*width
                print(f'x: {x}')
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

    gt_path = os.path.join(folder, "gt.gt") 
    with open(gt_path, "w") as g:
        json_output = json.dumps(gen_output, indent=4)
        g.write(json_output)


if __name__ == "__main__":
    generate()
