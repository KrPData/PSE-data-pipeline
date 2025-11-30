import pandas as pd
import numpy as np
from datetime import datetime as dt
from config.pse_script_config import PseScriptConfig
from config.pse_api_config import PseApiConfig
from config.proxy_config import Proxy_config
from extract.fetch_data import FetchData

class PseExtract():

    def __init__(self, report_variant):
        self.report_variant = report_variant
        self.pse_script_config = PseScriptConfig(self.report_variant)

    def read_csv(self: int) -> pd.DataFrame:
        df_csv = pd.read_csv(
        filepath_or_buffer=PseScriptConfig(self.report_variant).csv_filepath[self.report_variant],
        sep = ",",
        decimal="."
        )

        return df_csv

    
    def set_datetime_range(self, df: pd.DataFrame):

        pse_script_config = self.pse_script_config

        last_date = pd.to_datetime(df["datetime"].tail(n=1)).dt.strftime(date_format="%Y-%m-%d").values[0]

        last_date = np.datetime64(last_date)

        today = np.datetime64(dt.now().replace(hour=23, minute=59, second=59, microsecond=59))
        time_diff = (today - last_date) / np.timedelta64(1, 'h')
        
        gradation = pse_script_config.records_gradation[self.report_variant]
        time_sequence = pse_script_config.report_time_sequence()
        
        final_records_num = [round(time_diff) * 4 if time_sequence == "quarter" else round(time_diff)][0]

        if self.report_variant == 9:
            final_records_num = 100000

        if final_records_num <= 0:
            print(f"Brak danych dla raportu wariant: {self.report_variant}")
        
        return [last_date, today, final_records_num]

    def set_url(self, params: list):
        last_date, today, recods_num = params
        url = PseApiConfig(self.report_variant).variant_url(last_date, today, recods_num)
        return url

    def get_data(self, url):
        data = FetchData(proxies=Proxy_config().get_proxies(), link=url).get_data()
        print(url)
        return data

