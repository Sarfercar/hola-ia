import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Mi Súper App", page_icon="👋", layout="centered")

# Título principal
st.title("Hey, IA 👋")

# Barra lateral para configuraciones
st.sidebar.header("Configuración")
tema = st.sidebar.selectbox("Elige un tema de interés:", ["General", "Tecnología", "Ciencia de Datos"])

# Crear pestañas para organizar el contenido
tab1, tab2 = st.tabs(["Inicio", "Visualización de Datos"])

with tab1:
    st.header("¡Bienvenido!")
    nombre = st.text_input("¿Cómo te llamas?", key="nombre_input")
    
    if nombre:
        st.success(f"¡Hola, {nombre}! Bienvenido/a a mi primera app en internet.")
        st.balloons()  # ¡Efecto divertido!
        
        st.write(f"Has seleccionado el tema: **{tema}** en la barra lateral.")

with tab2:
    st.header("Gráfico Interactivo")
    st.write("Aquí puedes ver un ejemplo de cómo mostrar datos dinámicos de forma visual:")
    
    # Generar datos aleatorios de ejemplo
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['Categoría A', 'Categoría B', 'Categoría C']
    )
    
    # Mostrar gráfico de líneas interactivas
    st.line_chart(chart_data)
    
    # Mostrar la tabla de datos si el usuario lo desea
    if st.checkbox("Mostrar tabla de datos de origen"):
        st.dataframe(chart_data)
