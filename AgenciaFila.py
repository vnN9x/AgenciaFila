import random
import time
clientCount = 0
timeCount = 0
i = 60
clientes = []
# op = operações no caixa eletronico, e seus respectivos tempos de duração
op = {0: 10, 1: 20, 2: 30, 3: 40, 4: 50}

"""
def client(tempo_de_entrada, tempo_de_uso_do_caixa, operacao, cliente_atual, caixa):
    print("Tempo de entrada do cliente {}         : {:.3f}s".format(cliente_atual, tempo_de_entrada))
    print("Tempo de uso do caixa pelo cliente {}  : {:.3f}s".format(cliente_atual, tempo_de_uso_do_caixa))
    if operacao == 10:
        op = "Saldo"
    elif operacao == 20:
        op = "Saque"
    elif operacao == 30:
        op = "Aplicação"
    elif operacao == 40:
        op = "Extrato Semanal"
    elif operacao == 50:
        op = "Extrato Mensal"
    print("Operação escolhida pelo cliente {}     : {}".format(cliente_atual, op))
    print("Caixa utilizado pelo cliente {}        : {}".format(cliente_atual, caixa))
    print()
"""

def caixa(clientes):
    global timeCount
    global clientCount
    caixa1 = []
    caixa2 = []
    caixa3 = []
    if len(caixa1) == 0:
        if len(clientes) != 0:
            caixa1.append(clientes[0])         
            crnt_op = op.get(random.randint(0, 4))

            timeCount = timeCount + (clientes[0] - time.time())
            timeCount = timeCount + crnt_op

            #client(clientes[0], timeCount, crnt_op, clientCount, 1)
            clientes.pop(0)
        else:
            pass
    if len(caixa2) == 0:
        if len(clientes) != 0:
            caixa2.append(clientes[0])         
            crnt_op = op.get(random.randint(0, 4))

            timeCount = timeCount + (clientes[0] - time.time())
            timeCount = timeCount + crnt_op

            #client(clientes[0], timeCount, crnt_op, clientCount, 2)
            clientes.pop(0)
        else:
            pass
    if len(caixa3) == 0:
        if len(clientes) != 0:
            caixa3.append(clientes[0])         
            crnt_op = op.get(random.randint(0, 4))

            timeCount = timeCount + (clientes[0] - time.time())
            timeCount = timeCount + crnt_op

            #client(clientes[0], timeCount, crnt_op, clientCount, 3)
            clientes.pop(0)
        else:
            pass
    return timeCount

def agencia(clientes):
    global clientCount
    if random.randint(0 , 1) == 1:
        t = time.time()
        clientes.append(t)
        clientCount = clientCount +1
    else:
        pass

while i != 0:
    agencia(clientes)
    caixa(clientes)
    i = i-5

print("Tempo total        : {:.3f}s ".format(timeCount))
print("Numero de clientes : {}".format(clientCount))
print("Tempo medio        : {:.3f}s".format(timeCount / clientCount))
