# ==================================================
#   SEUC-4 - Refinaria Delta-9
#   Sistema de Escoamento de Unidades de Carga
# ==================================================

def ajuste_termico(pressao):
   if pressao > 150:
       return pressao * 1.08
   else:
       return pressao * 0.96

def classificar_zona(pressao_ajustada):
   if pressao_ajustada > 250:
       return "VERMELHA"
   elif 120 <= pressao_ajustada <= 180:
       return "VERDE"
   else:
       return "AMARELA"

def main():
   print("=" * 50)
   print("  SEUC-4 - Refinaria Delta-9")
   print("  Sistema de Escoamento de Unidades de Carga")
   print("=" * 50)

   total = int(input("\nInforme o número total de leituras do turno: "))

   if total <= 0:
       print("Número de leituras inválido. Encerrando.")
       return

   soma_ajustadas = 0.0
   menor_pressao = float('inf')
   contagem_verde = 0
   zona_anterior_vermelha = False
   travamento = False
   leituras_realizadas = 0

   for i in range(1, total + 1):
       print(f"\n--- Leitura {i} de {total} ---")
       pressao = float(input("  Digite a pressão (UPC): "))

       ajustada = ajuste_termico(pressao)
       zona = classificar_zona(ajustada)

       print(f"  Pressão original : {pressao:.2f} UPC")
       print(f"  Pressão ajustada : {ajustada:.2f} UPC")
       print(f"  Zona             : {zona}")

       soma_ajustadas += ajustada
       leituras_realizadas += 1

       if ajustada < menor_pressao:
           menor_pressao = ajustada

       if zona == "VERDE":
           contagem_verde += 1

       if zona == "VERMELHA" and zona_anterior_vermelha:
           print("\n !!! ALERTA: Dois picos consecutivos na Zona Vermelha !!!")
           print("  !!! ESCOAMENTO INTERROMPIDO IMEDIATAMENTE !!!")
           travamento = True
           break

       if zona == 'VERMELHA':
           zona_anterior_vermelha = True
       else:
           zona_anterior_vermelha = False

   # Relatório Final
   media = soma_ajustadas / leituras_realizadas
   percentual_verde = (contagem_verde / leituras_realizadas) * 100

   print("\n" + "=" * 50)
   print(" RELATÓRIO FINAL - SEUC-4")
   print("=" * 50)
   print(f"  Leituras realizadas      : {leituras_realizadas} de {total}")
   print(f"  Média das pressões       : {media:.2f} UPC")
   print(f"  Menor pressão ajustada   : {menor_pressao:.2f} UPC")
   print(f"  Leituras na Zona Verde   : {percentual_verde:.1f}%")

   if travamento:
       percentual_realizado = (leituras_realizadas / total) * 100
       print(f"\n* SISTEMA TRAVADO *")
       print(f"  Percentual do turno executado : {percentual_realizado:.1f}%")
       print(f"  Causa: dois picos consecutivos na Zona Vermelha.")
   else:
       print("\n  Turno concluído sem travamentos.")

   print("=" * 50)

main()