import pytest

from spark_transformer.utilizers.spark_utilizer import first


def test_check_if_schema_exists():
    dt = [('id', 'bigint'), ('name', 'string'), ('surname', 'string')]
    r =  first(dt, 'id', 'bigint')
    e = ('id', 'bigint')

    assert r == e, "there is problem"
