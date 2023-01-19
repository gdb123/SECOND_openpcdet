# 3D Object Detection with SECOND on MORAI dataset

This repository is based on [OpenPCDet](https://github.com/open-mmlab/OpenPCDet). All configurations and codes were revised for MORAI dataset.

## Results and Models

### SECOND

Class accuracy is IoU(Intersection over Union).

| Dataset | epoch | bbox AP(0.70) | bev AP(0.70) | bev AP(0.50) | 3d AP(0.70) | 3d AP(0.50) | aos | config | log | model |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Real | 80 | 84.46 | 62.83 | 74.31 | 50.25 | 73.52 | 82.70 | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Daegu | 80 | 84.99 | 74.59 | 76.46 | 62.33 | 74.77 | 79.15 | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Daegu(Mix) | 80 | 89.15 | 82.55 | 82.95 | 79.16 | 82.95 | 85.35 | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Sejong BRT 1 | 80 | 83.83 | 69.59 | 70.00 | 64.84 | 69.88 | 80.02 | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Sejong BRT 1(Mix) | 80 | 81.18 | 70.19 | 70.45 | 61.56 | 70.21 | 76.22 | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Sangam Edge | 80 |  | | | | | | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Sejong BRT 1 Edge | 80 | | | | | | | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |

Real:



Daegu:



Sejong BRT 1:



Sangam Edge:



Sejong BRT 1 Edge:




## Usage

### Installation

Please refer to [install.md](docs/install.md) for installation, dataset preparation and making configuration file.

### Testing

```
python test.py --cfg_file ${CONFIG_FILE} --batch_size ${BATCH_SIZE} --ckpt ${CKPT}
```

Example:
```
python test.py --cfg_file cfgs/custom_models/second.yaml --batch_size 4 --ckpt ../ckpt/custom_model/second_daegu.pth
```

### Training

```
python train.py --cfg_file ${CONFIG_FILE}
```

Example:
```
python train.py --cfg_file cfgs/custom_models/second.yaml
```

### Demo

```
python demo.py --cfg_file ${CONFIG_FILE} \
    --ckpt ${CKPT} \
    --data_path ${POINT_CLOUD_DATA}
    (--ext .npy)
```

Default --ext is .pcd. But custom point cloud is .npy

Example:
```
python demo.py --cfg_file cfgs/custom_models/second.yaml \
    --ckpt ../ckpt/custom_model/second_daegu.pth \
    --data_path ../data/custom/points/000000.npy
    --ext .npy
```
