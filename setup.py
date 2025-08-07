from setuptools import setup, find_packages

setup(
    name="shp2gpkg",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "geopandas",
        "tqdm"
    ],
    entry_points={
        "console_scripts": [
            "shp2gpkg=shp2gpkg.__main__:main",
        ]
    },
    author="Kevin Irias",
    description="Herramienta para convertir shapefiles a GeoPackage con reproyección.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
