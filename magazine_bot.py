import requests
from bs4 import BeautifulSoup

url = "https://br.ign.com/"

##Mascara do robo
headers = {
    "User-Agent": "Mozilla/5,0 (windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

print("[SukoBot] Tentando conectar na IGN Brasil...")

resposta = requests.get(url, headers=headers)
print(f"[SukoBot] Status da resposta: {resposta.status_code}")
if resposta.status_code == 200:
    print("[SukoBot] Conexão estabelecida! Conseguimos baixar o HTML da IGN.")
    print("\n Um trecho do HTML baixado:")

    sopa = BeautifulSoup(resposta.text, "html.parser")
    print("\n [SukoBot]Procurando titulos de noticias...")
    titulos = sopa.find_all("h2", class_="card-title")

    if titulos:
        print(f"[SukoBot] Encontrei {len(titulos)} titulos! Mostrando os 5 primeiros titulos:\n")
        for i, titulo in enumerate(titulos[:5], start=1):
            texto_limpo = titulo.text.strip()
            print(f"{i}. {texto_limpo}")

    else:
        print("Não encontrei nenhuma tag <h2> com a classe 'card-title'. O site pode ter mudado de estrutura.")

else:
    print("[SukoBot] Falha na conexão. Fomos descobertos ou o site esta fora do ar.")
 