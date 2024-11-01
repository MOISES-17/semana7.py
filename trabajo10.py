import streamlit as st
def encontrar_mayor(array):
    """Encuentra el número mayor en un array.
    Args:
        array: El array de números.
    Returns:
        El número mayor del array.
    """
    if len(array) == 0:
        return None
    mayor = array[0]
    for numero in array:
        if numero > mayor:
            mayor = numero
    return mayor
def main():
    """Crea un array de números, lo llena con datos ingresados por el usuario y encuentra el mayor."""

    st.title("Encontrar el Número Mayor")

    tamaño = st.number_input("Ingrese el tamaño del array:", min_value=1)
    array = []
    for i in range(tamaño):
        numero = st.number_input(f"Ingrese el número {i+1}:")
        array.append(numero)
    mayor = encontrar_mayor(array)
    if mayor is not None:
        st.write(f"El array es: {array}")
        st.write(f"El número mayor del array es: {mayor}")
    else:
        st.write("El array está vacío.")

if __name__ == "__main__":
    main()