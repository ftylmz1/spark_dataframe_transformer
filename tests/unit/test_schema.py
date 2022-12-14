import pytest

from spark_transformer.utilizers.spark_utilizer import first


import sys, os

# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.insert(0, os.path.dirname(__file__))



def check_data_type(dt, column, type):
    filter(lambda x: x[0] == column) 



def test_check_if_schema_exists():
    dt = [('id', 'bigint'), ('name', 'string'), ('surname', 'string')]
    r =  first(dt, 'id', 'bigint')
    e = ('id', 'bigint')

    assert r == e, "there is problem"


def test_simple():
    assert 1 == 2, "why is that?"