import pandas as pd
from config import pse_script_config
from  sqlalchemy import create_engine
import os
from dotenv import load_dotenv

class PseLoadData():

    def __init__(self, data: pd.DataFrame, report_variant):
        self.data = data
        self.report_variant = report_variant
        self.report = pse_script_config.PseScriptConfig(self.report_variant)

        load_dotenv()
        self.db_host = os.getenv("DB_HOST")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASS")
        self.db_name = os.getenv("DB_NAME")
        self.db_port = os.getenv("DB_PORT")
        self.engine = create_engine(f"postgresql+psycopg2://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")

    def save_to_csv(self):
        df = self.data

        df.to_csv(path_or_buf=self.report.csv_filepath[self.report_variant], 
                        sep=",", decimal=".", header=False, mode="a", index=False)
        
        print(f"{self.report_variant} report processed and saved in csv")

    def save_to_psql_database(self):
        df = self.data

        df.to_sql(pse_script_config.PseScriptConfig.staging_tables[self.report_variant], self.engine, if_exists="append", index=False, schema="market_data")

        print(f"{self.report_variant} report processed and saved in sql database")