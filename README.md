# data-collect

## Objetivo

Este projeto realiza a coleta de informações sobre personagens do jogo Resident Evil a partir do site [Resident Evil Database](https://www.residentevildatabase.com/personagens/). O objetivo é extrair dados como informações básicas e aparições dos personagens, e salvar esses dados em diferentes formatos.
## Conteúdo do Projeto

O projeto inclui um script Python que utiliza bibliotecas de scraping para buscar e processar informações de personagens. Os dados são extraídos e salvos em três formatos: CSV, Parquet e Pickle.

### Dependências

- `requests` - Para fazer requisições HTTP.
- `beautifulsoup4` - Para fazer parsing do HTML.
- `tqdm` - Para exibir uma barra de progresso.
- `pandas` - Para manipulação e armazenamento dos dados.

### Funcionamento

1. **Requisição de Dados**: O script realiza uma requisição HTTP para a página principal de personagens e coleta os links para as páginas individuais de cada personagem.
2. **Extração de Dados**: Para cada página de personagem, o script extrai:
    - Informações básicas (nome, idade, etc.).
    - Aparições do personagem em diferentes mídias.
3. **Armazenamento**: Os dados extraídos são armazenados em três formatos:
    - CSV (`dados_re.csv`)
    - Parquet (`dados_re.parquet`)
    - Pickle (`dados_re.pkl`)

### Como Executar

1. Instale as dependências necessárias:
```bash
pip install requests beautifulsoup4 tqdm pandas
``` 

2. Execute o script:
```
python collect.py
```

O script salvará os dados extraídos nos arquivos mencionados.

### Arquivos Gerados

- `dados_re.csv` - Arquivo CSV contendo os dados dos personagens.
- `dados_re.parquet` - Arquivo Parquet com os mesmos dados.
- `dados_re.pkl` - Arquivo Pickle com os dados.