import requests
from json import loads

def buscar_cep(cep):
    request = requests.get(f"https://viacep.com.br/ws/{str(cep)}/json/")
    data = loads(request.content)
    print(f"""
        RUA:\t{data["logradouro"]}
        BAIRRO:\t{data["bairro"]}
        CIDADE:\t{data['localidade']}\t{data['uf']}
    """)


buscar_cep('06680103')

