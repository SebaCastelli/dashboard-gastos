import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard de Gastos", layout="wide")

st.title("💸 Dashboard de Gastos")

uploaded_file = st.file_uploader("Subí tu CSV", type=["csv"])

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    st.subheader("Datos")

    st.dataframe(df)

    total = df["monto"].sum()

    ingresos = df[df["monto"] > 0]["monto"].sum()

    gastos = df[df["monto"] < 0]["monto"].sum()

    col1, col2, col3 = st.columns(3)

    col1.metric("Balance", f"${total:,.2f}")
    col2.metric("Ingresos", f"${ingresos:,.2f}")
    col3.metric("Gastos", f"${gastos:,.2f}")

    df_gastos = df[df["monto"] < 0]

    fig = px.pie(
        df_gastos,
        names="descripcion",
        values="monto",
        title="Distribución de gastos"
    )

    st.plotly_chart(fig, use_container_width=True)