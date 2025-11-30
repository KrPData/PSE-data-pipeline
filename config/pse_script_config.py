class PseScriptConfig:

    def __init__(self, report_variant):
        self.report_variant = report_variant

    csv_filepath = {
        1 : r"cleared data\zap_gen_kse_15min.csv",
        2 : r"cleared data\mb_podst_cena.csv",
        3 : r"cleared data\mb_podst_wielkosc.csv",
        4 : r"cleared data\mb_uzup_wielkosc.csv",
        5 : r"cleared data\mb_uzup_cena.csv", 
        8 : r"cleared data\nierynkowe_red.csv"
    }

    records_gradation = {
        1 : 30,
        2 : 8,
        4 : 8,
        5 : 8,
        3 : 8,
        8 : 30,
        9 : 8
    }

    staging_tables = {
        1 : "staging_zap_gen",
        2 : "staging_mb_podst_cena",
        3 : "staging_mb_podst_wielkosc",
        4 : "staging_mb_uzup_wielkosc",
        5 : "staging_mb_uzup_cena",
        8 : "staging_nierynkowe_red"
    }

    time_sequence = {
        "quarter" : [1, 4, 5, 8],
        "hour" : [2, 3, 9]
    }

    target_df_columns = {
        ("business_date", "period", "hour", "demand", "swm_p", "swm_np", "jg", "jgw1", "jgw2", "jgm1", "jgm2", "jgz1", "jgz2", "jgz3", "jga", "pv", "wi", "jnwrb") : [1],
        ("business_date", "hour", "fcr_g", "fcr_d", "afrr_g", "afrr_d", "mfrrd_g", "mfrrd_d", "rr_g", "rr_d") : [2, 3],
        ("business_date", "period", "hour", "fcr_g", "fcr_d", "afrr_g", "afrr_d", "mfrrd_g", "mfrrd_d") : [4, 5],
        ("business_date", "period", "hour", "pv_red_balance", "wi_red_balance", "pv_red_network", "wi_red_network") : [8],
        ("business_date", "hour", "reserve_type", "pom", "com") : [9]
    }

    def report_time_sequence(self):
        for time_seq, variants in self.time_sequence.items():
            if self.report_variant in variants:
                time_sequence = time_seq
                return time_sequence