import os

def count()
    # count number of nondamaged container image based on label in text file
    count = 0
    folder = os.getcwd()
    print(folder)
    for file in os.listdir(folder):
        if file.endswith('.jpg'):
            continue 
        else:
            id = file.rstrip(',jpg')
            txt_path = os.path.join(folder,file)

            with open(txt_path, 'r') as f:
                reader = f.readlines()
            for line in reader:
                line = line.rstrip('\n')
                line = line.split(' ')
                if line[0] != '0':
                    damage = True
                    break
                else:
                    damage = False
            if damage == False:
                count += 1
    print(count)


if __name__ == '__main__':
    count()
