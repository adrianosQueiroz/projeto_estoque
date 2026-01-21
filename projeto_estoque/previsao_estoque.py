import numpy as np
import pandas as pd
from  datetime import datetime, timedelta
import matplotlib.pyplot as plt


    # gerar todos os dias de 2025:
def gerar_dados(dias = 365):
    x = datetime(2025, 1, 1)
    datas = [x + timedelta(days=i) for i in range(dias)]


    # 2. Gerar vendas fictícias (Média de 50 peças/dia, Desvio Padrão de 15)
        # np.random.normal(media, desvio_padrao, quantidade)
    np.random.seed(42) # Mantém os dados iguais toda vez que rodar
    vendas = np.random.normal(50, 15, dias)
        
        # Garantir que não existam vendas negativas e converter para inteiros
    vendas = np.where(vendas < 0, 0, vendas).astype(int)
        
        # 3. Montar o DataFrame
    df = pd.DataFrame({
            'data': datas,
            'vendas': vendas
        })
    
    return df


if __name__ == "__main__":
    df_vendas = gerar_dados()
    
            # 1. Parâmetros de Logística
    lead_time = 7  # O fornecedor demora 7 dias para entregar
    z_score = 1.65 # Nível de serviço de 95% (padrão de mercado)

    # 2. Cálculos Estatísticos
    media_vendas = df_vendas['vendas'].mean()
    desvio_padrao = df_vendas['vendas'].std()

    # Fórmulas
estoque_seguranca = z_score * desvio_padrao * np.sqrt(lead_time)
consumo_durante_lead_time = media_vendas * lead_time
ponto_pedido = consumo_durante_lead_time + estoque_seguranca

# 3. Visualização com Matplotlib
plt.style.use('bmh') # Estilo visual mais limpo
plt.figure(figsize=(12, 6))

# Plotar as vendas diárias (o histórico)
plt.plot(df_vendas['data'], df_vendas['vendas'], label='Vendas Diárias', color='skyblue', alpha=0.8)

# Adicionar linha da média diária
plt.axhline(media_vendas, color='green', linestyle='--', label=f'Média Diária ({media_vendas:.1f})')

# Adicionar a linha do Ponto de Pedido (PP)
# Nota: Para o gráfico diário ficar comparável, vamos dividir o PP pelo Lead Time 
# ou apenas mostrar o nível de criticidade diária. 
# Aqui vamos focar em mostrar o nível de "alerta" de vendas.
plt.title('Análise de Demanda e Gestão de Estoque', fontsize=14)
plt.xlabel('Tempo (Dias)')
plt.ylabel('Unidades Vendidas')

# Adicionar uma caixa de texto com os KPIs no gráfico
texto_kpi = (f"Lead Time: {lead_time} dias\n"
             f"SLA: 95%\n"
             f"Estoque Segurança: {int(estoque_seguranca)} un\n"
             f"Ponto de Pedido: {int(ponto_pedido)} un")

plt.gca().text(0.02, 0.95, texto_kpi, transform=plt.gca().transAxes, fontsize=10,
               verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.5))

plt.legend(loc='upper right')
plt.tight_layout()

# Salvar o gráfico e mostrar
plt.savefig('analise_estoque.png')
print("Gráfico 'analise_estoque.png' gerado com sucesso!")
plt.show()

print(f"\n--- RELATÓRIO DE COMPRAS ---")
print(f"Consumo Médio no Período: {int(consumo_durante_lead_time)} unidades")
print(f"Estoque de Segurança Necessário: {int(estoque_seguranca)} unidades")
print(f"Ação: Disparar novo pedido ao chegar em {int(ponto_pedido)} unidades no estoque.")
