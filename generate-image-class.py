import os
import cv2 as cv

def count():
    # count number of nondamaged container image based on label in text file
    count = 0
    totalcount = 0
    parent_folder = os.getcwd()
    img_folder = 'img'
    folder = os.path.join(parent_folder, img_folder)
    print(f'folder is {folder}')
    for file in os.listdir(folder):
        damage = False
        if file.endswith('.png'):
            continue 
        else:
            id = file.rstrip('.txt')
            if id.endswith('Cr') or id.endswith('Cl'):
                continue
            txt_path = os.path.join(folder, file)
            print(txt_path)
            with open(txt_path, 'r') as f:
                reader = f.readlines()
            for line in reader:
                line = line.rstrip('\n')
                line = line.split(' ')
                if line[0] != '0':
                    print(line)
                    damage = True
                    break
                else:
                    damage = False
            if damage is False:
                count += 1
                crop_section(id, txt_path)
            totalcount += 1
            if totalcount >= 40:
                break
    print(f'no damage image count is {count}')
    print(f'total count is {totalcount}')

def crop_section(id, txt_path):
    width = 1920
    height = 1080
    newfolder = "E:/nodamage"
    img_path = os.path.join(newfolder, id+'.png')
    print(img_path)
    image = cv.imread(img_path)
    with open(txt_path, 'r') as f:
        reader = f.readlines()
    for line in reader:
        line = line.rstrip('\n')
        item = line.split(' ')
        extract_and_write(item, image, width, height)


def extract_and_write(item: list, image, width, height):
    x = float(item[1])*width
    y = float(item[2])*height
    w = float(item[3])*width
    h = float(item[4])*height
    x_1, y_1 = round(x - w/2), round(y - h/2)
    w_1 = int(w/8)
    h_1 = int(h/3)
    k = 0
    for i in range(8):
        for j in range(3):
            x_k = x_1 + i*w_1
            y_k = y_1 + j*h_1
            img = image[y_k:y_k + h_1, x_k:x_k + w_1]
            try:
                cv.imwrite(f'test{k}.png', img)
            except cv.error:
                continue
            print(f'k is {k}')
            print(f'{i}, {j}')
            k += 1


if __name__ == '__main__':
    count()
