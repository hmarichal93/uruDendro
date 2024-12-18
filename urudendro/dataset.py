"""Script for downloading and preprocessing the dataset."""
import os
import argparse
from pathlib import Path

from urudendro.io import load_json, write_json
from urudendro.labelme import draw_curves_over_image
def download_file_and_store_id_in_dir(images_url, dataset_path, local_filename="images.zip"):

    os.system(f"cd {dataset_path} && wget -r -np -nH --cut-dirs=3 -R index.html {images_url}")
    page_name = images_url.split("/")[-2]
    #1.1 move file to images.zip
    os.system(f"mv {dataset_path}/{page_name}/index.html.tmp {dataset_path}/{local_filename}")
    #1.2 remove 244 directory
    os.system(f"rm -r {dataset_path}/{page_name}")
    return



def process_annotations(annotations_path, images_path):
    annotations_path = Path(f"{annotations_path}/")
    for file in annotations_path.rglob("*"):
        file_json = load_json(file)
        #file_json["imageData"] = None
        img_name = file.name.split(".")[0].split("-")[0]
        file_json["imagePath"] = str(f"{images_path}/{img_name}.png")
        write_json(file_json, file)


def unzip_file(path, filename):
    os.system(f"mkdir -p {path} && cd {path} && unzip -o -q ../{filename} && rm ../{filename}")
    return

def download_dataset(dataset_path="/home/henry/Documents/repo/fing/uruDendro/data2"):
    "Download the dataset from url"
    # create dataset path directory if not exists
    os.system(f"mkdir -p {dataset_path}")
    #1.0 download images from url
    images_url = "https://iie.fing.edu.uy/proyectos/madera/download/244/"
    images_name = "images.zip"
    images_path = f"{dataset_path}/images"
    download_file_and_store_id_in_dir(images_url, dataset_path, local_filename=images_name)
    #2.0 unzip images
    unzip_file(images_path, images_name)

    #3.0 download labels from url
    annotations_url = "https://iie.fing.edu.uy/proyectos/madera/download/246/"
    annotations_name = "labels.zip"
    download_file_and_store_id_in_dir(annotations_url, dataset_path, local_filename=annotations_name)
    annotations_path = f"{dataset_path}/annotations"
    unzip_file(annotations_path, annotations_name)

    #4.0 download pith annotations
    pith_url = "https://iie.fing.edu.uy/proyectos/madera/download/248/"
    pith_name = "pith.csv"
    pith_path = f"{dataset_path}/pith"
    download_file_and_store_id_in_dir(pith_url, dataset_path, local_filename=pith_name)
    #os.system(f"rmdir {pith_path}")
    #unzip_file(pith_path, pith_name)

    #5.0 process annotations
    process_annotations(annotations_path, images_path)
    return
def visualize_annotation(annotation_path, image_path, output_path):
    #os.system(f"labelme {annotation_path}")
    draw_curves_over_image(annotation_path, image_path, output_path)
    return


if __name__ == "__main__":
    #create parser. Two options. Option 1: download dataset. Option 2: visualize annotation
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--download', action='store_true', help='download dataset')
    parser.add_argument('--dataset_path', type=str, help='path to download dataset')
    parser.add_argument('--visualize', action='store_true', help='visualize annotation')
    parser.add_argument('--annotation_file', type=str, help='annotation file to visualize')
    parser.add_argument('--image_file', type=str, help='image file to visualize')
    parser.add_argument('--output_path', type=str, help='output path to save visualization')
    args = parser.parse_args()
    if args.download:
        download_dataset(args.dataset_path)

    if args.visualize:
        visualize_annotation(args.annotation_file, args.image_file, args.output_path)