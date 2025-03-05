import requests

headers = {'Authorization': 'Token d43619ff4c542b1ed3c086e8ed99b228641ed947'} 
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)
print(resultado.json())

# Teste endpoint correto:
assert resultado.status_code == 200 #Se URI estiver incorreta, mostrará erro

# Teste qtde de registros:
assert resultado.json()['count'] == 2

# Teste de título do primeiro registro
assert resultado.json()['results'][0]['titulo'] == 'Título teste'