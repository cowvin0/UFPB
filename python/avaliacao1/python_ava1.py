# 1)


def print_quest_1():
    nome = "João da Silva"
    idade = 38
    salario = 12500.37
    print(
        "Nome: [{:+<20}], Idade: [{:0=4d}], Salário: [{:*^14}]".format(
            nome, idade, salario
        )
    )


# 2)
# Ambientes virtuais em Python são formas de manter a versão do Python e bibliotecas do Python numa versão
#   diferente do Python instalado no sistema operacional. É uma boa forma de manter projetos funcionando e não
#   sofrer com problemas de versões diferentes de bibliotecas e do próprio Python.

# Como criar um ambiente virtual:

# Um ambiente virtual pode ser criado utilizando a biblioteca venv.

# O comando para a criação do ambiente virtual é: $ python{versao_do_python} - m venv {nome_do_ambiente_virtual}

# Agora que o ambiente virtual foi criado, você poderar ativar ele utilizando o bash com:
# source {nome_do_ambiente_virtual}/bin/activate

# Para desativar o virtual environment, basta digitar: deactivate

# Agora que já foi possível criar o ambiente virtural, pode criar as bibliotecas utilizando o pip install.

# Instalando o pandas com o pip, será possível colocar a versão do pandas num arquivo .txt com pip freeze.
# Assim, basta utilizado o comando: pip freeze > requirements.txt
# Pronto, agora você tem um arquivo .txt com a biblioteca pandas e algumas das dependências que foram instaladas juntas com ela.
# Agora, caso queira utilizar o requirements.txt para instalar bibliotecas em outros ambientes, basta utilizar o comando:
# pip install -r requirements.txt

# 3)


def funcao_pokemon(passe_pokemon):
    pokemons = {
        "pikachu": {
            "tipo": "elétrico",
            "ataques": ["Choque do Trovão", "Raio", "Investida"],
        },
        "charizard": {
            "tipo": "fogo/voador",
            "ataques": ["Lança-chamas", "Fogo Fátuo", "Ataque Aéreo"],
        },
        "blastoise": {
            "tipo": "água",
            "ataques": ["Jato d'Água", "Giro Rápido", "hidro bomba"],
        },
    }

    try:
        return pokemons[passe_pokemon]
    except:
        return ""


# 5)


def impar(func):
    def retorna_impar(lista_salario):
        pega_lista_ant = func(lista_salario)
        filtra_impar = list(filter(lambda x: x % 3 == 0, pega_lista_ant))
        return filtra_impar if len(filtra_impar) != 0 else pega_lista_ant

    return retorna_impar


def par(func):
    def retorna_par(lista_salario):
        pega_lista_ant = func(lista_salario)
        filtra_par = list(filter(lambda x: x % 2 == 0, pega_lista_ant))
        return filtra_par if len(filtra_par) != 0 else pega_lista_ant

    return retorna_par


def impar_par(func):
    def retorna_par(lista_salario):
        pega_lista_ant = func(lista_salario)
        filtra_par = list(filter(lambda x: x % 2 == 0, pega_lista_ant))
        impar = [odd for odd in pega_lista_ant if odd not in filtra_par]
        return filtra_par if len(filtra_par) != 0 else pega_lista_ant, impar

    return retorna_par


# Agora, considere que você tem uma função que calcule o aumento salarial de cada funcionário
# Se o salário for maior que 1250, o salário será aumentado em 10%, caso contrário, será aumentado em 15%.


@impar
def salario(lista_salario):
    return list(map(lambda x: x * 1.1 if x > 1250 else x * 1.15, lista_salario))


@par
def salario(lista_salario):
    return list(map(lambda x: x * 1.1 if x > 1250 else x * 1.15, lista_salario))


@impar_par
def salario(lista_salario):
    return list(map(lambda x: x * 1.1 if x > 1250 else x * 1.15, lista_salario))


print(salario(lista_salario=[1250, 1300, 1500, 1000]))

# A função salário é primeiramente passada para o decorador par para verificar os números pares para retornar. Caso não exista
# números pares, a lista retornada no decorador par é passada para o decorador impar, retornando aqueles valores que são impares.
