import random

cronometro = 600

caixa1 = 0
caixa2 = 0
caixa3 = 0

operacoes = {'saldo': 10,
	     'saque': 20,
	     'aplicacao': 30,
	     'extrato semanal': 40,
	     'extrato mensal': 50}

fila_de_clientes = []

def entrada_de_cliente(fila, segundo):
    if random.randint(0, 1) == 1:
        fila.append(segundo)

def escolher_operacao():
    global operacoes
    op = random.randint(1, 5)
    if op == 1:
        return operacoes['saldo']
    elif op == 2:
        return operacoes['saque']
    elif op == 3:
        return operacoes['aplicacao']
    elif op == 4:
        return operacoes['extrato semanal']
    elif op == 5:
        return operacoes['extrato mensal']

clientes = {'caixa1': None,
            'caixa2': None,
            'caixa3': None}

for s in range(1, cronometro + 1):
    entrada_de_cliente(fila_de_clientes, s)

    if caixa1 == 0:
        caixa1 = escolher_operacao()
        try:
            clientes['caixa1'] = fila_de_clientes.pop(0)
            print("Entrou um cliente no {}".format('caixa1'))
        except IndexError:
            clientes['caixa2'] = None
            caixa1 = 0
            pass
    if caixa2 == 0:
        caixa2 = escolher_operacao()
        try:
            clientes['caixa2'] = fila_de_clientes.pop(0)
            print("Entrou um cliente no {}".format('caixa2'))
        except IndexError:
            clientes['caixa2'] = None
            caixa2 = 0
            pass
    if caixa3 == 0:
        caixa3 = escolher_operacao()
        try:
            clientes['caixa3'] = fila_de_clientes.pop(0)
            print("Entrou um cliente no {}".format('caixa3'))
        except IndexError:
            clientes['caixa3'] = None
            caixa3 = 0
            pass

    if caixa1 != 0:
        caixa1 -= 1
        if caixa1 == 0:
            try:
                print("\nO cliente que usou o {} aguardou {} segundos\n".format('caixa 1', s - clientes['caixa1']))
            except TypeError:
                pass

    if caixa2 != 0:
        caixa2 -= 1
        if caixa2 == 0:
            try:
                print("\nO cliente que usou o {} aguardou {} segundos\n".format('caixa 2', s - clientes['caixa2']))
            except TypeError:
                pass

    if caixa3 != 0:
        caixa3 -= 1
        if caixa3 == 0:
            try:
                print("\nO cliente que usou o {} aguardou {} segundos\n".format('caixa 3', s - clientes['caixa3']))
            except TypeError:
                pass

print(fila_de_clientes)
