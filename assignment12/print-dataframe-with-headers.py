import pandas as pd

class DFPlus(pd.DataFrame):
    @property
    def _constructor(self):
        return DFPlus

    @classmethod
    def from_csv(cls, filepath, **kwargs):
        df = pd.read_csv(filepath, **kwargs)
        return cls(df)

    def print_with_headers(self):
        total = len(self)
        i = 0
        while i < total:
            print(self.columns.tolist())
            print(super().iloc[i:i+10]) 
            i += 10

dfp = DFPlus.from_csv("../csv/products.csv")

dfp.print_with_headers()