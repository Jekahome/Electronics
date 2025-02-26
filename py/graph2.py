import pygraphviz as pgv
import networkx as nx
from PIL import Image

# Создаем граф с помощью PyGraphviz
A = pgv.AGraph(strict=False, directed=False)

# Добавляем узлы
nodes = [1, 2, 3, 4]
A.add_nodes_from(nodes)

# Добавляем рёбра с элементами цепи
edges = [
    (1, 2, {'name': 'R1', 'label': 'R1, 20Ω'}),
    (1, 2, {'name': 'E1', 'label': 'E1, 9V'}),
    (2, 3, {'name': 'R2', 'label': 'R2, 8Ω'}),
    (3, 4, {'name': 'R3', 'label': 'R3, 10Ω'}),
    (3, 4, {'name': 'R4', 'label': 'R4, 12Ω'}),
    #(4, 1, {'name': 'R5', 'label': 'R5, 2Ω'}),
]

# Добавляем рёбра в граф
for u, v, data in edges:
    A.add_edge(u, v, label=data['label'])

# Визуализация графа и сохранение в файл
A.layout(prog='dot')  # Используем алгоритм dot для построения схемы
A.draw('/tmp/circuit_graph.png')
img = Image.open('/tmp/circuit_graph.png')
img.show()

# Дополнительно: поиск мостов и связности с помощью networkx
G = nx.Graph()
G.add_edges_from([(u, v) for u, v, _ in edges])

# Поиск мостов
bridges = list(nx.bridges(G))
print("Мосты в графе:", bridges)

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

print("Граф сохранен как 'circuit_graph.png'.")