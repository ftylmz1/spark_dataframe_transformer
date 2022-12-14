from pyspark.sql import DataFrame

class Drop:
    def __init__(self, column: str) -> None:
        self.column = column
    
    def execute(self, df: DataFrame):
        return df.drop(self.column)