import streamlit as st

def calcular_suma_y_media():
  """Calcula la suma y la media de los números introducidos hasta que se ingrese un cero."""

  suma = 0
  cantidad = 0
  numero = st.number_input("Ingrese un número (0 para salir):", min_value=0)

  while numero != 0:
    suma += numero
    cantidad += 1
    numero = st.number_input("Ingrese un número (0 para salir):", min_value=0)

  if cantidad > 0:
    media = suma / cantidad
    st.write(f"La suma de los números es: {suma}")
    st.write(f"La media de los números es: {media}")
  else:
    st.write("No se ingresaron números.")

def main():
  """Muestra la interfaz de usuario para ingresar los números."""

  st.title("Cálculo de Suma y Media")

  calcular_suma_y_media()

if __name__ == "__main__":
  main()