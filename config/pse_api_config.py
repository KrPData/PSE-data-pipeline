import math
import pandas as pd
from urllib.parse import urlencode

class PseApiConfig:

    def __init__(self, report_variant: int): 
        self.report_variant = report_variant

    def variant_url(self, date_start: str, date_end: str, records_num: float):
        link_core = "https://api.raporty.pse.pl/api/"

        url_parts = {
            1 : ["his-wlk-cal?", "business_date,period,demand,swm_p,swm_np,jg,jgw1,jgw2,jgm1,jgm2,jgz1,jgz2,jgz3,jga,pv,wi,jnwrb"],
            2 : ["cmbp-tp?", "business_date,onmb,fcr_g,fcr_d,afrr_g,afrr_d,mfrrd_g,mfrrd_d,rr_d,rr_g"],
            3 : ["mbp-tp?", "business_date,onmbp,fcr_g,fcr_d,afrr_g,afrr_d,mfrrd_g,mfrrd_d,rr_d,rr_g"], 
            4 : ["mbu-tu?", "business_date,period,fcr_g,fcr_d,afrr_g,afrr_d,mfrrd_g,mfrrd_d"],
            5 : ["cmbu-tu?", "business_date,period,fcr_g,fcr_d,afrr_g,afrr_d,mfrrd_g,mfrrd_d"],
            6 : ["gen-jw?", ""], 
            7 : [],
            8 : ["poze-redoze?", "business_date,period,pv_red_balance,wi_red_balance,pv_red_network,wi_red_network"],
            9 : ["popmb-rmb?", "business_date,onmbp,reserve_type,pom,com"]
        }

        params = {
            "$select" : url_parts[self.report_variant][1],
            "$filter" : f"business_date ge '{date_start}' and business_date le '{date_end}'",
            "$orderby" : "business_date asc",
            "$first" :  f"{math.floor(records_num)}"
        }

        return link_core + url_parts[self.report_variant][0] + urlencode(params)

