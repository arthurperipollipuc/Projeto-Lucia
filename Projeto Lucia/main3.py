import os

COR_VERDE = '\033[92m'
COR_AMARELA = '\033[93m'
COR_VERMELHA = '\033[91m'
COR_RESET = '\033[0m'
NEGRITO = '\033[1m'

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

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
   


def gerar_relatorio(total, leituras_realizadas, soma_ajustadas, menor_pressao, contagem_verde, travamento):
   limpar_tela()

   
   if leituras_realizadas > 0:
       media = soma_ajustadas / leituras_realizadas
       percentual_verde = (contagem_verde / leituras_realizadas) * 100
   else:
       media = 0
       percentual_verde = 0

   print(f"\n{NEGRITO}" + "=" * 50)
   print(" RELATÓRIO FINAL - SEUC-4")
   print("=" * 50 + f"{COR_RESET}")
   print(f"  Leituras realizadas      : {leituras_realizadas} de {total}")
   print(f"  Média das pressões       : {media:.2f} UPC")
   print(f"  Menor pressão ajustada   : {menor_pressao:.2f} UPC")
   print(f"  Leituras na Zona Verde   : {percentual_verde:.1f}%")

   if travamento:
       percentual_realizado = (leituras_realizadas / total) * 100
       print(f"\n{NEGRITO}{COR_VERMELHA}>>> STATUS: SISTEMA TRAVADO <<<")
       print(f"  Percentual do turno executado : {percentual_realizado:.1f}%")
       print(f"  Causa: dois picos consecutivos na Zona Vermelha.{COR_RESET}")
   else:
       print(f"\n{NEGRITO}{COR_VERDE}>>> STATUS: TURNO CONCLUÍDO COM SUCESSO <<<{COR_RESET}")

   print("=" * 50)


def main():
   limpar_tela()
   print(f"{NEGRITO}{COR_AMARELA}" + "=" * 50)
   print("  SEUC-4 - Refinaria Delta-9")
   print("  Sistema de Escoamento de Unidades de Carga")
   print("=" * 50 + f"{COR_RESET}")

   total = 0
   turno_valido = False
   
   while not turno_valido:
       total = (input("\nInforme o número total de leituras do turno: "))
       if total.isdigit():
           if int(total) <= 0:
               print(f"{COR_VERMELHA}Número de leituras deve ser maior que zero. Tente novamente.{COR_RESET}")
           else:
               turno_valido = True
               total = int(total)
       else:
           print(f"{COR_VERMELHA}Entrada inválida. Por favor, insira um número inteiro.{COR_RESET}")


   soma_ajustadas = 0.0
   menor_pressao = None
   contagem_verde = 0
   zona_anterior_vermelha = False
   travamento = False
   leituras_realizadas = 0
   
   

   for i in range(1, total + 1):
       limpar_tela()
       
       print(f"{NEGRITO}\n--- Leitura {i} de {total} ---{COR_RESET}")
       
       pressao = 0
       turno_valido = False
   
       while not turno_valido:
            pressao = input(f"  Digite a pressão {NEGRITO}(UPC){COR_RESET}: ")
            if not pressao.replace('.', '', 1).isdigit():
                print(f"{COR_VERMELHA}Entrada inválida. Por favor, insira um número.{COR_RESET}")
            else:
                turno_valido = True
                pressao = float(pressao)



       ajustada = ajuste_termico(pressao)
       zona = classificar_zona(ajustada)


       soma_ajustadas += ajustada
       leituras_realizadas += 1

       if menor_pressao is None or ajustada < menor_pressao:
           menor_pressao = ajustada

       if zona == "VERDE":
           contagem_verde += 1
           cor_zona = COR_VERDE
       elif zona == "AMARELA":
           cor_zona = COR_AMARELA
       else:
            cor_zona = COR_VERMELHA

       print(f"  Pressão original : {pressao:.2f} UPC")
       print(f"  Pressão ajustada : {ajustada:.2f} UPC")
       print(f"  Zona             :{NEGRITO}{cor_zona}{zona}{COR_RESET}\n")

       if zona == "VERMELHA" and zona_anterior_vermelha:
           limpar_tela()
           print(f"{NEGRITO}{COR_VERMELHA}")
           print("=" * 55)
           print(" [!!!] ALERTA CRÍTICO: FADIGA DE MATERIAL[!!!]")
           print(" DOIS PICOS CONSECUTIVOS NA ZONA VERMELHA DETECTADOS!")
           print(" ESCOAMENTO INTERROMPIDO IMEDIATAMENTE POR SEGURANÇA.")
           print("=" * 55 + f"{COR_RESET}")
           travamento = True
           input(f"\n{NEGRITO}[Pressione ENTER para visualizar o relatório de travamento]{COR_RESET}")
           break

       if zona == 'VERMELHA':
           zona_anterior_vermelha = True
           print(f"{COR_VERMELHA}\n  [AVISO] PICO DETECTADO! Atenção à próxima leitura.{COR_RESET}")
       else:
           zona_anterior_vermelha = False
        
       if not travamento:
           if i < total:
               input(f"\n{NEGRITO}[Pressione ENTER para a próxima leitura]{COR_RESET}")
           else:
               input(f"\n{NEGRITO}[Pressione ENTER para gerar o Relatório Final]{COR_RESET}")

   gerar_relatorio(total, leituras_realizadas, soma_ajustadas, menor_pressao, contagem_verde, travamento)

   

main()