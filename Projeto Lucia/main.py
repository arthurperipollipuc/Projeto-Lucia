print("=== SEUC-4 - Refinaria Delta-9 ===")

total = int(input("Quantas leituras serão feitas? "))

# variáveis
soma = 0
menor = None
cont_verde = 0
leituras_feitas = 0
zona_anterior = ""

travou = False

for i in range(total):
    valor = float(input(f"Leitura {i+1}: "))

    # ajuste térmico
    if valor > 150:
        valor = valor * 1.08
    else:
        valor = valor * 0.96

    # classificação
    if valor >= 120 and valor <= 180:
        zona = "verde"
    elif valor < 250:
        zona = "amarela"
    else:
        zona = "vermelha"

    print("Valor ajustado:", round(valor, 2))
    print("Zona:", zona)

    # atualizar dados
    soma += valor
    leituras_feitas += 1

    if menor is None or valor < menor:
        menor = valor

    if zona == "verde":
        cont_verde += 1

    # verificar travamento
    if zona == "vermelha" and zona_anterior == "vermelha":
        print("TRAVAMENTO! Duas zonas vermelhas seguidas.")
        travou = True
        break

    zona_anterior = zona

# resultados
media = soma / leituras_feitas
porc_verde = (cont_verde / leituras_feitas) * 100

print("\n=== RESULTADO ===")
print("Média:", round(media, 2))
print("Menor valor:", round(menor, 2))
print("Porcentagem zona verde:", round(porc_verde, 2), "%")

if travou:
    porc_realizado = (leituras_feitas / total) * 100
    print("Sistema travou.")
    print("Leituras feitas:", round(porc_realizado, 2), "%")
else:
    print("Sistema finalizado normalmente.")