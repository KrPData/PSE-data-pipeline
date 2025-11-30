import pandas as pd

class getCSVData:

    def read_csv_last_date(self, dir: str, sep: str, date_column_name: str):
        df = pd.read_csv(dir, sep=sep)
        last_date = df[date_column_name].iloc[-1]
        return last_date