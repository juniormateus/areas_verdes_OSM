# 🏞️ Extração de Praças e Parques com OpenStreetMap

Este projeto tem como objetivo extrair, visualizar e analisar espacialmente **praças e parques urbanos** utilizando a API do OpenStreetMap, com foco inicial em **Florianópolis/SC**, mas com possibilidade de adaptação para qualquer localidade.

## 🌐 Descrição

A partir de consultas à Overpass API via biblioteca `osmnx`, são coletados elementos do tipo:

- `leisure=park`
- `leisure=garden`
- `leisure=common`
- `place=square`
- `landuse=recreation_ground`

Estes dados representam áreas verdes públicas, como **parques urbanos**, **jardins**, **praças** e outras **zonas de lazer**, essenciais para planejamento urbano, saúde ambiental e qualidade de vida.

---

## ⚙️ Tecnologias Utilizadas

- [Python 3.10+]
- [OSMnx]
- [GeoPandas]
- [Folium] *(opcional para mapa interativo)*

---

## 📦 Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/seu-usuario/praças-e-parques-osm.git
cd areas_verdes_OSM
pip install -r requirements.txt
