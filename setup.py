import setuptools

from setuptools.command.develop import develop
from setuptools.command.install import install
from subprocess import check_call
import sysconfig
import os
import shutil

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        python_lib_dir = sysconfig.get_path("purelib")
        src = "u2net.pth"
        dst = os.path.join(python_lib_dir, "urudendro", "u2net.pth")
        #shutil.copy(src, dst)
        print(f"cp {src} {dst}")
        os.system(f"cp {src} {dst}")
        os.system(f"mv u2net.pth urudendro/")
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        python_lib_dir = sysconfig.get_path("purelib")
        src = "u2net.pth"
        dst = os.path.join(python_lib_dir, "urudendro", "u2net.pth")
        print(f"cp {src} {dst}")
        os.system(f"cp {src} {dst}")
        os.system(f"mv u2net.pth urudendro/")
        install.run(self)

setuptools.setup(
    name="urudendro",
    version="0.4",
    python_requires=">=3.6",
    packages=setuptools.find_packages(include=["urudendro", "urudendro.*"]),
    cmdclass={
        'develop': PostDevelopCommand,
        'install': PostInstallCommand,
    },
)