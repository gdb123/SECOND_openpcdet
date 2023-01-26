import argparse
import os
import shutil
from tqdm import tqdm
import json
import open3d
import numpy as np

parser = argparse.ArgumentParser(description="Convert MORAI into custom")
parser.add_argument("--data_path", type=str, help="MORAI data path")
args = parser.parse_args()
if args.data_path[len(args.data_path) - 1] != '/':
    args.data_path = args.data_path + '/'

train_path = args.data_path + "train/"
train_list = os.listdir(train_path)
val_path = args.data_path + "val/"
val_list = os.listdir(val_path)
pcd_path = args.data_path + "pcd/"
pcd_list = os.listdir(pcd_path)

# Create labels
if not os.path.isdir(args.data_path + "label/"):
    os.mkdir(args.data_path + "label/")
label_path = args.data_path + "label/"

for list in train_list:
    shutil.move(train_path + list, label_path + list)
for list in val_list:
    shutil.move(val_path + list, label_path + list)
label_list = os.listdir(label_path)

if not os.path.isdir(args.data_path + "labels/"):
    os.mkdir(args.data_path + "labels/")
labels_path = args.data_path + "labels/"

classes = []
for bbox in tqdm(label_list, desc="labels"):
    with open(label_path + bbox) as f:
        bbox_json = json.load(f)
    
    annotations = bbox_json['annotations']

    for ann in annotations:
        if ann['distance'] == -1 or ann['bbox'] == []:
            continue
        if ann['class'] not in classes:
            classes.append(ann['class'])

        x = round(ann['location'][0], 2)
        y = round(ann['location'][1], 2)
        z = round(ann['location'][2], 2)
        dx = round(ann['dimension'][0], 2)
        dy = round(ann['dimension'][1], 2)
        dz = round(ann['dimension'][2], 2)
        heading_angle = round(ann['orientation'][2], 2)
        category_name = "Vehicle"
        if ann['class'] == "Pedestrian":
            category_name == "Pedestrian"
        elif ann['class'] == "bicycle":
            category_name == "Cyclist"
        elif ann['class'] == "animal":
            continue

        text = (
            str(x) + ' ' + str(y) + ' ' + str(z) + ' ' +
            str(dx) + ' ' + str(dy) + ' ' + str(dz) + ' ' +
            str(heading_angle) + ' ' + category_name + '\n'
        )

        with open(labels_path + bbox[:-5] + ".txt", 'a') as f:
            f.write(text)

print("classes: ", classes)

# Create points
if not os.path.isdir(args.data_path + "points/"):
    os.mkdir(args.data_path + "points/")
points_path = args.data_path + "points/"

for pcd in tqdm(pcd_list, desc="points"):
    point_cloud = open3d.io.read_point_cloud(pcd_path + pcd)
    pcd_array = np.asarray(point_cloud.points, dtype=np.float32)
    PATH = pcd_path + "../points/" + pcd[:-4] + ".npy"
    np.save(PATH, pcd_array)

# Create ImageSets, Rename
if not os.path.isdir(args.data_path + "ImageSets/"):
    os.mkdir(args.data_path + "ImageSets/")
imagesets_path = args.data_path + "ImageSets/"

labels_list = os.listdir(labels_path)
labels_list.sort()
points_list = os.listdir(points_path)
points_list.sort()

if not os.path.isdir(args.data_path + "trash/"):
    os.mkdir(args.data_path + "trash/")

for point in tqdm(points_list, desc="sort points"):
    if point[:-4] + ".txt" not in labels_list:
        shutil.move(points_path + point, points_path + "../trash/" + point)
shutil.rmtree(points_path + "../trash/")

for idx, item in tqdm(enumerate(labels_list), desc="rename"):
    name = item[:-4] + ".json"
    if name in val_list:
        with open(labels_path + "../ImageSets/val.txt", 'a') as f:
            f.write(f'{idx:06d}' + '\n')
    elif name in train_list:
        with open(labels_path + "../ImageSets/train.txt", 'a') as f:
            f.write(f'{idx:06d}' + '\n')
    with open(labels_path + "../ImageSets/test.txt", 'a') as f:
            f.write(f'{idx:06d}' + '\n')
    shutil.move(labels_path + item, labels_path + f'{idx:06d}' + ".txt")
    shutil.move(points_path + item[:-4] + ".npy", points_path + f'{idx:06d}' + ".npy")

# Clean up
for label in label_list:
    if label in train_list:
        shutil.move(label_path + label, train_path + label)
    elif label in val_list:
        shutil.move(label_path + label, val_path + label)
os.rmdir(label_path)
