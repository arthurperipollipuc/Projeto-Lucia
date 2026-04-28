# ============================================================
#   SEUC-4 - Sistema de Escoamento de Unidades de Carga
#   Refinaria Delta-9
# ============================================================
 
def ajuste_termico(pressao):
    """Aplica o ajuste térmico à leitura de pressão."""
    if pressao > 150:
        return pressao * 1.08   
    else:
        return pressao * 0.96   
 
 
def classificar_zona(pressao_ajustada):
    """Retorna a zona de estabilidade da leitura ajustada."""
    if pressao_ajustada > 250:
        return "VERMELHA"       
    elif 120 <= pressao_ajustada <= 180:
        return "VERDE"          
    else:
        return "AMARELA"        
 
 
def exibir_leitura(numero, pressao_original, pressao_ajustada, zona):
    """Exibe os dados de uma leitura formatada."""
    print(f"\n  Leitura #{numero}")
    print(f"    Pressão original : {pressao_original:.2f} UPC")
    print(f"    Pressão ajustada : {pressao_ajustada:.2f} UPC")
    print(f"    Zona             : {zona}")
 
 
def exibir_relatorio(total_leituras, soma_ajustadas, menor_pressao,
                     contagem_verde, travamento, leituras_realizadas):
    """Exibe o relatório final de métricas."""
    print("\n" + "=" * 50)
    print("        RELATÓRIO FINAL - SEUC-4")
    print("=" * 50)

                      
    media = soma_ajustadas / leituras_realizadas if leituras_realizadas > 0 else 0
    percentual_verde = (contagem_verde / leituras_realizadas * 100) if leituras_realizadas > 0 else 0
 
    print(f"  Leituras realizadas    : {leituras_realizadas} de {total_leituras}")
    print(f"  Média das pressões     : {media:.2f} UPC")
    print(f"  Menor pressão ajustada : {menor_pressao:.2f} UPC")
    print(f"  Leituras na Zona Verde : {percentual_verde:.1f}%")
 
    if travamento:
        percentual_realizado = (leituras_realizadas / total_leituras) * 100
        print(f"\n  * SISTEMA TRAVADO *")
        print(f"  Percentual do turno executado: {percentual_realizado:.1f}%")
        print(f"  Causa: dois picos consecutivos na Zona Vermelha.")
    else:
        print(f"\n  Turno concluído sem travamentos.")
 
    print("=" * 50)

def processar_leituras(total_leituras, numero_atual,
                       soma_ajustadas, menor_pressao,
                       contagem_verde, zona_anterior_vermelha):
    """
    Função recursiva que processa cada leitura.
    Retorna (soma_ajustadas, menor_pressao, contagem_verde,
             travamento, leituras_realizadas).
    """
    # caso base: todas as leituras foram concluídas
    if numero_atual > total_leituras:
        return soma_ajustadas, menor_pressao, contagem_verde, False, total_leituras
 
    print(f"\n--- Leitura {numero_atual} de {total_leituras} ---")
    pressao = float(input("  Digite a pressão (UPC): "))
 
    ajustada = ajuste_termico(pressao)
    zona = classificar_zona(ajustada)
 
    exibir_leitura(numero_atual, pressao, ajustada, zona)
 
    # atualiza os acumuladores do turno
    nova_soma  = soma_ajustadas + ajustada
    nova_menor = ajustada if ajustada < menor_pressao else menor_pressao
    nova_verde = contagem_verde + (1 if zona == "VERDE" else 0)
 
    # caso base: dois vermelhos seguidos → trava o sistema
    if zona == "VERMELHA" and zona_anterior_vermelha:
        print("\n  !!! ALERTA CRITICO: Dois picos consecutivos na Zona Vermelha !!!")
        print("  !!! ESCOAMENTO INTERROMPIDO IMEDIATAMENTE !!!")
        return nova_soma, nova_menor, nova_verde, True, numero_atual
 
    # avança para a próxima leitura, informando se a zona atual foi vermelha
    return processar_leituras(
        total_leituras,
        numero_atual + 1,
        nova_soma,
        nova_menor,
        nova_verde,
        zona == "VERMELHA"
    )
 
 
def main():
    print("=" * 50)
    print("   SEUC-4 - Refinaria Delta-9")
    print("   Sistema de Escoamento de Unidades de Carga")
    print("=" * 50)
 
    total = int(input("\nInforme o número total de leituras do turno: "))
 
    if total <= 0:
        print("Número de leituras inválido. Encerrando.")
        return
 
    # inicia a recursão; menor_pressao começa em infinito para ser
    # substituído pela primeira leitura real
    soma, menor, verde, travamento, realizadas = processar_leituras(
        total_leituras=total,
        numero_atual=1,
        soma_ajustadas=0.0,
        menor_pressao=float('inf'),
        contagem_verde=0,
        zona_anterior_vermelha=False
    )
 
    exibir_relatorio(total, soma, menor, verde, travamento, realizadas)
 
 
main()
