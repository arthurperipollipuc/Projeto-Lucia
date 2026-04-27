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
 
    # calcula média e percentual verde (evita divisão por zero)
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
