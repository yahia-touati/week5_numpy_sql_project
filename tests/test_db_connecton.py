import pytest
from db_connection import get_engine
from sqlalchemy import Engine

def test_get_engine_return_engine_object():
    engine = get_engine()
    assert isinstance(engine, Engine)

def test_engine_can_connect_to_datavase():
    """Test that the engine can successfuly"""
    engine = get_engine()
    #try to open a connection
    with engine.connect() as conn:
        assert conn is not None