import networkx as nx
import matplotlib.pyplot as plt

# Создаём граф
G = nx.MultiGraph()

# Добавляем узлы (вершины графа)
nodes = [1, 2, 3, 4]
G.add_nodes_from(nodes)

# Добавляем рёбра (элементы цепи)
edges = [
    (1, 2, {'name': 'R1', 'resistance': 20}),  # A-B, резистор 2 Ом
    (1, 2, {'name': 'E1', 'voltage': 9}),  # A-B, Источник ЭДС 9 В   
    (2, 3, {'name': 'R2', 'resistance': 8}),  # B-C, резистор 8 Ом 
    (3, 4, {'name': 'R3', 'resistance': 10}),  # C-D, резистор 10 Ом
    (3, 4, {'name': 'R4', 'resistance': 12}),  # C-D, резистор 12 Ом
    #(4, 1, {'name': 'R5', 'resistance': 2}),  # D-A, резистор 2 Ом
    
]         
G.add_edges_from(edges)

# Визуализация графа
pos = nx.spring_layout(G)  # Позиции узлов для визуализации
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=15)
#edge_labels = nx.get_edge_attributes(G, 'name')
#nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')
# Рисуем параллельные рёбра с изгибом
for u, v, key in G.edges(keys=True):
    edge_data = G[u][v][key]
    edge_label = edge_data['name']
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], connectionstyle=f"arc3,rad={0.1 * key}", edge_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): edge_label}, font_color='red')
    
plt.show()

# Поиск мостов
bridges = list(nx.bridges(G))
print("Мосты в графе:", bridges)

# Вывод критических элементов
if bridges:
    print("Критические элементы (мосты):")
    for u, v in bridges:  
        for i in G[u][v]:  
           print(f"Ребро между узлами {u} и {v} ({G[u][v][i]['name']}) является мостом.")
else:
    print("В графе нет мостов.")

# Проверка связности
if nx.is_connected(G):
    print("Граф связный.")
else:
    print("Граф несвязный.")
    print("Число компонент связности:", nx.number_connected_components(G))    

# Находим компоненты связности
components = list(nx.connected_components(G))
print("Компоненты связности:")
for i, component in enumerate(components, 1):
    print(f"Компонента {i}: {component}")    