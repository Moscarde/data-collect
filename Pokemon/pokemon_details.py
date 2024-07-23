# %%
import requests
import json
from pyspark.sql import SparkSession
import pandas as pd
import datetime
from multiprocessing import Pool

# %%
spark = SparkSession.builder \
    .appName("Pokemon") \
    .getOrCreate()

# %%

# Subindo o banco
json_directory = "/mnt/datalake/pokemon/pokemon"

(spark.read.json(json_directory).createOrReplaceTempView("pokemon"))

query = """
WITH all_pokes AS (
    SELECT ingestion_date,
    poke.*
    FROM pokemon
    LATERAL VIEW explode(results) AS poke
),

tb_row_number AS (
    SELECT *,
        row_number() OVER (PARTITION BY name ORDER BY ingestion_date DESC) AS rn_pokemon

    FROM all_pokes
    ORDER BY url, ingestion_date
)

SELECT *
FROM tb_row_number
WHERE rn_pokemon = 1

"""
df = spark.sql(query).coalesce(1)
urls = df.toPandas()["url"].tolist()

# %%
def save_pokemon_details(data):
    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S.%f")

    filename = f"/mnt/datalake/pokemon/pokemon_details/{data["id"]} {now}.json"
    data["ingestion_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w") as open_file:
        json.dump(data, open_file)

def get_and_save(url):
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        save_pokemon_details(data)
    else:
        print("Error:", resp.status_code, "url:", url)
        



# %%

with Pool(5) as p:
    p.map(get_and_save, urls)

# %%
# lendo os arquivos
json_directory = "/mnt/datalake/pokemon/pokemon_details"

(spark.read.json(json_directory).createOrReplaceTempView("pokemon_details"))

# %%
query = """
SELECT *
FROM pokemon_details
"""
df = spark.sql(query)
pandas_result = df.toPandas()
display(pandas_result)