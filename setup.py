"""Setup configuration for UruDendro package."""
import os
import shutil
from pathlib import Path
from setuptools import setup, find_packages
from setuptools.command.build_py import build_py


class BuildPyCommand(build_py):
    """Custom build command to copy u2net.pth model file."""
    
    def run(self):
        """Run the build and copy the model file."""
        build_py.run(self)
        
        # Copy u2net.pth to the build directory
        if os.path.exists('u2net.pth'):
            # Get the build lib directory
            build_lib = self.build_lib
            dest_dir = os.path.join(build_lib, 'urudendro')
            dest_file = os.path.join(dest_dir, 'u2net.pth')
            
            # Create directory if it doesn't exist
            os.makedirs(dest_dir, exist_ok=True)
            
            # Copy the model file
            print(f"Copying u2net.pth to {dest_file}")
            shutil.copy2('u2net.pth', dest_file)
        else:
            print("Warning: u2net.pth not found. The model will need to be downloaded separately.")


# Read the README for long description
def read_readme():
    """Read README.md for long description."""
    readme_path = Path(__file__).parent / "README.md"
    if readme_path.exists():
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""


# Read requirements from requirements.txt
def read_requirements():
    """Read requirements from requirements.txt."""
    requirements_path = Path(__file__).parent / "requirements.txt"
    requirements = []
    if requirements_path.exists():
        with open(requirements_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                # Skip empty lines, comments, and special pip options
                if line and not line.startswith('#') and not line.startswith('--'):
                    # Remove version specifiers that use ==, convert to >=
                    if '==' in line:
                        pkg = line.split('==')[0].strip()
                        version = line.split('==')[1].strip()
                        requirements.append(f"{pkg}>={version}")
                    else:
                        requirements.append(line)
    return requirements


setup(
    name="urudendro",
    version="0.5.0",
    author="Henry Marichal",
    author_email="hmarichal93@gmail.com",
    description="UruDendro - A dataset and tools for cross-section tree ring analysis",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/hmarichal93/uruDendro",
    project_urls={
        "Bug Tracker": "https://github.com/hmarichal93/uruDendro/issues",
        "Documentation": "https://iie.fing.edu.uy/proyectos/madera/",
        "Paper": "https://arxiv.org/abs/2404.10856",
    },
    packages=find_packages(include=["urudendro", "urudendro.*"]),
    package_data={
        "urudendro": ["u2net.pth"],
    },
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    cmdclass={
        'build_py': BuildPyCommand,
    },
    keywords="dendrochronology tree-rings image-processing computer-vision deep-learning",
    license="AGPL-3.0",
)