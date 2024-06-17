import requests
import responses
import json

api_token  = "DWLCj1CwAA2Flnn2AK03UhPndbpiMcNjlKR03dPiiCPrfc1yOXO9w70unUT2"
sportmonks = "https://api.sportmonks.com/v3/football/leagues?api_token="+api_token+"&include=today;"

payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
}

response = requests.request("GET", sportmonks, headers=headers, data=payload)
print(response)
t = response.json()
t = json.dumps(t)
res = json.loads(t)
print(res)
# for i, c in enumerate(res['data']):
#     print(res)
#     if c['time']['nome_popular'].upper() == 'FLAMENGO':
#       print(c['time']['nome_popular'])
#       print(f"Posição: {c['posicao']}")
#       print(f"Pontos: {c['pontos']}")
#       print(f"Jogos: {c['jogos']}")
#       print(f"Vitorias: {c['vitorias']}")
#       print(f"empates: {c['empates']}")
#       print(f"derrotas: {c['derrotas']}")
#       print(f"gols_pro: {c['gols_pro']}")
#       print(f"gols_contra: {c['gols_contra']}")
#       print(f"saldo_gols: {c['saldo_gols']}")
#       print(f"aproveitamento: {c['aproveitamento']}")
#       print(f"variacao_posicao: {c['variacao_posicao']}")
#       print(f"ultimos_jogos: {c['ultimos_jogos']}")
      
    


# https://futebol.placar.esporte.uol.com.br/api/v2/debug.htm?file=commons.uol.com.br/monaco/placar/modalidades/futebol/149/2015/01/27/chelsea-x-liverpool.vm