import random
import time
clientCount = 0
timeCount = 0
i = 60
clientes = []
op = {0: 10, 1: 20, 2: 30, 3: 40, 4: 50}

def caixa(clientes):
    global timeCount
    caixa1 = []
    caixa2 = []
    caixa3 = []
    if len(caixa1) == 0:
        if len(clientes) != 0:
            caixa1.append(clientes[0])         
            timeCount = timeCount + (clientes[0] - time.time())
            timeCount = timeCount + op.get(random.randint(0, 4))
            clientes.pop(0)
        else:
            pass
    if len(caixa2) == 0:
        if len(clientes) != 0:
            caixa2.append(clientes[0])         
            timeCount = timeCount + (clientes[0] - time.time())
            timeCount = timeCount + op.get(random.randint(0, 4))
            clientes.pop(0)
        else:
            pass
    if len(caixa3) == 0:
        if len(clientes) != 0:
            caixa3.append(clientes[0])         
            timeCount = timeCount + (clientes[0] - time.time())
            timeCount = timeCount + op.get(random.randint(0, 4))
            clientes.pop(0)
        else:
            pass
    return timeCount

def agencia(clientes):
    global clientCount
    if random.randint(0 , 1) == 1:
        clientes.append(time.time())
        clientCount = clientCount +1
    else:
        pass

while i != 0:
    agencia(clientes)
    caixa(clientes)
    i = i-1

print("Tempo total: ", timeCount)
print("Numero de clientes: ", clientCount)
print("Tempo medio: ", timeCount / clientCount)