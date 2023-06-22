import geopandas as gpd
from math import radians, sin, cos, sqrt, atan2

# Cargar el archivo de nodos (nodes.shp)
nodes = gpd.read_file('C:/Users/sebas/OneDrive/Escritorio/ESAN/CICLO VI/ANÁLISIS Y DISEÑO DE ALGORITMOS/pryfinal/Road_Graph-master/road.shp/nodes.shp')

# IDs de los nodos que deseas calcular la distancia entre ellos
nodo1_id = 10979948872
nodo2_id = 10979948882

# Verificar si los IDs de los nodos existen en el DataFrame
if nodo1_id not in nodes['osmid'].values or nodo2_id not in nodes['osmid'].values:
    print("Los IDs de los nodos no se encontraron en el archivo de nodos.")
else:
    # Obtener las coordenadas de los nodos
    nodo1_coords = nodes.loc[nodes['osmid'] == nodo1_id, ['y', 'x']].values
    nodo2_coords = nodes.loc[nodes['osmid'] == nodo2_id, ['y', 'x']].values

    if len(nodo1_coords) == 0 or len(nodo2_coords) == 0:
        print("Las coordenadas de los nodos no se encontraron en el archivo de nodos.")
    else:
        lat1, lon1 = map(radians, nodo1_coords[0])
        lat2, lon2 = map(radians, nodo2_coords[0])

        # Calcular la diferencia de latitud y longitud
        dlat = lat2 - lat1
        dlon = lon2 - lon1

        # Aplicar la fórmula de Haversine para calcular la distancia
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        distance = 6371 * c  # Radio de la Tierra en kilómetros

        print("La distancia entre los dos nodos es:", distance, "km")
