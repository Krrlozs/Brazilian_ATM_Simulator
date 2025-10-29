import sys
from time import sleep
from random import randint
notas = [1,5,10,20,50,100]

#SISTEMA QUE SIMULA A FALTA DE NOTAS ALEATORIAMENTE
notas_a_retirar = randint(1,len(notas))
#print(notas_a_retirar)
for n in range(0,notas_a_retirar):
    notas.pop(randint(0,len(notas)-1))
print(f'Notas dispníveis para saque: \033[34m{notas}\033[m')

#ERRO CRÍTICO, NENHUMA NOTA DISPONÍVEL PARA SAQUE!
if notas == []:
    print('\033[31mERRO!\033[0m\nCondição de falha crítica atingida!\nNão é possivel realizar o saque pois não há nenhuma cédula disponível'
          'Encerrando...')
    sys.exit()

# LÊ O VALOR DO SAQUE DO USUÁRIO
sleep(1)
saque = int(input('Quanto deseja sacar? R$'))
print('Analisando...')
sleep(2)

# VERIFICAÇAO DA MENOR NOTA ( SE A MENOR NOTA (notas[0]) FOR MAIOR QUE O VALOR DO SAQUE, JÁ IMPOSSIBILITA DE VEZ.
if notas[0] > saque:
    print('\033[31mERRO!\033[0m'
          'Não há notas disponíveis para realizar o saque.'
          'Encerrando...')
    sleep(2)
    sys.exit()

# ANALISA SE O SAQUE TERMINA EM 5 OU EM 1 (ULTIMO DIGITO) JÁ QUE NAO E POSSIVEL EX: SACAR 66 REAIS SEM NOTAS DE 5 OU DE 1
if saque % 10 == 5:
    if 5 in notas or 1 in notas:
        print('Notas para saque disponíveis, vamos continuar.')
    else:
        print('\033[31mERRO!\033[0m'
              'Não há notas disponíveis para realizar esse saque.'
              'Encerrando...')
        sleep(2)
        sys.exit()
elif saque % 10 != 0 and saque != 5:
    if 1 in notas:
        print('Notas para saque disponíveis, o processo será iniciado...')
    else:
        print('\033[31mERRO!\033[0m'
              'Não há notas dinsponíveis para realizar esse saque.'
              'Encerrando...')
        sleep(2)
        sys.exit()

# RESTO

total_saque = saque
contador = -1
cedula_atual = notas[contador]
total_cedulas = 0
while True:
    if total_saque >= cedula_atual:
        total_saque -= cedula_atual
        total_cedulas += 1
        #print(total_saque)

        if total_saque == 0:
            if total_cedulas > 0:
                print(f'{total_cedulas} nota(s) de R${cedula_atual}')
            break
    else:
        if total_cedulas > 0:
            print(f'{total_cedulas} nota(s) de {cedula_atual}')
        total_cedulas = 0
        contador += -1
    if abs(contador) > len(notas):
        if total_saque > 0:
            print('\033[31mERRO!\033[0m'
                  'Não há notas dinsponíveis para realizar esse saque.')
        break
    cedula_atual = notas[contador]

print('Encerrando...')
sleep(2)

