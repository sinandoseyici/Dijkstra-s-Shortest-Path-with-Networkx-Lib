import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_nodes_from([0,1,2,3,4])

G.add_edge(0,4,weight =2.0)
G.add_edge(0,2,weight =3.0)
G.add_edge(0,1,weight =5.0)
G.add_edge(4,3,weight =4.0)
G.add_edge(4,2,weight =10.0)
G.add_edge(4,1,weight =6.0)
G.add_edge(2,3,weight =2.0)
G.add_edge(1,3,weight =6.0)
G.add_edge(2,1,weight=1.0)
G.add_edge(1,2,weight=2.0)

G.nodes[0]['pos'] = (0,1.5)
G.nodes[1]['pos'] = (1,0.75)
G.nodes[2]['pos'] = (0.5,0)
G.nodes[3]['pos'] = (-0.5,0)
G.nodes[4]['pos'] = (-1,0.75)

dp40_1 = " 4'ten 0'a yol yok!\n---------------------------"
dp41_1 = nx.dijkstra_path(G,source = 4, target = 1)
dp42_1 = nx.dijkstra_path(G,source = 4, target = 2)
dp43_1 = nx.dijkstra_path(G,source = 4, target = 3)
print(dp40_1)
print(" 4'ten 1'e en yakın yol:\n",dp41_1,"\n---------------------------")
print(" 4'ten 2'ye en yakın yol:\n",dp42_1,"\n---------------------------")
print(" 4'ten 3'e en yakın yol:\n",dp43_1,"\n---------------------------")

#G.remove_node(3)

dp40_2 = "4'ten 0'a yol yok!"
dp41_2 = nx.dijkstra_path(G,source = 4, target = 1)
dp42_2 = nx.dijkstra_path(G,source=4,target=2)
dp43_2 = " 4'ten 3'e yol yok! 3 Node'u silindi!"
print("**********2.DURUM**********\n\n",dp40_2,"\n---------------------------")
print(" 4'ten 1'e en yakın yol:\n",dp41_2,"\n---------------------------")
print(" 4'ten 2'ye en yakın yol:\n",dp42_2,"\n---------------------------")
print(dp43_2)

node_pos=nx.get_node_attributes(G,'pos')
labels=nx.get_edge_attributes(G,'weight')
nx.draw_networkx_nodes(G,node_pos,node_size=350)
nx.draw_networkx_edges(G, node_pos,connectionstyle='arc3, rad = -0.11', edgelist = [(1,2)], width = 2, alpha = 1, edge_color='b')
nx.draw_networkx_edge_labels(G,node_pos,edge_labels=labels,label_pos=0.7,font_size=9,verticalalignment="center_baseline")
nx.draw(G, node_pos, with_labels=True)

plt.show()
