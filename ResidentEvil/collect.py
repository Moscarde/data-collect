# %%
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    "Referer": "https://www.residentevildatabase.com/personagens/",
    "Connection": "keep-alive",
    # 'Cookie': '_ga_DJLCSW50SC=GS1.1.1721629819.1.1.1721629953.37.0.0; _ga=GA1.2.994490107.1721629819; _gid=GA1.2.1533775789.1721629820; __gads=ID=c0033dd6ce75c28f:T=1721629820:RT=1721629820:S=ALNI_MbuH-R27Zuxwh4lwJxDWIa-ws5QrA; __gpi=UID=00000a4690ee369e:T=1721629820:RT=1721629820:S=ALNI_MYdumfbEbBsrBuyjJzPLQA-lpS9vQ; __eoi=ID=1cc10befecbf7393:T=1721629820:RT=1721629820:S=AA-AfjZn58UibglFXKl-c96QGaxB; _ga_D6NF5QC4QT=GS1.1.1721629859.1.1.1721629953.37.0.0; FCNEC=%5B%5B%22AKsRol-KCMZ6UXD9KqBv-7We1ULZV4UeAuwsp7K9-nt2sgLss3x2XOvFL7v6KLYCjRUCJ0v61rlKP5efCO1iifH5kZ_QNWlvJERt6VPnpKHhbq3pkvOU9BNjxGe2lMaNRig-DeyGRiXhObQCZXzToDbXlBx4cCWDmg%3D%3D%22%5D%5D',
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i",
}


def get_content(url):

    return requests.get(url, headers=headers)


def get_basic_infos(soup):
    div_page = soup.find("div", class_="td-page-content")
    paragrafo = div_page.find_all("p")[1]

    ems = paragrafo.find_all("em")

    data = {}
    for i in ems:
        chave, valor, *_ = i.text.split(":")
        chave = chave.strip(" ")
        data[chave] = valor.strip(" ")

    return data


def get_aparicoes(soup):
    lis = (
        soup.find("div", class_="td-page-content").find("h4").find_next().find_all("li")
    )

    aparicoes = [i.text for i in lis]
    return aparicoes


def get_personagem_infos(url):
    response = get_content(url)

    if response.status_code != 200:
        print("Não foi possível obter os dados!")
        return {}
    else:
        soup = BeautifulSoup(response.text)
        data = get_basic_infos(soup)
        data["Aparicoes"] = get_aparicoes(soup)
        return data


def get_links():
    url_lista = "https://www.residentevildatabase.com/personagens/"

    response = requests.get(url_lista, headers=headers)

    soup_personagens = BeautifulSoup(response.text)

    ancoras = soup_personagens.find("div", class_="td-page-content").find_all("a")

    links = [i["href"] for i in ancoras]
    return links


# %%

# %%

links = get_links()
data =[]
for i in tqdm(links):
    d = get_personagem_infos(i)
    d["link"] = i
    data.append(d)

# %%
df = pd.DataFrame(data)
df.to_csv("dados_re.csv", index=False, sep=";")
df.to_parquet("dados_re.parquet", index=False)
df.to_pickle("dados_re.pkl")
