from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


class Executor:
    def __init__(self, spark: SparkSession) -> None:
        self.spark = spark
    
    def apply(self, df, transformer) -> DataFrame:
        return transformer.execute(df)
