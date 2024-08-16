import os
import argparse
import sys

# this script generates image folder neccessary for training model in cira core without the need of manual labeliing 


parser = argparse.ArgumentParser('convert class index')
parser.add_argument("-f", metavar="from", dest="by", type=int, help="from which class index")
parser.add_argument("-t", metavar="to", dest="to", type=int, help="to which class index")
parser.add_argument("-mode", metavar="mode", dest="mode", type=str, help="to which class index")
args = parser.parse_args()
to_index = args.to
from_index = args.by
mode = args.mode
print(to_index)
print(from_index)
print(mode)

folder = os.getcwd()
txtfile_path = os.path.join(folder, 'train.txt')


# current index is still fixed, will change to arguments once workload increases
def generate():
    count = 1
    global folder
    imgfolder = os.path.join(folder, 'img')
    print(imgfolder)
    txtfile_path = os.path.join(folder, 'train.txt')
    print(txtfile_path)
    with open(txtfile_path, 'w') as f:
        for file in os.listdir(imgfolder):
            if file.endswith('.jpg'):
                imgfile_path = os.path.join('data/img', file)
                f.write(imgfile_path)
                f.write('\n')
            if file.endswith('.txt'):
                txtfile_path = os.path.join(imgfolder, file)
                with open(txtfile_path, 'r') as g:
                    reader = g.readlines()
                    new_list = []
                    new_reader = []
                    for line in reader:
                        line = line.rstrip('\n')
                        new_reader.append(line)
                    # todo right strip away the newline character
                    for line in new_reader:
                        item = line.split(' ')
                        # check if data point is for segmentation
                        # if yes, remove the boundary box
                        # if len(item) > 5:
                        #    continue
                        if item [0] == '0':
                            item[0] = '451'
                        elif item [0] == '1':
                            item[0] = '16'
                        new_item = ' '.join(item)
                        #print(new_item)
                        new_list.append(new_item)
                    #print(reader)
                    print(new_list)
                with open(txtfile_path, 'w') as h:
                    for line in new_list:
                        h.write(f'{line}\n')
                print(count)
                count += 1

def iso_segment_data():
    # find and count the number of segmentation data in the datset
    global folder
    imgfolder = os.path.join(folder, 'img')
    count = 0
    for file in os.listdir(imgfolder):
        id = file.rstrip('.txt')
        print(id)
        if file.endswith('.txt'):
            txtfile_path = os.path.join(imgfolder, file)
            with open(txtfile_path, 'r') as g:
                reader = g.readlines()
                new_reader = []
                for line in reader:
                    line = line.rstrip('\n')
                    new_reader.append(line)
                for line in new_reader:
                    item = line.split(' ')
                    if len(item) > 6:
                        print('segment data found')
                        count += 1
    print(count)


def change_sig_fig():
    global folder
    imgfolder = os.path.join(folder, 'img')
    for file in os.listdir(imgfolder):
        if file.endswith('.txt'):
            txtfile_path = os.path.join(imgfolder, file)
            with open(txtfile_path, 'r') as g:
                new_list = []
                reader = g.readlines()
                new_reader = []
                for line in reader:
                    line = line.rstrip('\n')
                    new_reader.append(line)
                for line in new_reader:
                    item = line.split(' ')
                    new_item = []
                    for i, element in enumerate(item):
                        if i == 0:
                            new_item.append(element)
                        else:
                            element = float(element)
                            element = f'{element:.6g}'
                            element = float(element)
                            print(element)
                            new_item.append(str(element))
                    # fix here
                    new_item = ' '.join(item)
                    new_list.append(new_item)
                print(f'new list is {new_list}')
            with open(txtfile_path, 'w') as h:
                for line in new_list:
                    h.write(f'{line}\n')


def remove():
    global folder
    imgfolder = os.path.join(folder, 'img')
    for file in os.listdir(imgfolder):
        if file.endswith('.txt'):
            txtfile_path = os.path.join(imgfolder, file)
            new_list = []
            with open(txtfile_path, 'r') as g:
                reader = g.readlines()
                new_reader = []
                for line in reader:
                    line = line.rstrip('\n')
                    new_reader.append(line)




if __name__ == "__main__":
    if mode == "count":
        iso_segment_data()
    if mode == "roundoff":
        change_sig_fig()
