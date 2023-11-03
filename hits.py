import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

G.add_edges_from([(1,2), (1, 3), (2, 4), (3, 4), (4, 5)])

plt.figure(figsize=(10, 10))
nx.draw_networkx(G, with_labels=True)

hubs, authorities = nx.hits(G, max_iter=50)

print('Hub Scores:', hubs)
print('Authority Scores:', authorities)