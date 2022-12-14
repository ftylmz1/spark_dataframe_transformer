from pyspark.sql import DataFrame
from pyspark.sql.functions import sha2

class Hash:
    def __init__(self, column: str) -> None:
        self.column = column
    
    def execute(self, df: DataFrame):
        return df.withColumn(self.column, sha2(self.column, 256))
