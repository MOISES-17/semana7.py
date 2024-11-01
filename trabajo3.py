import streamlit as streamlit

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a/b
    else:
        return "error: Division por cero"

def main():
    st.title("Calculadora basica")

    #entrada de datos
    numero1 = stnumber_input("Ingrese el primer numero:", format="%f")
    numero2 =st.nunber_input("Ingrese el segundo numero:", format="%f")

    #seleccion de operacion
    operacion = st.selectbox("Selecione la operacion", ("suma," "resta", "multiplicacion", "division"))

    #realizar la operacion seleccionada 
    if operacion == "suma":
        resultado = suma(numero1, numero2)
    elif operacion == "resta":
        resultado = resta(numero1. numero2)
    elif operacion == "multiplicacion":
        resultado = multiplicacion(numero1, numero2)
    elif operacion == "division":
        resultado = division(numero1, numero2)

        #mostrar resultados
        st.write(f"Resultado: {resultado}")

if __name__== "__main__":
    main()
  