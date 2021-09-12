from networkx.algorithms.shortest_paths.astar import astar_path_length
import osmnx as ox
import networkx as nx
import plotly.graph_objects as go
import numpy as np
from random import randint

def get_coordinate(punto):
    coordinate = {}
    if(punto == 'magazzino'):
        coordinate['y'] = 41.122145722114226
        coordinate['x'] = 16.83511575578864
    elif(punto == 'centro commerciale'):
        coordinate['y'] = 41.11066278357663
        coordinate['x'] = 16.85121704780033
    elif(punto == 'negozio elettronica'):
        coordinate['y'] = 41.12519492716369
        coordinate['x'] = 16.85158533330846
    elif(punto == 'libreria'):
        coordinate['y'] = 41.117926514903615
        coordinate['x'] = 16.85666496047897
    elif(punto == 'ferramenta'):
        coordinate['y'] = 41.1245634831549
        coordinate['x'] = 16.854578321254767
    elif(punto == 'autoricambi'):
        coordinate['y'] = 41.1275981792235
        coordinate['x'] = 16.84802892133656
    
    return coordinate.copy()

def stampa_indicazioni(G, percorso):
    strade = []
    count = 0

    words = ['svolta su', 'prendi', 'gira su', 'imbocca']

    while(count < len(percorso)-1):
        s = percorso[count]
        o = percorso[count +1]
        try:
            strada = G.edges[(s, o, 0)]['name']
            if(strada not in strade):
                strade.append(strada)
        except KeyError:
            pass
        count+=1

    for strada in strade:
        if(isinstance(strada, str)):
            print(words[randint(0,3)], strada)

    print('Destinazione\n')

def get_grafo():
    G = ox.graph_from_address('Bari, BA, IT', dist=3000, network_type='drive')
    return G

def get_nodo(G, y, x):
    nodo = ox.get_nearest_node(G, (y, x))
    return nodo

def percorso_astar(G, nodo_partenza, nodo_destinazione):
        percorso = []
        percorso = nx.astar_path(G, nodo_partenza, nodo_destinazione, weight='length')
        return percorso

def lunghezza_percorso(G, nodo_partenza, nodo_destinazione):
        len = nx.astar_path_length(G, nodo_partenza, nodo_destinazione, weight='length')
        return len
      

def plot_percorso(G, percorso, esecuzione):
    if(esecuzione == 0):
        pt = ox.graph_to_gdfs(G, edges=False).unary_union.centroid
        bbox = ox.utils_geo.bbox_from_point((pt.y, pt.x), dist=3000)

        fig, ax = ox.plot_graph_route(G, percorso, bbox=bbox)
    else:
        colori = ['r', 'y', 'c', 'g', 'b']
        col = []

        for i in range (0,esecuzione+1):
            col.append(colori[i])

        pt = ox.graph_to_gdfs(G, edges=False).unary_union.centroid
        
        bbox = ox.utils_geo.bbox_from_point((41.115274207564624, 16.84751453664305), dist=1400)
        fig, ax = ox.plot_graph_routes(G, percorso, route_colors=col, bbox=bbox)
        


