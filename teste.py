import requests
import responses
import json

# computador = ['Processador', 'Teclado', 'Mouse']
# for indice in range(len(computador)):
#     print(f"Índice = {indice} | valor = {computador[indice]}")

api_token  = "DWLCj1CwAA2Flnn2AK03UhPndbpiMcNjlKR03dPiiCPrfc1yOXO9w70unUT2"
# sportmonks = "https://api.sportmonks.com/v3/my/teams?api_token="+api_token
sportmonks = "https://api.sportmonks.com/v3/core/countries?api_token="+api_token+"&include=leagues;"


api_futebol = "https://api.api-futebol.com.br/v1/campeonatos/10"
api_futebol_key = {"Authorization" : "Bearer live_fbcea0cb6695e13a022fe66a3cbced"}
campeonato_id = 10

# url = api_futebol
# headers = {api_futebol_key}

# response = requests.get(sportmonks)
# data=response.json()
# # print(data)
# print(data)


payload={}
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

response = requests.request("GET", sportmonks, headers=headers, data=payload)
data = response.json()


print(f'\n',data)


# https://futebol.placar.esporte.uol.com.br/api/v2/debug.htm?file=commons.uol.com.br/monaco/placar/modalidades/futebol/149/2015/01/27/chelsea-x-liverpool.vm