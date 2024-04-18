# UruDendro, a public dataset of cross-section images of Pinus Taeda 
Link to web-site: https://iie.fing.edu.uy/proyectos/madera/

## Requirements
- Python 3.6
- OpenCV 4.2.0
- Labelme
- SHAPELY
- Numpy 

Install the requirements using the following command:
```bash
pip install -r requirements.txt
```

## Download Dataset
Download the dataset using the following command:
```bash
python dataset.py --download --dataset_path DATASET_PATH
```
where DATASET_PATH is the path where the dataset will be downloaded. DATASET_PATH must be absolute path.

## Visualize Dataset
Visualize the dataset using the following command:
```bash
python dataset.py --visualize --annotation_file ANNOTATION_FILE
```
where ANNOTATION_FILE is the path to the annotation file.

## Metric Evaluation
Tree ring Detection evaluation metrics used by UruDendro. The evaluation code provided here can be used to obtain results on the publicly available UruDendro dataset. It computes multiple metrics described below.
```bash
python metric_influence_area.py --dt_filename DETECTION_FILENAME
 --gt_filename GROUND_TRUTH_FILENAME  --img_FILENAME IMAGE_FILENAME 
 --cx CX --cy CY --th THRESHOLD --output_dir OUTPUT_DIR
```
where DETECTION_FILENAME is the path to the detection file, GROUND_TRUTH_FILENAME is the path to the ground truth file,
IMAGE_FILENAME is the path to the image file, CX is the x pith coordinate in pixels, CY is the y pith coordinate in pixel, 
THRESHOLD is the threshold to consider a detection as valid (between 0 and 1) and OUTPUT_DIR is the path to the 
results output directory.


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
