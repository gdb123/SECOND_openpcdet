# Environment setting

## Install Anaconda

Anaconda version can be changed. Check https://www.anaconda.com/
```
curl -O https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh
```
```
bash Anaconda3-5.2.0-Linux-x86_64.sh
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

Change into custom format like:
```

```

Prepare data like:
```

```

Then, run:
```

```


# Change Configuration File

Modify content:

```

```
