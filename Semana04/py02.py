
mensagem = 'Ola, mundo'

print(mensagem) #mostra a string
print(len(mensagem)) #mostra no número de caracteres da string
print(mensagem[0]) #mostra o primeiro caractere da string
print(mensagem[:5]) #mostra os caracteres do primeiro ao índice 5 não incluindo o índice 5
print(mensagem[6:]) #mostra os caracteres a partir do índice 6
print(mensagem.lower()) #mostra a string com todas as letras minúsculas
print(mensagem.count('l')) #mostra quantos caracteres l estão na string
print(mensagem.find('l')) #mostra onde está o primeiro caractere l da string

nova_mensagem = mensagem.replace('mundo', 'universo') #substitui na mensagem o primeiro argumento da função pelo segundo
print(nova_mensagem)

cumprimento = 'Ola'
nome = 'Matheus'
segunda_mensagem = '{}, {}. Bem-vindo!'.format(cumprimento, nome) #cria uma nova string concatenando strings anteriores e formatando-as
#segunda_mensagem = f'{cumprimento}, {nome}. Welcome!' #faz o mesmo que a linha acima
print(segunda_mensagem)

print(dir(nome)) #mostra todas as funções que podem ser usadas com essa variável
print(help(str.lower))