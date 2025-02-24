a = input('Digite algo:')
print('O tipo primitivo desse valor é ', type(a))
# type(var) mostra se e inteiro, string ou outro tipo de variavel
print('So tem espaços?', a.isspace())
# a=var isspace=verifica se há espaços no texto digitado
print('É um número?', a.isnumeric())
# isnumeric= verifica se e um numero
print('É alfabetico?', a.isalpha())
# alpha= verifica se alfabetico/texto. Se tiver numero nao será afalbetico 
print('É alfanúmerico?',a.isalnum())
# isalnum verifica se o texto contem números ou somente texto
print('Ésta em maiúsculas?',a.isupper())
# isupper verifica se esta em letra maiusculas
print('Está em minúsculas?',a.islower())
#islower verifica se esta em minusculas
print('Está capitalizada?',a.istitle())
# istitle verifica se a palavra digita esta em outra "lingua"


