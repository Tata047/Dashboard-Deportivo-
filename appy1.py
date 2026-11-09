import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dashboard Deportivo", layout="centered")

st.title("Panel de rendimiento: Equipo Datos Santoto")
st.write("Estadisticas clave de los juegos en el semestre actual")

datos = {
    "jugador": ["Sebastian", "Manuel", "Cristian", "Gabriela"],
    "Goles": [18,14,20,1],
    "Asistencias": [5,7,10,2]

}

""" df = pd.DataFrame(datos)

col1,col2,col3,col4 = st.columns(4)

st.write(f"Goles totales: {df['Goles'].sum()}")
st.write(f"Asistencias totales: {df['Asistencias'].sum()}")
st.write(f"Goleador del equipo: {df.loc[df['Goles'].idxmax()]['jugador']}") """

df = pd.DataFrame(datos)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Goles totales", df['Goles'].sum(), delta = "3+ vs partito anterior")
col2.metric("Asistencias totales", df['Asistencias'].sum())
col3.metric("Goleador del equipo", df.loc[df['Goles'].idxmax(),"jugador"])
col4.metric("Posicion de liga del Equipo", value="3er lugar", delta = "-1 puesto")



st.subheader("Estadisticas al detalle")
st.dataframe(df)

st.subheader("Agregar nuevo jugador")
st.bar_chart(df.set_index("jugador"))
