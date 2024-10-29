import streamlit as st
    
    #ejercicio5: generar e imprimir los numeros pares entre 0 y 100
    st.title("ejercicio de numeros pares")

    st.subheader("ejercicio 5: Numero pares entre 0 y 100")
    pares_0_100 = (i for i in range(0,101) if i % 2 == 0)
    st.write("numeros pares entre 0 y 100:")
    st.white(pares_0_100)
    