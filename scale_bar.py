import pandas as pd
from pathlib import Path
import numpy as np
from urudendro.image import load_image, write_image
import cv2

def draw_scale_bar_on_image(image, m):
    """
    Draw a scale bar on the image of size 50mm.
    @param image: The input image.
    @param m: Relation millimiter to pixel. [mm] = m * [pixel]
    """
    scale_bar_length_mm = 50
    scale_bar_length_px = int(scale_bar_length_mm / m)
    scale_bar_width = 5
    h, w, _ = image.shape

    # Draw the scale bar
    start_point = (int(w*0.85), int(h*0.05))
    end_point = (start_point[0] + scale_bar_length_px, start_point[1])

    # Draw a white rectangle for the scale bar
    background_size = 10
    cv2.rectangle(image, (start_point[0]-3*background_size, start_point[1]-3*background_size),
                  (end_point[0] + background_size, end_point[1] + scale_bar_width + background_size),
                  (255, 255, 255), -1)

    # Draw the scale bar on the image
    cv2.rectangle(image, start_point, (end_point[0], end_point[1] + scale_bar_width), (0, 0, 0), -1)

    # Add text label
    cv2.putText(image, f"{scale_bar_length_mm} mm", ((start_point[0]), start_point[1] - 5),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    return image

def main(images_dir:str="/data/maestria/publicaciones/urudendro64/annals_of_forest_science/zenodo_v2"):
    file_path = Path(images_dir) / "pixel_millimeter.txt"
    df = pd.read_csv(file_path, delimiter=",")
    images_dir = Path(images_dir)
    output_dir = Path(images_dir) / "images_scale_bar"
    output_dir.mkdir(parents=True, exist_ok=True)

    for idx, row in df.iterrows():
        image_name = row.iloc[0]
        m = row.iloc[3]
        image = load_image(images_dir / f"images/{image_name}.png")
        image_scale = draw_scale_bar_on_image(image, m)
        write_image(output_dir / f"{image_name}.png", image_scale)

    return









if __name__ == "__main__":
    main()