# UruDendro: Cross-Section Images of Pinus Taeda

A dataset and Python toolkit for automated tree ring detection and analysis in Pinus Taeda cross-sections.

[Paper](https://rdcu.be/euo3F) • [Dataset (Zenodo)](https://doi.org/10.5281/zenodo.15110646) • [Project Page](https://iie.fing.edu.uy/proyectos/madera/)  
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%203.0-blue.svg)](LICENSE)

---

## Features

- 📊 Public dataset of tree ring images
- 🔍 Automated detection & segmentation
- 📏 Evaluation metrics
- 🎨 Annotation visualization
- 🤖 Deep learning background removal (U2-Net)

---

## Quick Installation (Recommended)

Install [uv](https://github.com/astral-sh/uv) if you don’t have it:
```bash
pip install uv
```

Create a fast, isolated environment and install all dependencies:
```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.txt
pip install -e .
```

> **Note:** The U2-Net model file (`u2net.pth`) must be in `urudendro/`. If you cloned with git-lfs:
> ```bash
> sudo apt-get install git-lfs
> git lfs pull
> ```

---

## Usage

**Download dataset:**
```python
import urudendro
urudendro.download_dataset('/absolute/path/to/dataset')
```

**Visualize annotations:**
```python
import urudendro
urudendro.visualize_annotation('annotation.json', 'image.png', 'output_dir/')
```

**Evaluate detection:**
```python
import urudendro
precision, recall, f_score, rmse, tp, fp, tn, fn = urudendro.compute_metrics(
    'detection.json', 'ground_truth.json', 'image.png',
    cx=512, cy=512, threshold=0.5, output_dir='results/'
)
```

**Remove background:**
```python
import urudendro
urudendro.remove_salient_object('input.jpg', 'output.jpg')
```

---

## Requirements

- Python ≥ 3.8
- PyTorch ≥ 2.4.1
- OpenCV ≥ 4.8.1
- NumPy ≥ 1.26.1
- See `requirements.txt` for full list

---

## Citation

If you use UruDendro, please cite:

```bibtex
@article{marichal2025uruDendro,
  title={UruDendro: a public dataset of cross-section images of Pinus taeda},
  author={Marichal, Henry and Passarella, Diego and Lucas, Christine and Profumo, Ludmila and Casaravilla, Verónica and Rocha Galli, María Noel and Ambite, Serrana and Randall, Gregory},
  journal={Annals of Forest Science},
  volume={82}, number={1}, pages={1--21}, year={2025},
  publisher={Springer},
  doi={10.1186/s13595-024-01267-6},
  url={https://rdcu.be/euo3F}
}
```
Dataset: [https://doi.org/10.5281/zenodo.15110646](https://doi.org/10.5281/zenodo.15110646)

---

## Alternative Installation

You may also use pip or conda if preferred:
```bash
pip install git+https://github.com/hmarichal93/uruDendro.git
# or
conda env create -f environment.yml
conda activate uruDendro
pip install -e .
```
