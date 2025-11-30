import pandas as pd
from datetime import datetime as dt

class Utils():

    def read_csv_file(path: str) -> pd.DataFrame:
    
        df = pd.read_csv(filepath_or_buffer= 
                            rf"{path}", 
                            delimiter=";",
                            decimal=",",
                            date_format="%d.%m.$Y"
                        )
        
        return df

    def save_in_csv_excel_format(df: pd.DataFrame, path: str):
        
        df.to_csv(
            path_or_buf=path, 
            sep=";", 
            decimal=",", 
            header=False, 
            mode="a", 
            index=False
            )
        
    def format_date(date):
        
        if date[:5][-1] == "-":
            d1 = dt.strptime(date, "%Y-%m-%d")
            return d1
        
        if date[:3][-1] == ".":
            d1 = dt.strptime(date, "%d.%m.%Y")
            d2 = dt.strftime(d1, "%Y-%m-%d")
            return d2
        
    def is_dataframe(obj):

        if not isinstance(obj, pd.DataFrame):
            raise TypeError("Expected pandas dataframe")
