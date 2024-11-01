import streamlit as st
    
    #Ejercicio5: generar e imprimir los números pares entre 0 y 100
    st.title("Ejercicio de números pares")

    st.subheader("Ejercicio 5: Números pares entre 0 y 100")
    pares_0_100 = (i for i in range(0,101) if i % 2 == 0)
    st.write("Números pares entre 0 y 100:")
    st.white(pares_0_100)
    