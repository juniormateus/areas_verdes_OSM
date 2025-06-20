import osmnx as ox
import geopandas as gpd
import folium
from pathlib import Path

# Configurações do projeto
cidade = "Florianópolis, Santa Catarina, Brazil"
saida_geojson = Path("data/areas_verdes.geojson")
saida_mapa_html = Path("output/mapa_areas_verdes.html")

# Tags OSM para praças e parques
tags = {
    "leisure": ["park", "garden", "common"],
    "place": "square",
    "landuse": "recreation_ground"
}

print(f"Buscando dados de áreas verdes para: {cidade}")
gdf = ox.features_from_place(cidade, tags=tags)

# Filtra apenas geometrias válidas e com nome (opcional)
gdf = gdf[gdf.geometry.notnull()]
gdf = gdf[gdf["geometry"].geom_type.isin(["Polygon", "MultiPolygon", "Point"])]

# Salva como GeoJSON
print(f"💾 Salvando GeoJSON em: {saida_geojson}")
gdf.to_file(saida_geojson, driver="GeoJSON")

# Gera o mapa interativo com Folium
print(f"Gerando mapa interativo em: {saida_mapa_html}")
centro = gdf.geometry.unary_union.centroid
mapa = folium.Map(location=[centro.y, centro.x], zoom_start=13)

for _, row in gdf.iterrows():
    nome = row.get("name", "Área verde")
    geom = row.geometry
    if geom.geom_type == "Point":
        folium.Marker(
            location=[geom.y, geom.x],
            popup=nome,
            icon=folium.Icon(color="green", icon="tree-conifer")
        ).add_to(mapa)
    else:
        folium.GeoJson(
            data=geom,
            name=nome,
            tooltip=nome,
            style_function=lambda x: {
                "color": "green",
                "weight": 1,
                "fillOpacity": 0.3
            }
        ).add_to(mapa)

mapa.save(saida_mapa_html)
print("Processo finalizado com sucesso!")
