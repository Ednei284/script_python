# lista = [1,2,3,4,5,6,7,8,9]
# # acessa a lista apartir da posição 0 e extrai dois valores
# print(lista[3:5])
email = input('digite seu email:')
arroba = email.find('@')
user = email[0:arroba]
dominio = email[arroba+1:]
print(user)
print(dominio)