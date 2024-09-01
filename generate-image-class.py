import os
import cv2 as cv

def count(class_id):
    # count number of container image class based on label in text file
    count = 0
    parent_folder = os.getcwd()
    img_folder = 'train'
    folder = os.path.join(parent_folder, img_folder)
    print(f'folder is {folder}')
    for file in os.listdir(folder):
        damage = False
        if file.endswith('.jpg'):
            continue
        else:
            id = file.rstrip('.txt')
            #if id.endswith('Cr') or id.endswith('Cl'):
                #continue
            txt_path = os.path.join(folder, file)
            print(txt_path)
            img_file = id + '.jpg'
            img_path = os.path.join(folder, img_file)
            image = cv.imread(img_path)
            height, width, channels = image.shape
            width = 1920
            height = 1080
            with open(txt_path, 'r') as f:
                reader = f.readlines()
            for line in reader:
                line = line.rstrip('\n')
                line = line.split(' ')
                '''
                if line[0] != f'{class_id}':
                    print(line)
                    damage = True
                    break
                '''
                if line[0] == f'{class_id}':
                    damage = True
                    count += 1
                    break
                else:
                    damage = False
            if damage is True:
                cv.imwrite('E:/newdentclass/{img_file}', image)
    print(count)

def create_image(image,width,height,x,y):
    image = cv.imread('1646813296_Camera_A.png')
    with open('1646813296_Camera_A.txt', 'r') as f:
        reader = f.readlines()

    print(reader)
    for line in reader:
        line = line.rstrip('\n')
        item = line.split(' ')
        index = item[0]
        x = float(item[1])*width
        y = float(item[2])*height
        w = float(item[3])*width
        h = float(item[4])*height
    x_1, y_1 = round(x - w/2), round(y - h/2)
    print(x_1, y_1)
    x_2, y_2 = round(x + w/2), round(y + h/2)
    print(x_1, y_1, x_2, y_2)
    img = image[y_1:y_2, x_1:x_2]
    hg, wd, ch = img.shape
    print(f'dimesion are {hg},{wd},{ch}')
    cv.imwrite('test.png', img)
    # lets do 16 by 4
    w_i = round(wd/16)
    h_i = round(hg/4)
    print(w_i, h_i)
    k=0
    for i in range(16):
        for j in range(4):
            x_i = x_1 + i*w_i
            y_i = y_1 + j*h_i
            img = image[y_i:y_i+h_i, x_i:x_i+w_i]
            cv.imwrite(f'test{k}.png', img)
            print(f'k is {k}')
            print(x_i, y_i)
            k+=1
    


    # total 1000 image 1/4 for around axis, 
    
if __name__ == '__main__':
    count()
