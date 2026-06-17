import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📈 Simulador de Investimentos")

capital = st.number_input(
    "Capital Inicial (R$)",
    min_value=0.0,
    value=1000.0
)

taxa = st.number_input(
    "Taxa de Juros Mensal (%)",
    min_value=0.0,
    value=2.0
)

tempo = st.number_input(
    "Tempo (meses)",
    min_value=1,
    value=12
)

if st.button("Calcular"):

    taxa_decimal = taxa / 100

    valores = []


    # ---- evolução mês a mês ----
    for mes in range(1, int(tempo) + 1):
        montante = capital * (1 + taxa_decimal) ** mes
        valores.append(montante)

    # ---- tabela ----
    df = pd.DataFrame({
        "Mês": range(1, int(tempo) + 1),
        "montante": valores
    })

    st.subheader("📋 Evolução mês a mês")
    st.dataframe(df)

    # ---- gráfico ----
    st.subheader("📈 Crescimento do investimento")

    fig, ax = plt.subplots()

    ax.plot(df["Mês"], df["montante"], marker='o')

    ax.set_xlabel("Mês")
    ax.set_ylabel("montante (R$)")

    ax.set_xticks(range(1, int(tempo) + 1))

    ax.grid(True, linestyle='--', alpha=0.5)

    st.pyplot(fig)

    # ---- resultado final ----
    st.success(f"montante Final: R$ {valores[-1]:.2f}")
    st.info(f"Lucro: R$ {valores[-1] - capital:.2f}")