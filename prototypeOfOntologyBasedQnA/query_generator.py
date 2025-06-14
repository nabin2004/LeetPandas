from rdflib import Graph

# Load the RDF ontology
g = Graph()
g.parse("ml_ontology.ttl", format="turtle")  # Use the extended ontology file

# Define multiple SPARQL queries with their question templates
queries = [
    {
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?param WHERE {
                :LinearRegression :uses ?param .
            }
        """,
        "template": "What parameter does Linear Regression use? → {}"
    },
    {
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?metric WHERE {
                :SVM :evaluatedBy ?metric .
            }
        """,
        "template": "Which evaluation metric is used for SVM? → {}"
    },
    {
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?task WHERE {
                :KNN :usedFor ?task .
            }
        """,
        "template": "Which ML task is KNN used for? → {}"
    },
    {
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?assumption WHERE {
                :LinearRegression :assumes ?assumption .
            }
        """,
        "template": "What assumption does Linear Regression make? → {}"
    },
    {
        "query": """
            PREFIX : <http://leetpandas.org/ml#>
            SELECT ?model WHERE {
                ?model :usedFor :Classification .
            }
        """,
        "template": "Which model is used for Classification? → {}"
    }
]

# Run and print results
print("Generated Questions:\n")
for item in queries:
    res = g.query(item["query"])
    for row in res:
        val = list(row)[0]
        short_name = val.split("#")[-1] if "#" in val else val
        print(item["template"].format(short_name))
