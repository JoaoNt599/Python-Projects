import requests

headers = {'Authorization': 'Token d43619ff4c542b1ed3c086e8ed99b228641ed947'}
url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo3 curso",
    "url": "http://novocurso3.com"
}

#curso = requests.get(url=f'{url_base_cursos}3/', headers=headers)
#print(curso.json())

resultado = requests.put(url=f'{url_base_cursos}3/', headers=headers, data=curso_atualizado) #Curso id 3
assert resultado.status_code == 200
assert resultado.json()['titulo'] == curso_atualizado['titulo']
print(resultado.json())