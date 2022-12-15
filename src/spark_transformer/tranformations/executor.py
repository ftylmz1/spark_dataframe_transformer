from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


class Executor:
    def __init__(self, spark: SparkSession) -> None:
        self.spark = spark
    
    def apply(self, df, transformer) -> DataFrame:
        return transformer.execute(df)

    def apply_bulk(self, df, transformations) -> DataFrame:
        
        df_temp = df
        
        for x in transformations:
            print(x.column)
            df_temp = self.apply(df_temp, x)

        return df_temp
