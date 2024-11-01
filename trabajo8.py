import streamlit as st

def main():
  """Calcula el promedio, mínimo y máximo de puntos contaminantes de los automóviles."""

  st.title("Centro de Verificación de Automóviles")

  n = st.number_input("Ingrese la cantidad de automóviles a registrar:", min_value=1)
  puntos_contaminantes = []

  for i in range(n):
    puntos = st.number_input(f"Ingrese los puntos contaminantes del automóvil {i+1}:", min_value=0)
    puntos_contaminantes.append(puntos)

  promedio = sum(puntos_contaminantes) / n
  minimo = min(puntos_contaminantes)
  maximo = max(puntos_contaminantes)

  st.write(f"El promedio de puntos contaminantes es: {promedio}")
  st.write(f"El automóvil que menos contaminó tiene {minimo} puntos.")
  st.write(f"El automóvil que más contaminó tiene {maximo} puntos.")

  mas_autos = st.checkbox("¿Desea ingresar los datos de otro automóvil?")

  if mas_autos:
    main()  # Llama de nuevo a la función main para registrar más autos

if __name__ == "__main__":
  main()