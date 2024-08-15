import os
import argparse

# this script generates image folder neccessary for training model in cira core without the need of manual labeliing 

# to improve this script, we should do relative path

parser = argparse.ArgumentParser('convert class index')
parser.add_argument("-f", metavar="from", dest="by", type=int, help="from which class index")
parser.add_argument("-t", metavar="to", dest="to", type=int, help="to which class index")
args = parser.parse_args()
to_index = args.to
from_index = args.by
print(to_index)
print(from_index)

folder = os.getcwd()
txtfile_path = os.path.join(folder, 'train.txt')


# current index is still fixed, will change to arguments once workload increases
def generate():
    global folder
    imgfolder = os.path.join(folder, 'img')
    print(imgfolder)
    txtfile_path = os.path.join(folder, 'train.txt')
    print(txtfile_path)
    with open(txtfile_path, 'w') as f:
        for file in os.listdir(imgfolder):
            if file.endswith('.jpg'):
                imgfile_path = os.path.join('data/img', file)
                print(imgfile_path)
                f.write(imgfile_path)
                f.write('\n')
            if file.endswith('.txt'):
                txtfile_path = os.path.join(imgfolder, file)
                with open(txtfile_path, 'r') as g:
                    reader = g.readlines()
                    new_list = []
                    for line in reader:
                        item = line.split(' ')
                        # check if data point is for segmentation
                        if len(item) > 5:
                            continue
                        if item [0] == '0':
                            item[0] = '451'
                        elif item [0] == '1':
                            item[0] = '16'
                        new_item = ' '.join(item)
                        #print(new_item)
                        new_list.append(new_item)
                    print(reader)
                    print(new_list)
                with open(txtfile_path, 'w') as h:
                    if len(new_list) != 0:
                        h.writelines(new_list)

if __name__ == "__main__":
    generate()
