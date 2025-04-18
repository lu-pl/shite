"""Grammar pass tests for shite shapes."""

from pyshacl import validate
import pytest
from rdflib import BNode, RDF, SH, URIRef

from lodkit import ttl
from tests.utils import SHITE


data_shapes_graph_pass_1 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["if"], BNode()),
    (SHITE["then"], BNode()),
).to_graph()

data_shapes_graph_pass_2 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["if"], BNode()),
    (SHITE["then"], BNode()),
    (SHITE["else"], BNode()),
).to_graph()

data_shapes_graph_pass_3 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["else"], BNode()),
    (SHITE["if"], BNode()),
    (SHITE["then"], BNode()),
).to_graph()

data_shapes_graph_pass_4 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["then"], BNode()),
    (SHITE["if"], BNode()),
).to_graph()

data_shapes_graph_pass_5 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        SH.property,
        [
            (SHITE["if"], BNode()),
            (SHITE["then"], BNode()),
        ],
    ),
).to_graph()

data_shapes_graph_pass_6 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        SH.property,
        [
            (SHITE["if"], BNode()),
            (SHITE["then"], BNode()),
            (SHITE["else"], BNode()),
        ],
    ),
).to_graph()

data_shapes_graph_pass_7 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        SH.property,
        [
            (SHITE["then"], BNode()),
            (SHITE["if"], BNode()),
            (SHITE["else"], BNode()),
        ],
    ),
).to_graph()


data_shapes_graphs = [
    data_shapes_graph_pass_1,
    data_shapes_graph_pass_2,
    data_shapes_graph_pass_3,
    data_shapes_graph_pass_4,
    data_shapes_graph_pass_5,
    data_shapes_graph_pass_6,
    data_shapes_graph_pass_7,
]


@pytest.mark.parametrize("data_shapes_graph", data_shapes_graphs)
def test_shite_grammar_pass(data_shapes_graph, shite_shapes_graph):
    conforms, *_ = validate(
        data_graph=data_shapes_graph, shacl_graph=shite_shapes_graph
    )

    assert conforms
