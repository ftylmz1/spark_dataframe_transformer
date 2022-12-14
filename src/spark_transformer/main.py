from __future__ import print_function


from pyspark import SparkConf
from pyspark.sql import SparkSession

from tranformations.executor import Executor
from tranformations.drop import Drop
from tranformations.hash import Hash


import json
from json import JSONEncoder
try:
    from types import SimpleNamespace as Namespace
except ImportError:
    # Python 2.x fallback
    from argparse import Namespace


spark = (SparkSession.builder
                     .master('local[*]')
                     .appName("base-test")
                     .getOrCreate())


path = 'data/people.json'
df = spark.read.json(path)



executor = Executor(spark)
hash_column = Hash('surname')
drop_column = Drop('name')


df = executor.apply(df, drop_column)
df = executor.apply(df, hash_column)

df.show(truncate=False)



print('PySpark Version :'+spark.version)
print('PySpark Version :'+spark.sparkContext.version)