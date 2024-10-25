import streamlit as st
def verificar_contrasena():
    st.title("verificacion de contarseña")

    #contraseña correcta
    contrasena_correcta = "asdasd"

    #inicializar variable de sesion para almacenar la entrada de usuario
    if "contrasena_ingresada" not in st.session_state:
        st.session_state.contrasena_ingresada = ""

        #imput de la contraseña
        contrasena_ingresada = st.text_input("ingrese la contraseña",type="pasword")

    #boton para verificar la contraseña
     if st.button("verificar"):
        if contrasena_ingresada == contrasena_correcta
            st.session_state.contrasena_ingresada = contrasena_ingresada
            st.success("bienvenido")
        else:
                st.error("contraseña_incorrecta, intente de nuevo")


#llamada la funcion principal
if __name__=="__main__":
    verificar_contrasena()