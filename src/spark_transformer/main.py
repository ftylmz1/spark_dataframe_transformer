from pyspark import SparkConf
from pyspark.sql import SparkSession

from tranformations.executor import Executor
from utilizers.transformation_helper import TransformationHelper

# parameters
path = 'data/people.json'
transformation_path = 'data/transformations.json'

# configurations
transformations = TransformationHelper().get_transformations_from_json_file(transformation_path)


# set up 
spark = (SparkSession.builder
                     .master('local[*]')
                     .appName("base-test")
                     .getOrCreate())

df = spark.read.json(path)


# Dataframe transformations
executor = Executor(spark)
df = executor.apply_bulk(df, transformations)


# result 
df.show(truncate=False)
