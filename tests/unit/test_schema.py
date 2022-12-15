import pytest

from spark_transformer.utilizers.spark_utilizer import first


def test_check_if_schema_exists():
    dt = [('id', 'bigint'), ('name', 'string'), ('surname', 'string')]
    r =  first(dt, 'id', 'bigint')
    e = ('id', 'bigint')

    assert r == e, "there is problem"


def test_json_serializer():

    import jsonpickle
    from spark_transformer.tranformations.executor import Executor
    from spark_transformer.tranformations.drop import Drop
    from spark_transformer.tranformations.hash import Hash

    spark = None
    executor = Executor(spark)
    hash_column = Hash('surname')
    drop_column = Drop('name')


    transformation_list = [hash_column]

    transformation_list_pickled = jsonpickle.encode(transformation_list)
    transformation_list_unpickled = jsonpickle.decode(transformation_list_pickled)

    print(transformation_list_pickled)

    assert 1 == 1