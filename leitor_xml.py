import xmltodict
import os
import xml.etree.ElementTree as ET


pasta = './xml_onu'
resultados = []

for arquivo in os.listdir(pasta):
    if arquivo.endswith('.xml'):
        caminho_arquivo = os.path.join(pasta, arquivo)


        tree = ET.parse(caminho_arquivo)
        root = tree.getroot()
        






# with open('teste.xml', 'rb') as fd:
#     dict_data = xmltodict.parse(fd)

# dados = dict_data['nfeProc']['NFe']['infNFe']




# for i, p in enumerate(dados):
#     print(f'{dados["Id"]} - {dados["det"][i]["infAdProd"]}')
