import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import folium
from geopy.geocoders import Nominatim
import time

# =====================================
# 1. Carregando e preparando os dados
# =====================================
df = pd.read_csv("results.csv")
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['decade'] = (df['year'] // 10) * 10
df['total_goals'] = df['home_score'] + df['away_score']

# =====================================
# 2. Gráfico Estático 1: Partidas por década
# =====================================
decade_counts = df['decade'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.bar(decade_counts.index.astype(str), decade_counts.values, color='steelblue')
plt.title('Número de partidas internacionais por década')
plt.xlabel('Década')
plt.ylabel('Número de partidas')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("partidas_por_decada.png")
plt.show()

# =====================================
# 3. Gráfico Estático 2: Top 10 seleções com mais vitórias
# =====================================
df['winner'] = df.apply(
    lambda x: x['home_team'] if x['home_score'] > x['away_score']
    else (x['away_team'] if x['away_score'] > x['home_score'] else 'Draw'),
    axis=1
)
top_winners = df[df['winner'] != 'Draw']['winner'].value_counts().head(10)
plt.figure(figsize=(10, 6))
sns.barplot(x=top_winners.values, y=top_winners.index, palette='viridis')
plt.title('Top 10 seleções com mais vitórias')
plt.xlabel('Vitórias')
plt.ylabel('Seleção')
plt.tight_layout()
plt.savefig("top10_vitorias.png")
plt.show()

# =====================================
# 4. Gráfico Interativo: Gols por ano
# =====================================
goals_by_year = df.groupby('year')['total_goals'].sum().reset_index()
fig = px.line(goals_by_year, x='year', y='total_goals', title='Total de gols por ano')
fig.write_html("gols_por_ano.html")
fig.show()

# =====================================
# 5. Mapa Interativo: Local das partidas
# =====================================
map_df = df.dropna(subset=['city', 'country']).copy()
map_df = map_df[['city', 'country']].drop_duplicates().head(100)  # limitar para visualização
map_df['location_str'] = map_df['city'] + ", " + map_df['country']

# Geolocalização com geopy
geolocator = Nominatim(user_agent="futebol_mapa")

def get_coordinates(loc):
    try:
        location = geolocator.geocode(loc)
        time.sleep(1)  # pausa para evitar bloqueio
        if location:
            return pd.Series([location.latitude, location.longitude])
    except:
        return pd.Series([None, None])
    return pd.Series([None, None])

map_df[['lat', 'lon']] = map_df['location_str'].apply(get_coordinates)
map_df = map_df.dropna(subset=['lat', 'lon'])

# Criando o mapa
world_map = folium.Map(location=[20, 0], zoom_start=2)
for _, row in map_df.iterrows():
    folium.Marker(location=[row['lat'], row['lon']], popup=row['location_str']).add_to(world_map)

world_map.save("mapa_partidas.html")
