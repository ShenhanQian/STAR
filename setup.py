from setuptools import setup, find_packages

setup(
    name="star",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "dlib",
        "tyro",
        "tqdm",
        "torch",
        "torchvision",
        "python-gflags",
        "pandas",
        "pillow",
        "numpy",
        "opencv-python",
        "imageio",
        "imgaug",
        "lmdb",
        "lxml",
        "tensorboard",
        "protobuf",
        "pyyaml",
    ],
    include_dirs=["star"],
)
