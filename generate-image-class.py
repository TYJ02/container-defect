import os

def count():
    # count number of nondamaged container image based on label in text file
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
            id = file.rstrip(',jpg')
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
    print(count)


if __name__ == '__main__':
    count()
