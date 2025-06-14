import streamlit as st
from rdflib import Graph
from pyvis.network import Network
import streamlit.components.v1 as components

# Load RDF graph
g = Graph()
g.parse("linear_regression.ttl", format="turtle")

# Build PyVis graph
net = Network(height="600px", width="100%", bgcolor="#222222", font_color="white")

for s, p, o in g:
    s_label = s.split("#")[-1]
    p_label = p.split("#")[-1]
    o_label = o.split("#")[-1]

    net.add_node(s_label, label=s_label)
    net.add_node(o_label, label=o_label)
    net.add_edge(s_label, o_label, label=p_label)

# Save and read as HTML
net.save_graph("kg.html")
HtmlFile = open("kg.html", "r", encoding="utf-8").read()

# Display in Streamlit
st.title("ML Knowledge Graph Visualization")
components.html(HtmlFile, height=650, scrolling=True)
