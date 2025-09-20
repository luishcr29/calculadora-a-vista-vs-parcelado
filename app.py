# app.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Calculadora: À Vista vs. Parcelado", layout="wide")

# Título e descrição
st.title("💸 Comprar à Vista ou Parcelado? 🤔")
st.write("Calcule a melhor opção de compra, considerando o desconto à vista e o rendimento do dinheiro em um investimento.")

# --- Seção de Entradas ---
st.subheader("⚙️ Configurações da Compra")

col1, col2 = st.columns(2)

with col1:
    valor_produto = st.number_input(
        "💵 Valor total do produto (R$)", 
        min_value=100.0, 
        value=1000.0, 
        step=100.0
    )
    desconto_vista = st.number_input(
        "🏷️ Desconto para pagamento à vista (%)", 
        min_value=0.0, 
        value=3.0, 
        step=0.5,
        format="%.2f"
    )

with col2:
    taxa_rendimento_mensal = st.number_input(
        "📈 Taxa de rendimento do investimento (% ao mês)", 
        min_value=0.0, 
        value=1.0, 
        step=0.1,
        format="%.2f"
    )
    num_parcelas = st.number_input(
        "🗓️ Número de parcelas", 
        min_value=1, 
        value=2, 
        step=1
    )

# Validação simples para evitar divisão por zero
if num_parcelas <= 0:
    st.error("O número de parcelas deve ser maior que zero.")
    st.stop()

# --- Cálculos ---

# Opção 1: Pagamento à Vista
custo_vista_bruto = valor_produto * (1 - desconto_vista / 100)
valor_desconto = valor_produto - custo_vista_bruto
rendimento_desconto = valor_desconto * ((1 + taxa_rendimento_mensal / 100) ** num_parcelas - 1)
custo_vista_liquido = custo_vista_bruto - rendimento_desconto

# Opção 2: Pagamento Parcelado
valor_parcela = valor_produto / num_parcelas
rendimento_total_parcelado = 0.0
rendimentos_por_mes = []
saldo_por_mes = []

saldo_atual = valor_produto

for mes in range(1, num_parcelas + 1):
    rendimento_mes = saldo_atual * (taxa_rendimento_mensal / 100)
    rendimento_total_parcelado += rendimento_mes
    rendimentos_por_mes.append(rendimento_total_parcelado)

    saldo_atual = saldo_atual + rendimento_mes - valor_parcela
    saldo_por_mes.append(saldo_atual)

custo_parcelado_liquido = valor_produto - rendimento_total_parcelado

# --- Resultados e Visualização ---

st.markdown("---")
st.subheader("📊 Análise Financeira")

col_vista, col_parcelado = st.columns(2)

with col_vista:
    st.metric(
        label="💰 Custo à Vista (com desconto)",
        value=f"R$ {custo_vista_bruto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    st.info(f"**Rendimento do Desconto:** R$ {rendimento_desconto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    st.info(f"**Saldo no Final do Período:** R$ {valor_desconto + rendimento_desconto:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    st.metric(
        label="✅ Custo Líquido Final",
        value=f"R$ {custo_vista_liquido:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

with col_parcelado:
    st.metric(
        label="💰 Custo Parcelado (sem desconto)",
        value=f"R$ {valor_produto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    st.info(f"**Rendimento do Parcelamento:** R$ {rendimento_total_parcelado:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    st.info(f"**Saldo no Final do Período:** R$ {rendimento_total_parcelado:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    st.metric(
        label="✅ Custo Líquido Final",
        value=f"R$ {custo_parcelado_liquido:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )


# Comparativo final
st.markdown("---")
if custo_vista_liquido < custo_parcelado_liquido:
    diferenca = custo_parcelado_liquido - custo_vista_liquido
    st.success(
        f"🎉 **Comprar à vista é a melhor opção!** Você economiza R$ {diferenca:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
elif custo_parcelado_liquido < custo_vista_liquido:
    diferenca = custo_vista_liquido - custo_parcelado_liquido
    st.success(
        f"🚀 **Comprar parcelado é a melhor opção!** Você economiza R$ {diferenca:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
else:
    st.info("As duas opções têm o mesmo custo líquido. A escolha é sua!")

# Gráfico de rendimentos
st.subheader("Gráfico de Acumulação de Rendimentos (Opção Parcelada)")
df_grafico = pd.DataFrame({
    'Mês': list(range(1, num_parcelas + 1)),
    'Rendimento Acumulado': rendimentos_por_mes
})

st.line_chart(df_grafico.set_index('Mês'))

# Tabela de detalhes
with st.expander("🧾 Detalhes do Cálculo"):
    detalhes_df = pd.DataFrame(columns=["Mês", "Saldo Inicial", "Rendimento do Mês", "Parcela Paga", "Saldo Final"])
    saldo_calc = valor_produto
    for mes in range(1, num_parcelas + 1):
        saldo_inicial = saldo_calc
        rendimento = saldo_inicial * (taxa_rendimento_mensal / 100)
        saldo_final = saldo_inicial + rendimento - valor_parcela
        
        detalhes_df.loc[mes] = [
            mes,
            f"R$ {saldo_inicial:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            f"R$ {rendimento:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            f"R$ {valor_parcela:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
            f"R$ {saldo_final:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        ]
        saldo_calc = saldo_final

    st.dataframe(detalhes_df.set_index("Mês"))