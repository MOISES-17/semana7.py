import streamlit as st

def multiplos_x(x):
  """Crea un arreglo con los múltiplos de x entre 0 y 100,
  calcula la cantidad de elementos y la suma de sus elementos.

  Args:
    x: El número por el cual se calcularán los múltiplos.

  Returns:
    Una tupla que contiene:
      - El arreglo con los múltiplos de x.
      - La cantidad de elementos en el arreglo.
      - La suma de los elementos del arreglo.
  """

  multiplos = []
  cantidad = 0
  suma = 0
  for i in range(101):
    if i % x == 0:
      multiplos.append(i)
      cantidad += 1
      suma += i
  return multiplos, cantidad, suma

def main():
  """Muestra la interfaz de usuario para ingresar el valor de x."""

  st.title("Múltiplos de X")

  x = st.number_input("Ingrese el valor de X:", min_value=1)

  if st.button("Calcular"):
    multiplos, cantidad, suma = multiplos_x(x)
    st.write(f"Arreglo de múltiplos de {x}: {multiplos}")
    st.write(f"Cantidad de elementos: {cantidad}")
    st.write(f"Suma de los elementos: {suma}")

if __name__ == "__main__":
  main()