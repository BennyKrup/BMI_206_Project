# %%
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


# %%
File_name = '12859_2019_2897_MOESM2_ESM.xlsx'

sheet_names = pd.ExcelFile(File_name).sheet_names
sheets = {}
for sheet in sheet_names:
    sheets[sheet] = pd.read_excel(File_name,sheet_name=sheet,index_col=0)
#load the graphs into a dictionary
graphs = {}
for sheet in sheet_names:
    graphs[sheet] = nx.from_pandas_adjacency(sheets[sheet],create_using=nx.DiGraph)
    

# %%
edges = []
nodes = []
for sheet in sheet_names:
    edges.append(len(graphs[sheet].edges))
    nodes.append(len(graphs[sheet].nodes))
fig, ax = plt.subplots(figsize=(20,10))
x = np.arange(len(sheet_names))
width = 0.35
rects1 = ax.bar(x - width/2, nodes, width, label='Nodes')
rects2 = ax.bar(x + width/2, edges, width, label='Edges')
ax.set_ylabel('Number')
ax.set_title('Number of nodes and edges for each graph')
ax.set_xticks(x)
ax.set_xticklabels(sheet_names)
ax.legend()
plt.rcParams.update({'font.size': 15})

plt.show()
fig.savefig('Node_edges.png')


# %%
node_degrees = []
for sheet in sheet_names:
    node_degrees.append(list(dict(nx.degree(graphs[sheet])).values()))

fig, ax = plt.subplots(figsize=(20,10))
ax.boxplot(node_degrees)
ax.set_xticklabels(sheet_names)
ax.set_ylabel('Node degree')
ax.set_title('Node degree distribution for each graph')
plt.rcParams.update({'font.size': 13})
plt.show()
#save
fig.savefig('Node_degree.png')


# %%



