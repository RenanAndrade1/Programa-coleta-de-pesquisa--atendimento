excelente = 0
ruim = 0
#Entrada
for i in range(50):
    nome = input("Digite seu nome:")
    idade = int (input("Digite sua idade:"))
    opiniao = int (input("O que achou do atendimento?(1-excelente / 2-bom / 3-ruim)"))
#Processamento
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
#saída
print("EXCELENTE:", excelente)
print("RUIM:", ruim)