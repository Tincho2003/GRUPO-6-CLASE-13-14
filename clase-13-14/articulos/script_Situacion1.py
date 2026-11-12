"""
Dataset ampliado (>= 500 titulos distintos) con la API de TMDB:
  - Peliculas basadas en videojuegos (todos los anios)
  - Peliculas familiares/animacion de 2025
  - A Minecraft Movie (2025), siempre incluida

Uso:
    pip install requests pandas
    PowerShell:  $env:TMDB_TOKEN="tu_token"
    python tmdb_dataset_500.py
Genera: dataset_peliculas_videojuegos.csv
"""
import os
import sys
import time
from datetime import date

import pandas as pd
import requests

TOKEN = os.environ.get("TMDB_TOKEN")
if not TOKEN:
    sys.exit("Falta la variable de entorno TMDB_TOKEN (Read Access Token v4).")

BASE = "https://api.themoviedb.org/3"
HEADERS = {"Authorization": f"Bearer {TOKEN}", "accept": "application/json"}
OBJETIVO = 500          # minimo de titulos distintos
MARGEN = 650            # candidatas a reunir (algunas se descartan por duplicadas)
MAX_PAGINAS = 500       # tope de TMDB por consulta


def get(path, **params):
    for intento in range(5):
        r = requests.get(f"{BASE}{path}", headers=HEADERS, params=params, timeout=30)
        if r.status_code == 429:
            time.sleep(2 * (intento + 1))
            continue
        r.raise_for_status()
        return r.json()
    raise RuntimeError(f"Demasiados reintentos en {path}")


# 1) A Minecraft Movie
res = get("/search/movie", query="A Minecraft Movie", primary_release_year=2025)
if not res["results"]:
    sys.exit("No se encontro A Minecraft Movie.")
minecraft_id = res["results"][0]["id"]
print(f"A Minecraft Movie -> id {minecraft_id}")

# 2) Keywords de videojuegos
kw_ids = []
for consulta in ("based on video game", "video game"):
    for k in get("/search/keyword", query=consulta)["results"]:
        if k["name"].lower() == consulta and k["id"] not in kw_ids:
            kw_ids.append(k["id"])
print(f"Keywords videojuego -> {kw_ids}")
if not kw_ids:
    sys.exit("No se encontro la keyword de videojuegos.")

# 3) Candidatas
categorias = {minecraft_id: {"Minecraft"}}


def agregar(etiqueta, tope, **filtros):
    """Recorre paginas de /discover/movie hasta alcanzar 'tope' candidatas nuevas."""
    nuevas = 0
    pagina = 1
    while nuevas < tope and pagina <= MAX_PAGINAS:
        data = get("/discover/movie", page=pagina, include_adult="false", **filtros)
        for m in data["results"]:
            if m["id"] not in categorias:
                nuevas += 1
            categorias.setdefault(m["id"], set()).add(etiqueta)
        if pagina >= data["total_pages"]:
            break
        pagina += 1
    print(f"  {etiqueta}: +{nuevas} candidatas")


print("Reuniendo candidatas...")
agregar("Adaptacion videojuego", 450,
        with_keywords="|".join(map(str, kw_ids)), sort_by="vote_count.desc")
agregar("Familiar/Animacion 2025", MARGEN - len(categorias),
        primary_release_year=2025, with_genres="10751|16", sort_by="popularity.desc")
if len(categorias) < MARGEN:
    agregar("Adaptacion videojuego", MARGEN - len(categorias),
            with_keywords="|".join(map(str, kw_ids)), sort_by="popularity.desc")

print(f"Candidatas: {len(categorias)}. Consultando detalle de cada una...")


# 4) Detalle
def detalle(mid):
    d = get(f"/movie/{mid}", language="es-AR")
    return {
        "id": d["id"],
        "titulo": d["title"],
        "titulo_original": d["original_title"],
        "estreno": d["release_date"],
        "presupuesto_usd": d["budget"],
        "recaudacion_usd": d["revenue"],
        "popularidad": d["popularity"],
        "nota_promedio": d["vote_average"],
        "votos": d["vote_count"],
        "duracion_min": d["runtime"],
        "generos": ", ".join(g["name"] for g in d["genres"]),
    }


filas = []
for i, (mid, cats) in enumerate(categorias.items(), 1):
    fila = detalle(mid)
    fila["categoria"] = " | ".join(sorted(cats))
    filas.append(fila)
    if i % 50 == 0:
        print(f"  {i}/{len(categorias)}")
    time.sleep(0.05)

df = pd.DataFrame(filas)

# 5) Limpieza: titulos distintos (titulo + anio) y fecha valida
df["anio"] = pd.to_datetime(df["estreno"], errors="coerce").dt.year
df = df.dropna(subset=["anio"])
df["anio"] = df["anio"].astype(int)
df = df.drop_duplicates(subset=["titulo_original", "anio"])
df = df.drop_duplicates(subset=["id"])

# Columnas calculadas (ROI solo si hay presupuesto y recaudacion cargados)
tiene_datos = (df["presupuesto_usd"] > 0) & (df["recaudacion_usd"] > 0)
df["ROI"] = (df["recaudacion_usd"] / df["presupuesto_usd"]).where(tiene_datos)
df["ganancia_bruta_usd"] = (df["recaudacion_usd"] - df["presupuesto_usd"]).where(tiene_datos)
df["ranking_recaudacion"] = df["recaudacion_usd"].rank(ascending=False, method="min").astype(int)
df["fecha_extraccion"] = date.today().isoformat()
df = df.sort_values("recaudacion_usd", ascending=False)

df.to_csv("dataset_peliculas_videojuegos.csv", index=False, encoding="utf-8-sig")

print(f"\nListo: {len(df)} titulos distintos guardados en dataset_peliculas_videojuegos.csv")
if len(df) < OBJETIVO:
    print(f"AVISO: quedaron menos de {OBJETIVO} filas. Subi MARGEN en el script o agrega otra fuente.")
print("A Minecraft Movie incluida:", minecraft_id in set(df["id"]))
print(df[["titulo", "anio", "presupuesto_usd", "recaudacion_usd", "popularidad", "categoria"]].head(10).to_string(index=False))