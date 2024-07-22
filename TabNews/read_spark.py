# %%
from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType


# Cria uma sessão Spark
spark = SparkSession.builder \
    .appName("Read JSON Files") \
    .getOrCreate()


# %%
# Caminho para o diretório contendo os arquivos JSON
json_directory = "data/contents/json"



# Lê os arquivos como texto
text_df = spark.read.text(json_directory)

# Define o esquema do JSON
schema = StructType([
    StructField("id", StringType(), True),
    StructField("owner_id", StringType(), True),
    StructField("parent_id", StringType(), True),
    StructField("slug", StringType(), True),
    StructField("title", StringType(), True),
    StructField("status", StringType(), True),
    StructField("type", StringType(), True),
    StructField("source_url", StringType(), True),
    StructField("created_at", TimestampType(), True),
    StructField("updated_at", TimestampType(), True),
    StructField("published_at", TimestampType(), True),
    StructField("deleted_at", StringType(), True),
    StructField("owner_username", StringType(), True),
    StructField("tabcoins", IntegerType(), True),
    StructField("tabcoins_credit", IntegerType(), True),
    StructField("tabcoins_debit", IntegerType(), True),
    StructField("children_deep_count", IntegerType(), True)
])

# Converte texto em JSON com o esquema definido
df = text_df.select(from_json(col("value"), schema).alias("json_data")).select("json_data.*")

# Mostra o esquema dos dados
df.printSchema()

# Mostra as primeiras linhas dos dados
df.show(truncate=False)


