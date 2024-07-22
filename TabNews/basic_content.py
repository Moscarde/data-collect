# %%
import requests
import pandas as pd
import datetime
import json
import time
# %%

def get_response(**kwargs):
    url = "https://www.tabnews.com.br/api/v1/contents/"

    response = requests.get(url, params=kwargs)

    return response

def save_data(data, option="json"):

    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
    if option == "json":
        with open(f"/mnt/datalake/TabNews/contents/json/{now}.json", "w") as f:
            json.dump(data, f, indent=4)

    elif option == "parquet":
        df = pd.DataFrame(data)
        df.to_parquet(f"/mnt/datalake/TabNews/contents/parquet/{now}.parquet", index=False)
# %%

page = 1
while True:
    response = get_response(page=page, per_page=100, strategy="new")
    print(response.status_code)
    if response.status_code == 200:
        print("Sucess, page", page)
        data = response.json()
        save_data(data, option="json")

        if len(data) < 100:
            break
        else:
            time.sleep(1)
            page += 1

    elif response.status_code == 429:
        print("Timeout")
        break

# %%
