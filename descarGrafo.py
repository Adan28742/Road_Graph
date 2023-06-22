import folium
import osmnx as ox
import shutil
import matplotlib

listapx = ((-12.0990933,-76.9692345), (-12.0992089, -76.9692794), (-12.0996268, -76.9694398))
coordinate = (-11.882031150174072, -77.12999757667411)

m = folium.Map(
    tiles='Stamen Terrain',
    zoom_start=15,
    location=coordinate
)

folium.PolyLine(listapx).add_to(m)

center = (-11.882031150174072, -77.12999757667411)
road = ox.graph_from_point(center, dist=2000, network_type='drive')

# Guardar el grafo en formato GraphML
ox.save_graphml(road, "grafo.graphml")

# Mover el archivo a una ubicación local
ruta_destino = "C:/users/sebas/OneDrive/Escritorio/ESAN/CICLO VI/grafo.graphml"
shutil.move("grafo.graphml", ruta_destino)