# 📦 PredictLog: Previsão de Demanda e Estoque de Segurança

Este projeto aplica conceitos de **Estatística e Ciência de Dados** para resolver um problema real da logística: o equilíbrio entre o custo de estoque e o nível de serviço (SLA).

## 🚀 Objetivo
Automatizar o cálculo do **Ponto de Pedido** e do **Estoque de Segurança** baseando-se na variabilidade real da demanda e no tempo de resposta do fornecedor.

## 🧠 Conceitos Aplicados

### 1. Estoque de Segurança
Utilizamos a fórmula estatística que considera a incerteza do período de cobertura:
$$ES = Z \times \sigma \times \sqrt{LT}$$

Onde:
* **$Z$ (Z-Score):** Fator de segurança para garantir um nível de serviço (SLA) de 95% ($Z = 1.65$).
* **$\sigma$ (Desvio Padrão):** Medida da volatilidade das vendas diárias.
* **$LT$ (Lead Time):** Tempo de entrega do fornecedor em dias.

### 2. Ponto de Pedido ($PP$)
O gatilho para a compra, garantindo que o novo lote chegue antes do estoque de segurança ser atingido:
$$PP = (Média\ de\ Vendas \times Lead\ Time) + ES$$



## 🛠️ Tecnologias Utilizadas
* **Python 3.x**
* **Pandas:** Manipulação e tratamento de séries temporais de vendas.
* **NumPy:** Cálculos matemáticos e geração de distribuições normais.
* **Matplotlib:** Visualização da demanda e indicadores de controle.

## 📊 Resultados Visualizados
O script gera um gráfico que permite identificar:
* Picos de demanda acima da média.
* Nível crítico para disparo de novas ordens de compra.
* Estatísticas descritivas do giro de estoque.

![Gráfico de Previsão de Demanda](analise_estoque.png)
---
*Projeto desenvolvido por **Adriano Soares**, unindo experiência em logística e análise de dados.*

