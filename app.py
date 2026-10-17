import streamlit as st

st.title("Hey, IA 👋")
nombre = st.text_input("¿Cómo te llamas?")
if nombre:
    st.write(f"¡Hola, {nombre}! Esta es mi primera app en internet.")
  
    # Nueva pregunta sobre el origen del usuario
    procedencia = st.text_input("¿De dónde eres?")
    if procedencia:
        st.write("¡Qué bien! Yo soy de Internet. 🌐")
