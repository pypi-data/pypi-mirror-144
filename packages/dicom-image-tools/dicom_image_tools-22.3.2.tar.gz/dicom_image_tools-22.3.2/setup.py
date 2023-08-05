from pathlib import Path

from setuptools import find_packages, setup

README = (Path(__file__).parent / "README.md").read_text()

setup(
    name="dicom_image_tools",
    version="22.3.2",
    description="Python package for managing DICOM images from different modalities",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/BwKodex/dicomimagetools",
    author="Josef Lundman",
    author_email="josef@lundman.eu",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["pydicom>=2.1.1", "numpy>=1.20.0", "scikit-image>=0.17.2", "scipy>=1.5.4", "plotly"],
    zip_safe=False,
)
