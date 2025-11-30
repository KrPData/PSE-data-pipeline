import pandas as pd
from config import pse_script_config
from utils.utils import Utils

class PseTransform():

    def __init__(self, report_variant, data: dict):
        self.report_variant = report_variant
        self.data = data
        self.report_time_sequence = pse_script_config.PseScriptConfig(self.report_variant).report_time_sequence()

    def transform_to_dataframe(self):
        if not isinstance(self.data, dict):
            raise TypeError("Expected dictionary")
        
        df = pd.DataFrame(data=self.data["value"])
        self.data = df

        return df

    def search_date_column(self) -> pd.DataFrame:
        Utils.is_dataframe(self.data)

        period_patterns = [r'^\d{2} - \d{2}$', r'^\d{2}:\d{2} - \d{2}:\d{2}$']

        if self.report_variant == 9:
            period_patterns = [r'^\d{2}$']

        df = self.data
        for pattern in period_patterns:
            for col in df.columns:
                if df[df[col].astype(str).str.contains(pattern, regex=True) == True].empty == False:
                    df.rename(columns={col : "period"}, inplace=True)

        df["period"] = df["period"].str.replace(" ", "")
        self.data = df

        return df
    
    def merge_time_series(self) -> pd.DataFrame:
        Utils.is_dataframe(self.data)

        df_oreb = pd.read_csv(r"helpers_data\zakresy_oreb.csv", sep=",")
        df_godziny = pd.read_csv(r"helpers_data\zakres_godzin.csv", sep=",")
        df_godziny_zaof = pd.read_csv(r"helpers_data\zakres_godzin_zaof.csv", sep=",", converters={"period" : str})

        if self.report_variant == 9:
            df_godziny = df_godziny_zaof

        df = self.data.merge([df_oreb if self.report_time_sequence == "quarter" else df_godziny][0], on="period", how="left")
        self.data = df
        return df
    
    def set_appropriate_columns(self) -> pd.DataFrame:
        Utils.is_dataframe(self.data)

        df = self.data[list([x for x, y in pse_script_config.PseScriptConfig(self.report_variant).
                             target_df_columns.items() if self.report_variant in y][0])]
        self.data = df
        return df

    
    def standarize_oreb_columns(self) -> pd.DataFrame:
        Utils.is_dataframe(self.data)

        df = self.data

        if self.report_time_sequence == "quarter":
            df.rename(columns={"period" : "oreb"}, inplace=True)
            df["oreb"] = df["oreb"].astype("str")
            self.data = df
            return df


        
    def melt_DataFrame(self):
            Utils.is_dataframe(self.data)

            df = self.data

            columns_to_melt = ["business_date", "hour"]
            
            if self.report_variant == 9:
                columns_to_melt = ["business_date", "hour", "reserve_type"]

            df = pd.melt(df, id_vars=[
                ["business_date", "hour", "oreb"] if self.report_time_sequence == "quarter" else columns_to_melt][0],
                var_name="var_1",
                value_name="value"
            )
            self.data = df
            return df
        
    def change_data_types(self):
        Utils.is_dataframe(self.data)

        df = self.data
        
        df["business_date"] = df["business_date"].astype("str")
        df["hour"] = df["hour"].astype("int")
        df["var_1"] = df["var_1"].astype("str")
        df["value"] = df["value"].astype("float")
        self.data = df
        return df
    
    def format_dates(self):
        Utils.is_dataframe(self.data)

        df = self.data

        if self.report_time_sequence == "quarter":
            df_timedelta = pd.to_timedelta(arg=df["oreb"].str.split("-").str[0]+":00")
        else: 
            df_timedelta = pd.to_timedelta(arg = "0" + df["hour"].astype(str) + ":00:00")

        df["datetime"] = pd.to_datetime(arg=df["business_date"],
                                                errors="raise",
                                                yearfirst=True,
                                                format="%Y-%m-%d"
                                                ) + df_timedelta

        if self.report_variant == 9:
            df = df[["datetime", "reserve_type", "var_1", "value"]]
        else:
            df = df[["datetime", "var_1", "value"]]

        self.data = df
        return df

    def deduplicate_data(self, system_df):
        Utils.is_dataframe(self.data)

        df = self.data

        df["d_key"] = df[["datetime", "var_1"]].astype(str).agg("_".join, axis=1)
        system_df["d_key"] = system_df[[col for col in system_df.columns[:2]]].astype(str).agg("_".join, axis=1)
        df = df[~df["d_key"].isin(system_df["d_key"])].drop(columns="d_key")
        system_df.drop(columns="d_key", inplace=True)
        self.data = df
        return df
    
    def rename_columns(self, system_df):
        Utils.is_dataframe(self.data)

        df = self.data
        df.columns = system_df.columns
        return df

    
    def replace_last_day_data(self, system_df):
        Utils.is_dataframe(self.data)

        system_df["datetime"].tail(n=1).values[0]
        
        df = self.data

    
    def sort_data(self):
        Utils.is_dataframe(self.data)

        df = self.data
        df.sort_values(by=["datetime"], ascending=True, inplace=True, ignore_index=True)

        return df
