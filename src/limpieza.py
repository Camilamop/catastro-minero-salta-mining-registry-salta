"""Carga y limpieza reproducible del catastro minero de Salta.
Uso: from src.limpieza import cargar_catastro"""

import geopandas as gpd
import pandas as pd
from pathlib import Path
from shapely.validation import make_valid

CRITICOS = {'LI', 'CU', 'AU'}
SHP = "poligonos_adaf55f39328ff45c8c60e94eb13a7a0.shp"


def _es_critico(valor):
    if pd.isna(valor):
        return False
    tokens = {t.strip().upper() for t in str(valor).split(',')}
    return bool(tokens & CRITICOS)


def cargar_catastro(carpeta, snapshot, shp=SHP, verbose=True):
    """Lee un corte del catastro y devuelve los 3 DataFrames limpios.

    carpeta : ruta a la carpeta del corte (ej. 'data/raw/agosto_2026')
    snapshot: etiqueta del corte (ej. 'agosto_2026'), se agrega como columna
    Devuelve dict con 'cmin', 'cmin_completo', 'cmin_critico'.
    """
    ruta = Path(carpeta) / shp

    # 1. Lectura + CRS
    cmin = gpd.read_file(ruta, encoding='latin-1').to_crs(epsg=4326)

    # 2. Fecha explícita
    cmin['fecha_inic'] = pd.to_datetime(
        cmin['fecha_inic'], errors='coerce', dayfirst=True)

    # 3. area_ha (formato argentino: 1.234,56 ha)
    cmin['area_ha'] = (
        cmin['area']
        .str.replace(' ha', '', regex=False)
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
        .pipe(pd.to_numeric, errors='coerce')
    )

    # 4. Geometrías válidas
    invalidas = ~cmin.geometry.is_valid
    if invalidas.any():
        cmin.loc[invalidas, 'geometry'] = cmin.loc[invalidas, 'geometry'].apply(make_valid)

    # 5. Etiqueta de corte (clave para el análisis longitudinal futuro)
    cmin['snapshot'] = snapshot

    # 6. Subconjunto con mineral
    cmin_completo = cmin[
        cmin['mineral'].notna() & (cmin['mineral'].str.strip() != '')
    ].copy()

    # 7. Clasificación de minerales críticos (token-set, sin regex)
    cmin_completo['minerales_criticos'] = cmin_completo['mineral'].apply(_es_critico)

    # 8. Subconjunto crítico
    cmin_critico = cmin_completo[cmin_completo['minerales_criticos']].copy()

    if verbose:
        print(f"[{snapshot}] total={len(cmin):,} | con mineral={len(cmin_completo):,} "
              f"| críticos={len(cmin_critico):,} | inválidas reparadas={int(invalidas.sum())}")

    return {'cmin': cmin, 'cmin_completo': cmin_completo, 'cmin_critico': cmin_critico}