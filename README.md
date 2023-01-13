# 3D Object Detection with SECOND on MORAI dataset

This repository is based on [OpenPCDet](https://github.com/open-mmlab/OpenPCDet). All configurations and codes were revised for MORAI dataset.

## Results and Models

### SECOND

Class accuracy is IoU(Intersection over Union).

| Dataset | epoch | bbox AP(0.70) | bev AP(0.70) | bev AP(0.50) | 3d AP(0.70) | 3d AP(0.50) | aos | config | log | model |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Real | 80 | | | | | | | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Daegu | 80 | | | | | | | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Sejong BRT 1 | 80 | | | | | | | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Sangam Edge | 80 | | | | | | | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |
| Sejong BRT 1 Edge | 80 | | | | | | | [config](tools/cfgs/custom_models/second.yaml) | [log] | [model] |

Real:



Daegu:



Sejong BRT 1:



Sangam Edge:



Sejong BRT 1 Edge:




## Usage

### Installation

Please refer to [install.md](docs/install.md) for installation, dataset preparation and making configuration file.

### Testing, Demo

```

```

Example:
```

```

### Training

```

```

Example:
```

```
