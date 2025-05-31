from setuptools import setup, find_packages

setup(
    name="conv_shp2gpkg",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "geopandas",
    ],
    entry_points={
        "console_scripts": [
            "convertir-shp=conv_shp2gpkg.__main__:main",
        ]
    },
    author="Kevin",
    description="Herramienta para convertir shapefiles a GeoPackage con reproyección.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
)
