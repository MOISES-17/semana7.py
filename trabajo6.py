import streamlit as st

def main():
  """Muestra un menú con opciones de Archivo, Editar, Ver y Salir."""

  st.title("Menú de Opciones")

  while True:
    opcion = st.sidebar.selectbox("Seleccione una opción:", ["Archivo", "Editar", "Ver", "Salir"])

    if opcion == "Archivo":
      st.write("**Archivo**")
      # Aquí se puede agregar código para las opciones del menú Archivo
    elif opcion == "Editar":
      st.write("**Editar**")
      # Aquí se puede agregar código para las opciones del menú Editar
    elif opcion == "Ver":
      st.write("**Ver**")
      # Aquí se puede agregar código para las opciones del menú Ver
    elif opcion == "Salir":
      st.write("**¡Hasta luego!**")
      break

if __name__ == "__main__":
    main()