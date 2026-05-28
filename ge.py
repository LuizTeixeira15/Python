import requests
import json

# URL da API GraphQL do GE
url = "https://globo.com"

# Query para solicitar os dados da tabela do Brasileirão Série A
payload = {
    "query": """
    query Classificacao($campeonato: String!, $fase: String!) {
      classificacao(campeonato: $campeonato, fase: $fase) {
        nome
        posicao
        pontos
        jogos
        vitorias
        empates
        derrotas
        gols_pro
        gols_contra
        saldo_gols
      }
    }
    """,
    "variables": {
        "campeonato": "brasileirao-serie-a",
        "fase": "fase-unica"
    }
}

headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 200:
    dados = response.json()
    times = dados['data']['classificacao']
    
    print(f"{'Pos':<4}{'Time':<20}{'Pts':<5}{'J':<4}{'V':<4}{'SG':<4}")
    print("-" * 45)
    for time in times:
        print(f"{time['posicao']:<4}{time['nome']:<20}{time['pontos']:<5}{time['jogos']:<4}{time['vitorias']:<4}{time['saldo_gols']:<4}")
else:
    print(f"Erro ao acessar a API: {response.status_code}")



