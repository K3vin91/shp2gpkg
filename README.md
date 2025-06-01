
# Herramienta conv_shp2gpkg

<p align="center">
  <img src="assets/icono.png" alt="conv_shp2gpkg icono" width="150"/>
</p>

**conv_shp2gpkg** es una herramienta de línea de comandos escrita en Python que convierte archivos Shapefile (.shp) en GeoPackage (.gpkg), 
reproyectándolos al sistema de coordenadas deseado. Ideal para flujos de trabajo SIG automatizados.

---

## 📦 Características

- Busca y convierte todos los `.shp` dentro de una carpeta raíz, incluyendo subcarpetas.
- Exporta cada archivo convertido en formato `.gpkg`.
- Asigna un EPSG personalizado a cada capa (por defecto: EPSG 32616).
- Guarda un registro de las conversiones realizadas y posibles errores.
- Crea una carpeta paralela para almacenar los archivos de salida.

---

## 🛠️ Requisitos

- Python 3.8 o superior
- Paquetes:
  - `geopandas`
  - `fiona`
  - `shapely`
  - `pyproj`

Instalación de dependencias:

```bash
pip install -r requirements.txt
```

---

## 🚀 Uso

```bash
python -m conv_shp2gpkg --entrada "ruta/a/las/capas" --salida "ruta/destino/gpkg" --epsg 32616
```

### Parámetros

| Parámetro  | Descripción                                    | Requerido |
|------------|------------------------------------------------|-----------|
| `--entrada` | Ruta de la carpeta raíz con shapefiles         | ✅        |
| `--salida`  | Ruta donde se guardarán los archivos `.gpkg`   | ✅        |
| `--epsg`    | Código EPSG del sistema de coordenadas         | Opcional (por defecto: 32616) |

---

## 📁 Estructura del proyecto

```
conv_shp2gpkg/
├── conv_shp2gpkg/
│   ├── __init__.py
│   └── __main__.py
├── assets/
│   └── icono.png
├── resumen_conversion.txt
├── setup.py
├── pyproject.toml
├── LICENSE
└── README.md
```

---

## 🧪 Ejemplo

```bash
python -m conv_shp2gpkg --entrada "C:/SIG/DatosBrutos" --salida "C:/SIG/Geopackages" --epsg 32616
```

---

## 🧑‍💻 Contribuciones

¡Estás invitado a contribuir! Por favor revisa [CONTRIBUTING.md](CONTRIBUTING.md) para saber cómo puedes ayudar.

---

## 📝 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE).

