import streamlit as st
from rdflib import Graph

# Load the RDF ontology
g = Graph()
g.parse("linear_regression.ttl", format="turtle")  # Use the extended TTL file

# Title and intro
st.title("🤖 Leetpandas: Auto-generated ML Questions")
st.markdown("Leetpandas uses Ontologies + SPARQL to auto-generate questions for machine learning topics.")

# Define multiple SPARQL queries and question formats
queries = [
    {
        "title": "Linear Regression",
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?param WHERE {
                :LinearRegression :uses ?param .
            }
        """,
        "template": "What parameter does Linear Regression use? → **{}**"
    },
    {
        "title": "SVM Evaluation",
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?metric WHERE {
                :SVM :evaluatedBy ?metric .
            }
        """,
        "template": "Which evaluation metric is used for SVM? → **{}**"
    },
    {
        "title": "KNN Task",
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?task WHERE {
                :KNN :usedFor ?task .
            }
        """,
        "template": "Which ML task is KNN used for? → **{}**"
    },
    {
        "title": "Linear Regression Assumptions",
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?assumption WHERE {
                :LinearRegression :assumes ?assumption .
            }
        """,
        "template": "What assumption does Linear Regression make? → **{}**"
    },
    {
        "title": "Classification Models",
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?model WHERE {
                ?model :usedFor :Classification .
            }
        """,
        "template": "Which model is used for Classification? → **{}**"
    }
]

# Iterate through queries and render them
for item in queries:
    st.subheader(f"🔹 {item['title']}")
    results = g.query(item["query"])
    for row in results:
        val = list(row)[0]
        label = val.split("#")[-1] if "#" in val else val
        st.markdown(f"• {item['template'].format(label)}")
