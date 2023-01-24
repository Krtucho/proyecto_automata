import gravis as gv
import streamlit as st
import streamlit.components.v1 as components
import networkx as nx
from Parsing.txt_graph import*
# graph4 = {
#     'graph': {
#         'label': 'Multigraph',
#         'directed': False,
#         'nodes': {
            
            
            
#             1: {'metadata': {'hover': 'Node 1', 'x': 0, 'y': 10}, 'z':10},
#             2: {'metadata': {'hover': 'Node 2', 'x': 0, 'y': 20}, 'z':20},
#             3: {'metadata': {'hover': 'Node 3', 'x': 0, 'y': 30}, 'z':30},
#             4: {'metadata': {'hover': 'Node 4', 'x': 0, 'y': 40}, 'z':40},
#             5: {'metadata': {'hover': 'Node 5', 'x': 0, 'y': 50}, 'z':50},
#             6: {'metadata': {'hover': 'Node 6', 'x': 0, 'y': 60}, 'z':60},
#         },
#         # 'edges': [
#         #     {'source': 1, 'target': 2},
#         #     {'source': 2, 'target': 3},
#         #     {'source': 2, 'target': 2, 'metadata': {'color': 'blue'}},
#         #     {'source': 3, 'target': 4},
#         #     {'source': 3, 'target': 3, 'metadata': {'color': 'blue'}},
#         #     {'source': 4, 'target': 5},
#         #     {'source': 4, 'target': 4, 'metadata': {'color': 'blue'}},
#         #     {'source': 5, 'target': 1, 'metadata': {'color': 'red'}},
#         #     {'source': 5, 'target': 1, 'metadata': {'color': 'red'}},
#         #     {'source': 1, 'target': 6, 'metadata': {'color': 'red'}},
#         #     {'source': 1, 'target': 6, 'metadata': {'color': 'red'}},
#         #     {'source': 6, 'target': 1, 'metadata': {'color': 'red'}},
#         #     {'source': 2, 'target': 6},
#         #     {'source': 3, 'target': 6, 'metadata': {'color': 'red'}},
#         #     {'source': 6, 'target': 3, 'metadata': {'color': 'red'}},
#         #     {'source': 4, 'target': 6, 'metadata': {'color': 'red'}},
#         #     {'source': 6, 'target': 4, 'metadata': {'color': 'red'}},
#         #     {'source': 5, 'target': 6},
#         # ],
#         #'metadata': {'node_color': '#aaa', 'node_border_size': 1.2, 'edge_size': 1.2}
#     }
# }
#fig = gv.d3(graph4, graph_height=200, edge_curvature=0.3, show_node_label=False)

#Ejemplo de uso
graph5 = nx.Graph()
graph5.graph['node_color'] = 'green'
graph5.add_node(0,x =0,y=10,color='red')
graph5.add_node(1,x =0,y=20)
graph5.add_node(2,x =0,y=30)
graph5.graph['node_size'] = '5'
graph5.nodes[0]['color'] = 'blue'
#parser(-1,graph5)
#fig = gv.three(graph5, use_edge_size_normalization=True,show_node_label=False)
#graph5.add_edge('000','001')
#graph5.add_edge('001','002')
fig = gv.d3(graph5, graph_height=500,use_edge_size_normalization=True, edge_curvature=0.3, show_node_label=False)
components.html(fig.to_html(), height=1000)