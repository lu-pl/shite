from pyshacl import validate
import pytest
from rdflib import BNode, RDF, SH, URIRef

from lodkit import ttl
from tests.utils import SHITE


data_shapes_graph_fail_1 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["if"], BNode()),
).to_graph()

data_shapes_graph_fail_2 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["then"], BNode()),
).to_graph()

data_shapes_graph_fail_3 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["else"], BNode()),
).to_graph()

data_shapes_graph_fail_4 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (SHITE["then"], BNode()),
    (SHITE["else"], BNode()),
).to_graph()

data_shapes_graph_fail_5 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        SH.property,
        [
            (SHITE["if"], BNode()),
        ],
    ),
).to_graph()

data_shapes_graph_fail_6 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        SH.property,
        [
            (SHITE["then"], BNode()),
        ],
    ),
).to_graph()

data_shapes_graph_fail_7 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        SH.property,
        [
            (SHITE["else"], BNode()),
        ],
    ),
).to_graph()

data_shapes_graph_fail_8 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        URIRef("urn:not_sh_property"),
        [
            (SHITE["if"], BNode()),
            (SHITE["then"], BNode()),
        ],
    ),
).to_graph()

data_shapes_graph_fail_9 = ttl(
    URIRef("urn:Shape"),
    (RDF.type, SH.NodeShape),
    (
        URIRef("urn:not_sh_property"),
        [
            (SHITE["if"], BNode()),
            (SHITE["then"], BNode()),
            (SHITE["else"], BNode()),
        ],
    ),
).to_graph()

data_shapes_graph_fail_10 = ttl(
    URIRef("urn:Shape"),
    (SHITE["if"], BNode()),
    (SHITE["then"], BNode()),
).to_graph()


data_shapes_graphs_failing = [
    data_shapes_graph_fail_1,
    data_shapes_graph_fail_2,
    data_shapes_graph_fail_3,
    data_shapes_graph_fail_4,
    data_shapes_graph_fail_5,
    data_shapes_graph_fail_6,
    data_shapes_graph_fail_7,
    data_shapes_graph_fail_8,
    data_shapes_graph_fail_9,
    data_shapes_graph_fail_10,
]


@pytest.mark.parametrize("data_shapes_graph", data_shapes_graphs_failing)
def test_shite_grammar_fail(data_shapes_graph, shite_shapes_graph):
    conforms, *_ = validate(
        data_graph=data_shapes_graph, shacl_graph=shite_shapes_graph
    )

    assert not conforms
