import matplotlib.pyplot as plt
import networkx as nx
import time

# Mapitaaaa
mapita_de_rumania = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Pitesti', 97), ('Craiova', 146)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Urziceni', 85), ('Giurgiu', 90)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

# Para la forma grafica
G = nx.Graph()
for ciudad, conexiones in mapita_de_rumania.items():
    for destino, costo in conexiones:
        G.add_edge(ciudad, destino, weight=costo)

# Posiciones de cada ciudad (traté de que se vea parecido xd)
pos = {
    'Arad': (-6, 3), 'Zerind': (-5.5, 4), 'Oradea': (-4.5, 5), 'Timisoara': (-6, 1),
    'Lugoj': (-4.5, 0), 'Mehadia': (-4.5, -1), 'Dobreta': (-4.7, -2.3), 'Craiova': (-2, -2.5),
    'Sibiu': (-3, 2), 'Rimnicu Vilcea': (-2.5, 0.8), 'Fagaras': (-1, 1.8), 'Pitesti': (-0.5, -0.3),
    'Bucharest': (1.8, -1), 'Giurgiu': (1, -3), 'Urziceni': (3.5, -0.5), 'Hirsova': (5.5, -0.5),
    'Eforie': (6.5, -2.5), 'Vaslui': (4.5, 1.8), 'Iasi': (3.5, 3.5), 'Neamt': (1.5, 4.5)
}

def dibujar_grafo(camino_recorrido, nodo_actual=None):
    plt.clf()                                                                                                   # Limpiar la figura
    plt.title("Búsqueda Uniforme - Mapa de Rumania - Proyecto final")                                           # Titulo de la graf
    nx.draw(G,pos,with_labels=True,node_size=600,node_color="lightgrey",font_size=8,font_weight="bold")         # Diubja los nodos
    nx.draw_networkx_edge_labels(G,pos,edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)}, font_size=7)    

    # Para resaltar el camnio
    camino_pasado = list(zip(camino_recorrido, camino_recorrido[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=camino_pasado, edge_color="green", width=3)
    if nodo_actual: # Resaltar el nodo actual
        nx.draw_networkx_nodes(G,pos,nodelist=[nodo_actual],node_color="lightgreen", node_size=700)
    plt.pause(0.5)  

def busqueda_uniforme_grafica(mapa, inicio, destino):
    frontera = [(0, inicio, [inicio])]
    visitados = set()

    while frontera:
        # Ordenar para obtener el nodo con el menor costo acumulado
        frontera.sort(key=lambda x: x[0])
        costo, ciudad, camino = frontera.pop(0)

        # Dibujar el grafo en cada paso con el camino recorrido y el nodo actual
        dibujar_grafo(camino, nodo_actual=ciudad)
        
        # Verificar si hemos llegado al destino
        if ciudad == destino:
            print("\n\t==--==--==--==--==--== (Ruta encontrada) ==--==--==--==--==--==")
            print(f"\t :: Mejor camino: {camino}\n\t :: Costo: {costo} km\n")
            dibujar_grafo(camino)  # S dibuja el camino final completo
            return costo, camino

        # Marcar la ciudad como visitada
        visitados.add(ciudad)

        # Expandir los vecinos
        for vecino, costo_camino in mapa[ciudad]:
            if vecino not in visitados:
                frontera.append((costo + costo_camino, vecino, camino + [vecino]))
    print("No se encontró un camino.")
    return None

def elegir_ciudades():
    ciudades_temp = list(mapita_de_rumania.keys())  # Creamos una lista temporal para acceder con numero
    for i, ciudad in enumerate(mapita_de_rumania.keys(), start=1):  # Imprime las ciudades enumeradas
        print(f"\t{i}. {ciudad}")
    origen = int(input("\n\t :> Ingresa el NUMERO de la ciudad ORIGEN: "))
    destino = int(input("\t :> Ingresa el NUMERO de la ciudad DESTINO: "))
    # Asignamos la ciudad segun el numero
    ciudad_origen = ciudades_temp[origen-1]
    ciudad_destino = ciudades_temp[destino-1]
    print(f"\t :: Ruta de {ciudad_origen} -> {ciudad_destino} ")
    return ciudad_origen, ciudad_destino

print("\n\t==--==--==--==--==--==--==--==--==--==--==---==--==--==--==--==--==")
print("\t==--==--==--==--==--== ( PROYECTO FINAL IA ) ==--==--==--==--==--==\n")

plt.figure(figsize=(10, 7))
origen, destino = elegir_ciudades()
costo, camino = busqueda_uniforme_grafica(mapita_de_rumania,origen,destino)
plt.show()
