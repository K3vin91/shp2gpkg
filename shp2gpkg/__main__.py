import argparse
from pathlib import Path
import geopandas as gpd

def convertir_shapefiles(carpeta_entrada, carpeta_salida, epsg_destino):
    shapefiles = list(carpeta_entrada.rglob("*.shp"))
    total = len(shapefiles)
    exitosos = 0
    resumen = []

    for ruta in shapefiles:
        try:
            gdf = gpd.read_file(ruta)
            if gdf.crs is None:
                gdf.set_crs(epsg=4326, inplace=True)
            gdf = gdf.to_crs(epsg=epsg_destino)

            ruta_relativa = ruta.relative_to(carpeta_entrada).with_suffix(".gpkg")
            ruta_salida = carpeta_salida / ruta_relativa
            ruta_salida.parent.mkdir(parents=True, exist_ok=True)

            gdf.to_file(ruta_salida, driver="GPKG")
            exitosos += 1
            resumen.append(f"{ruta.stem}: exitoso")

        except Exception as e:
            resumen.append(f"{ruta.stem}: fallido → {e}")

    ruta_resumen = carpeta_salida / "resumen_conversion.txt"
    with ruta_resumen.open("w", encoding="utf-8") as f:
        f.write("RESUMEN DE CONVERSIÓN DE SHAPEFILES A GPKG\n\n")
        f.write(f"Total de capas: {total}\n")
        f.write(f"Capas exitosas: {exitosos}\n")
        f.write(f"Capas fallidas: {total - exitosos}\n\n")
        f.write("Detalle:\n" + "\n".join(resumen))

    print(f"\n📝 Resumen guardado en: {ruta_resumen}")

def main():
    parser = argparse.ArgumentParser(description="Convierte shapefiles a GeoPackage con reproyección.")
    parser.add_argument("--entrada", type=Path, required=True, help="Ruta a la carpeta raíz de shapefiles")
    parser.add_argument("--salida", type=Path, required=True, help="Ruta donde se guardarán los GeoPackages")
    parser.add_argument("--epsg", type=int, default=32616, help="EPSG de destino (por defecto: 32616)")
    args = parser.parse_args()
    convertir_shapefiles(args.entrada, args.salida, args.epsg)

if __name__ == "__main__":
    main()
