# %%

import datetime
import json
import time
import pandas as pd
import requests

# %%


class Collector:
    def __init__(self, url, instance_name):
        self.url = url
        self.instance_name = instance_name

    def get_content(self, **kwargs):
        response = requests.get(self.url, params=kwargs)
        return response

    def save_json(self, data):
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
        with open(f"/mnt/datalake/JovemNerd/{self.instance_name}/json/{now}.json", "w") as f:
            json.dump(data, f, indent=4)

    def save_parquet(self, data):
        now = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
        df = pd.DataFrame(data)
        df.to_parquet(f"/mnt/datalake/JovemNerd/{self.instance_name}/parquet/{now}.parquet", index=False)

    def save_data(self, data, option="json"):
        if option == "json":
            self.save_json(data)

        elif option == "parquet":
            self.save_parquet(data)

    def get_and_save(self, save_format="json", **kwargs):
        response = self.get_content(**kwargs)
        if response.status_code == 200:
            data = response.json()
            self.save_data(data, option=save_format)
        else:
            data = None
            print("Error:", response.status_code)

        return data

    def auto_exec(self, save_format="parquet", date_stop="2000-01-01"):
        page = 1
        while True:
            print("Page", page)
            data = self.get_and_save(save_format=save_format, page=page, per_page=1000)

            if data == None:
                print("Erro ao coletar dados, aguardando.")
                time.sleep(60* 15)
            else:
                last_date = pd.to_datetime(data[-1]["published_at"]).date()
                if last_date < pd.to_datetime(date_stop).date():
                    break
                elif len(data) < 1000:
                    break

                page += 1
                time.sleep(5)


# %%
url = "https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/"
collect = Collector(url, "episodios")
collect.auto_exec()
