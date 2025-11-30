from extract.pse_extract import PseExtract
from transform.pse_transform import PseTransform
from load.pse_load import PseLoadData

# Warianty raportów
# 1 - zapotrzebowanie, generacja KSE
# 2 - ceny mocy bilansujacych nabytych w trybie podstawowym
# 3 - wielkości mocy bilansujących nabytych w trybie podstawowym
# 4 - wielkości mocy bilansujących nabytych w trybie uzupełniającym
# 5 - ceny mocy bilansujących nabytych w trybie uzupełniającym
# 8 - nierynkowe redysponowanie OZE

variants_to_get = [1,2,3,4,5,8]

for variant in variants_to_get:

    pse_extract = PseExtract(variant)
    df_c_data = pse_extract.read_csv()
    values = pse_extract.set_datetime_range(df=df_c_data)

    if values[2] <= 0:
        continue

    url = pse_extract.set_url(params=values)

    pse_data = pse_extract.get_data(url=url)

    pse_transform = PseTransform(variant, pse_data)
    df_pse = pse_transform.transform_to_dataframe()
    
    if df_pse.empty:
        print(df_pse, f"Brak danych: {variant}")
        continue

    df_pse = pse_transform.search_date_column()
    df_pse = pse_transform.merge_time_series()
    df_pse = pse_transform.set_appropriate_columns()
    df_pse = pse_transform.standarize_oreb_columns()
    df_pse = pse_transform.melt_DataFrame()
    df_pse = pse_transform.change_data_types()
    df_pse = pse_transform.format_dates()
    df_pse = pse_transform.deduplicate_data(system_df=df_c_data)
    df_pse = pse_transform.rename_columns(system_df=df_c_data)
    df_pse = pse_transform.sort_data()

    PseLoadData(data=df_pse, report_variant=variant).save_to_csv()
    PseLoadData(data=df_pse, report_variant=variant).save_to_psql_database()
    