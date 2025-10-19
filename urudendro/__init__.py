"""
UruDendro - A public dataset and tools for cross-section tree ring analysis.

This package provides tools for downloading, visualizing, and analyzing tree ring
images from the UruDendro dataset, as well as evaluation metrics for tree ring
detection algorithms.

Copyright (c) 2023-2024 Henry Marichal and contributors
Licensed under AGPL-3.0
"""

__version__ = "0.5.0"
__author__ = "Henry Marichal"
__email__ = "hmarichal93@gmail.com"
__license__ = "AGPL-3.0"

# Import main functions for easy access
from urudendro.dataset import download_dataset, visualize_annotation
from urudendro.metric_influence_area import main as compute_metrics
from urudendro.remove_salient_object import remove_salient_object

# Define public API
__all__ = [
    "download_dataset",
    "visualize_annotation",
    "compute_metrics",
    "remove_salient_object",
    "__version__",
]
