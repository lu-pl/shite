"""Global fixture definitions."""

import pytest
from rdflib import Graph

import lodkit
from shite import shite_shapes


@pytest.fixture()
def shite_shapes_graph() -> Graph:
    return shite_shapes
