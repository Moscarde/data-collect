# Estudo sobre APIs e Ingestão de Dados

Este repositório contém um estudo abrangente sobre a coleta e o processamento de dados de APIs públicas, utilizando técnicas avançadas de engenharia de dados. O objetivo principal é demonstrar como realizar a ingestão de dados em diferentes formatos e como processá-los eficientemente usando Python e Spark.

O estudo explora diversas etapas de uma rotina completa de engenharia de dados, desde a coleta inicial até uma introdução ao processamento e armazenamento em camadas na nuvem.


## Estrutura do Repositório

O repositório está organizado da seguinte forma:

- **`JovemNerd/`**: Scripts para coletar e processar dados do [Jovem Nerd API](https://api.jovemnerd.com.br/wp-json/jovemnerd/v1/nerdcasts/).
  - **`data/`**: Pasta contendo os dados coletados.
    - **`episodios/`**: Subpastas para dados em formato JSON e Parquet.
  - **`episodios.py`**: Script para coletar dados da API e salvá-los em formatos JSON e Parquet.

- **`Pokemon/`**: Scripts para coletar e processar dados da [Pokémon API](https://pokeapi.co/api/v2/pokemon/).
  - **`collect.py`**: Script para coletar dados da API e salvá-los em formato JSON.
  - **`pokemon_details.py`**: Script para processar dados coletados e obter detalhes dos Pokémon usando Spark.

- **`ResidentEvil/`**: Scripts e dados relacionados a [Resident Evil Database](https://www.residentevildatabase.com/personagens/), incluindo arquivos CSV, Parquet e Pickle.
  - **`collect.py`**: Script para coleta de dados.
  - **`dados_re.csv`**: Dados em formato CSV.
  - **`dados_re.parquet`**: Dados em formato Parquet.
  - **`dados_re.pkl`**: Dados em formato Pickle.

- **`TabNews/`**: Scripts para coletar e processar dados da [Tab News API](https://www.tabnews.com.br/api/v1/contents/).
  - **`basic_content.py`**: Script básico para coleta de dados.
  - **`data/`**: Pasta contendo dados coletados.
    - **`contents/`**: Subpastas para dados em formato JSON e Parquet.
  - **`read_spark.py`**: Script para ler e processar dados usando Spark.

## Requisitos

- Python 3.x
- Bibliotecas Python: `requests`, `pandas`, `pyspark`, `json`
- Spark (para processamento de dados)

## Como Usar

1. **Configurar Ambiente:**
   - Instale as dependências necessárias usando `pip install -r requirements.txt`.

2. **Executar Scripts:**
   - Execute os scripts `basic_content.py`, `collect.py`, `pokemon_details.py` e `read_spark.py` para coletar e processar os dados.
   - Todos estão estruturados em formatos de celulas, com o objetivo de auxiliar o desenvolvedor na escrita de código.