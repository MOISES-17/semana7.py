import streamlit as st
def verificar_contrasena():
    st.title("verificacion de contraseña")

    #contraseña correcta
    contrasena_correcta = "asdasd"

    #inicializar variable de sesion para almacenar la entrada de usuario
    if "contrasena_ingresada" not in st.session_state:
        st.session_state.contrasena_ingresada = ""

     #imput de la contraseña
    contrasena_ingresada = st.text_input("ingrese la contraseña", type="password")

    #boton para verificar la contraseña
    if st.button("verificar"):
        if contrasena_ingresada == contrasena_correcta:
            st.session_state.contrasena_ingresada = contrasena_ingresada
            st.success("bienvenido")
        else:
            st.error("contraseña_incorrecta, intente de nuevo")


#llamada la funcion principal
if __name__=="__main__":
    verificar_contrasena()

------------------------------------
    import streamlit as st
    
    #ejercicio5: generar e imprimir los numeros pares entre 0 y 100
    st.title("ejercicio de numeroa pares")

    st.subheader("ejercicio 5: Numero pares entre 0 y 100")
    pares_0_100 = (i for i in range(0,101) if i % 2 == 0)
    st.write("numeros pares entre 0 y 100:")
    st.white(pares_0_100)
    