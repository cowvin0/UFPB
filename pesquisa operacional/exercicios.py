# exercicio 1 problema do transporte

import pulp

# Definindo o problema
problem = pulp.LpProblem("Problema_de_Transporte", pulp.LpMinimize)

# Definindo as variáveis de decisão
x11 = pulp.LpVariable('x11', lowBound=0)
x12 = pulp.LpVariable('x12', lowBound=0)
x13 = pulp.LpVariable('x13', lowBound=0)
x14 = pulp.LpVariable('x14', lowBound=0)
x15 = pulp.LpVariable('x15', lowBound=0)
x16 = pulp.LpVariable('x16', lowBound=0)

x21 = pulp.LpVariable('x21', lowBound=0)
x22 = pulp.LpVariable('x22', lowBound=0)
x23 = pulp.LpVariable('x23', lowBound=0)
x24 = pulp.LpVariable('x24', lowBound=0)
x25 = pulp.LpVariable('x25', lowBound=0)
x26 = pulp.LpVariable('x26', lowBound=0)

# Função Objetivo
problem += (
    7 * x11 + 9 * x12 + 1 * x13 + 12 * x14 + 7 * x15 + 400 * x16 +
    4 * x21 + 5 * x22 + 12 * x23 + 1 * x24 + 3 * x25 + 800 * x26
), "Custo_total"

# Restrições de demanda
problem += x11 + x21 == 1400
problem += x12 + x22 == 1560
problem += x13 + x23 == 300
problem += x14 + x24 == 150
problem += x15 + x25 == 570
problem += x16 + x26 == 520

# Restrições de capacidade das filiais
problem += x11 + x12 + x13 + x14 + x15 + x16 <= 2500
problem += x21 + x22 + x23 + x24 + x25 + x26 <= 2000

# Resolvendo o problema
problem.solve()

# Resultados
result = {
    "Status": pulp.LpStatus[problem.status],
    "Custo_Total": pulp.value(problem.objective),
    "Ipanema_Centro": x11.varValue,
    "Ipanema_Barra": x21.varValue,
    "Copacabana_Centro": x12.varValue,
    "Copacabana_Barra": x22.varValue,
    "Centro_Centro": x13.varValue,
    "Centro_Barra": x23.varValue,
    "Barra_Centro": x14.varValue,
    "Barra_Barra": x24.varValue,
    "Leblon_Centro": x15.varValue,
    "Leblon_Barra": x25.varValue,
    "Tijuca_Centro": x16.varValue,
    "Tijuca_Barra": x26.varValue
}

# exercicio 2 problema do transporte

# Definindo o problema
problem = pulp.LpProblem("Problema_de_Transporte", pulp.LpMinimize)

# Definindo as variáveis de decisão
x11 = pulp.LpVariable('x11', lowBound=0)
x12 = pulp.LpVariable('x12', lowBound=0)
x13 = pulp.LpVariable('x13', lowBound=0)

x21 = pulp.LpVariable('x21', lowBound=0)
x22 = pulp.LpVariable('x22', lowBound=0)
x23 = pulp.LpVariable('x23', lowBound=0)

x31 = pulp.LpVariable('x31', lowBound=0)
x32 = pulp.LpVariable('x32', lowBound=0)
x33 = pulp.LpVariable('x33', lowBound=0)


# Função Objetivo
problem += (
    25 * x11 + 20 * x12 + 30 * x13 + 30 * x21 + 25 * x22 + 25 * x23 +
    20 * x31 + 15 * x32 + 23 * x33
), "Custo_total"

problem += x11 + x21 + x31 == 2000
problem += x12 + x22 + x32 == 2000
problem += x13 + x23 + x33 == 1000
problem += x11 + x12 + x13 <= 2000
problem += x21 + x22 + x23 <= 1500
problem += x31 + x32 + x33 <= 1500

result = {
    "Status": pulp.LpStatus[problem.status],
    "Custo_Total": pulp.value(problem.objective),
    "x11": x11.varValue,
    "x21": x21.varValue,
    "x12": x12.varValue,
    "x22": x22.varValue,
    "x13": x13.varValue,
    "x23": x23.varValue,
    "x33": x23.varValue,
    "x23": x23.varValue,
}
