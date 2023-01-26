# Environment setting

## Install Anaconda

Anaconda version can be changed. Check https://www.anaconda.com/
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
```
```
./Anaconda3-5.2.0-Linux-x86_64.sh
```
```
source ~/.bashrc
```

## Create conda environment

```
conda create -n openpcdet python=3.8
```
```
conda activate openpcdet
```

## Install pytorch

CUDA version is 11.3
```
conda install pytorch==1.12.0 torchvision==0.13.0 torchaudio==0.12.0 cudatoolkit=11.3 -c pytorch
```

## Install spconv

```
pip install spconv-cu113
```

## Git Clone & Install requirements

```
git clone https://github.com/cbnuirl/cbnu_openpcdet.git
cd cbnu_openpcdet
pip install -r requirements.txt
python setup.py develop
```

# Data Conversion

Prepare data like:
```
data/
  └custom/
    ├pcd/
    │ └XX_XX_TXWX_XX_XXX_REXX_XXX.pcd
    │   -> point cloud(train + val)
    ├train/
    │ └XX_XX_TXWX_XX_XXX_REXX_XXX.json
    │   -> bounding box information
    └val/
      └XX_XX_TXWX_XX_XXX_REXX_XXX.json
```

Then, run:
```
pip install tqdm open3d numpy # If not installed
```

```
python tools/dataset_converters/custom.py --data_path {DATA_PATH}
```

Changed into custom format like:
```
data/
  └custom/
    ├ImageSets/   
    │	├test.txt
    │	├train.txt
    │	└val.txt
    │     -> index of splited data
    ├labels/
    │	└XXXXXX.txt
    │	  -> bounding box information
    └points/
        └XXXXXX.npy
          -> point cloud
```

Other files will not be used in training

```
python -m pcdet.datasets.custom.custom_dataset create_custom_infos tools/cfgs/dataset_configs/custom_dataset.yaml
```

**NOTE**: If dataset have Pedestrian, Cyclist

tools/cfgs/custom_models/second.yaml
```
CLASS_NAMES: ['Vehicle', 'Pedestrian', 'Cyclist']  
...
```
