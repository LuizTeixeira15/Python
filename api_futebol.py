import requests
import responses
import json

campeonato_id = 10
api_futebol = "https://api.api-futebol.com.br/v1/campeonatos/"+campeonato_id+"/tabela"
api_futebol_key = "Bearer live_fbcea0cb6695e13a022fe66a3cbced"


payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization':api_futebol_key
}

response = requests.request("GET", api_futebol, headers=headers, data=payload)
print(response)
t = response.json()
t = json.dumps(t)
res = json.loads(t)
for i, c in enumerate(res):
    if c['time']['nome_popular'].upper() == 'FLAMENGO':
      print(c['time']['nome_popular'])
      print(f"Posição: {c['posicao']}")
      print(f"Pontos: {c['pontos']}")
      print(f"Jogos: {c['jogos']}")
      print(f"Vitorias: {c['vitorias']}")
      print(f"empates: {c['empates']}")
      print(f"derrotas: {c['derrotas']}")
      print(f"gols_pro: {c['gols_pro']}")
      print(f"gols_contra: {c['gols_contra']}")
      print(f"saldo_gols: {c['saldo_gols']}")
      print(f"aproveitamento: {c['aproveitamento']}")
      print(f"variacao_posicao: {c['variacao_posicao']}")
      print(f"ultimos_jogos: {c['ultimos_jogos']}")
      
# https://futebol.placar.esporte.uol.com.br/api/v2/debug.htm?file=commons.uol.com.br/monaco/placar/modalidades/futebol/149/2015/01/27/chelsea-x-liverpool.vm