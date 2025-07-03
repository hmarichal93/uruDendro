# UruDendro, a public dataset of cross-section images of Pinus Taeda 

**Published at Annals of Forest Science (ANFS) Journal 2025.** 


[Web-site](https://iie.fing.edu.uy/proyectos/madera/) | [Paper](https://rdcu.be/euo3F) | [Zenode](https://doi.org/10.5281/zenodo.15110646)

## Requirements
- Python 3.6
- OpenCV 4.2.0
- Labelme
- SHAPELY
- Numpy 

Install the requirements using the following command:
```bash
conda env create -f environment.yml 
```

## Installation
```bash
sudo apt-get install git-lfs
git lfs pull
python setup.py install
```

## Download Dataset
Download the dataset using the following command:
```python 
from urudendro.dataset import download_dataset
DATASET_PATH = 'path/to/dataset'
download_dataset(DATASET_PATH)
```
where DATASET_PATH is the path where the dataset will be downloaded. DATASET_PATH must be absolute path.

## Visualize Dataset
Visualize the dataset using the following command:
```python
from urudendro.dataset import visualize_annotation
ANNOTATION_FILE = 'path/to/annotation/file'
IMAGE_PATH = 'path/to/image/file'
OUTPUT_PATH = 'path/to/output/directory'
visualize_annotation(ANNOTATION_FILE, IMAGE_PATH, OUTPUT_PATH )
```
where ANNOTATION_FILE is the path to the annotation file.

## Metric Evaluation
Tree ring Detection evaluation metrics used by UruDendro. The evaluation code provided here can be used to obtain results on the publicly available UruDendro dataset. It computes multiple metrics described below.
```python 
from urudendro.metric_influence_area import main as metric
    
DETECTION_FILENAME = 'path/to/detection/file'
GROUND_TRUTH_FILENAME = 'path/to/ground/truth/file'
IMAGE_FILENAME = 'path/to/image/file'
CX = 0
CY = 0
THRESHOLD = 0.5
OUTPUT_DIR = 'path/to/output/directory'

P, R, F, RMSE, TP, FP, TN, FN = metric(DETECTION_FILENAME, GROUND_TRUTH_FILENAME, IMAGE_FILENAME, CX, CY, THRESHOLD, OUTPUT_DIR)

```
where DETECTION_FILENAME is the path to the detection file, GROUND_TRUTH_FILENAME is the path to the ground truth file,
IMAGE_FILENAME is the path to the image file, CX is the x pith coordinate in pixels, CY is the y pith coordinate in pixel, 
THRESHOLD is the threshold to consider a detection as valid (between 0 and 1) and OUTPUT_DIR is the path to the 
results output directory.


## Remove Background 

Remove the background of the image using the following command:
```python
from urudendro.remove_salient_object import remove_salient_object
IMAGE_PATH = 'input/F02c.jpg'
OUTPUT_PATH = 'input/F02c_segmented.jpg'
remove_salient_object(IMAGE_PATH, OUTPUT_PATH)
```
where IMAGE_PATH is the path to the image file and OUTPUT_PATH is the path to the output directory.

## Citation
```
@misc{marichal2024urudendro,
      title={UruDendro, a public dataset of cross-section images of Pinus taeda}, 
      author={Henry Marichal and Diego Passarella and Christine Lucas and Ludmila Profumo and Verónica Casaravilla and María Noel Rocha Galli and Serrana Ambite and Gregory Randall},
      year={2024},
      eprint={2404.10856},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```
