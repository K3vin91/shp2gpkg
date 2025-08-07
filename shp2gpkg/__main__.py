import argparse
from pathlib import Path
import geopandas as gpd
from tqdm import tqdm

def convertir_shapefiles(carpeta_entrada, carpeta_salida, epsg_destino=None):
    shapefiles = list(carpeta_entrada.rglob("*.shp"))
    total = len(shapefiles)
    exitosos = 0
    sin_crs = 0
    resumen = []

    for ruta in tqdm(shapefiles, desc="🔄 Convirtiendo capas"):
        try:
            gdf = gpd.read_file(ruta)
            mensaje_extra = ""

            if gdf.crs is None:
                sin_crs += 1
                if epsg_destino:
                    gdf.set_crs(epsg=epsg_destino, inplace=True)
                    mensaje_extra = f" (CRS original indefinido → se asignó directamente EPSG:{epsg_destino})"
                    print(f"⚠️ {ruta.stem}: no tenía CRS → se asignó directamente EPSG:{epsg_destino}")
                else:
                    gdf.set_crs(epsg=4326, inplace=True)
                    mensaje_extra = f" (CRS original indefinido → se asignó EPSG:4326)"
                    print(f"⚠️ {ruta.stem}: no tenía CRS → se asignó EPSG:4326")

            elif epsg_destino:
                gdf = gdf.to_crs(epsg=epsg_destino)
                mensaje_extra = f" (Reproyectado a EPSG:{epsg_destino})"

            ruta_relativa = ruta.relative_to(carpeta_entrada).with_suffix(".gpkg")
            ruta_salida = carpeta_salida / ruta_relativa
            ruta_salida.parent.mkdir(parents=True, exist_ok=True)

            gdf.to_file(ruta_salida, driver="GPKG")
            exitosos += 1
            resumen.append(f"{ruta.stem}: exitoso{mensaje_extra}")

        except Exception as e:
            print(f"❌ {ruta.stem}: fallido → {e}")
            resumen.append(f"{ruta.stem}: fallido → {e}")

    ruta_resumen = carpeta_salida / "resumen_conversion.txt"
    with ruta_resumen.open("w", encoding="utf-8") as f:
        f.write("RESUMEN DE CONVERSIÓN DE SHAPEFILES A GPKG\n\n")
        f.write(f"Total de capas: {total}\n")
        f.write(f"Capas exitosas: {exitosos}\n")
        f.write(f"Capas fallidas: {total - exitosos}\n")
        f.write(f"Capas sin CRS original: {sin_crs}\n\n")
        f.write("Detalle:\n" + "\n".join(resumen))

    print(f"\n📝 Resumen guardado en: {ruta_resumen}")

def main():
    parser = argparse.ArgumentParser(description="Convierte shapefiles a GeoPackage con reproyección opcional.")
    parser.add_argument("--entrada", type=Path, required=True, help="Ruta a la carpeta raíz de shapefiles")
    parser.add_argument("--salida", type=Path, required=True, help="Ruta donde se guardarán los GeoPackages")
    parser.add_argument("--epsg", type=int, default=None, help="EPSG de destino (opcional). Si no se especifica, se conserva el CRS original o se asigna EPSG:4326 si no tiene")
    args = parser.parse_args()
    convertir_shapefiles(args.entrada, args.salida, args.epsg)

if __name__ == "__main__":
    main()

