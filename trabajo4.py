import streamlit as st
def validar_datos(marca, modelo, kilometraje):
  """Valida los datos del automóvil.
  Args:
    marca: La marca del automóvil.
    modelo: El modelo del automóvil.
    kilometraje: El kilometraje del automóvil.
  Returns:
    True si los datos son válidos, False en caso contrario.
  """
  if not marca or not modelo or not kilometraje:
    st.error("Por favor, ingrese todos los datos.")
    return False

  if not isinstance(kilometraje, (int, float)) or kilometraje < 0:
    st.error("El kilometraje debe ser un número mayor o igual a 0.")
    return False
  return True
def main():
  """Muestra la interfaz de usuario para ingresar los datos del automóvil."""

  st.title("Registro de Automóviles")
  marca = st.text_input("Marca:")
  modelo = st.text_input("Modelo:")
  kilometraje = st.number_input("Kilometraje:", min_value=0)
  if st.button("Registrar"):
    if validar_datos(marca, modelo, kilometraje):
      st.success("¡Automóvil registrado correctamente!")
      st.write(f"Marca: {marca}")
      st.write(f"Modelo: {modelo}")
      st.write(f"Kilometraje: {kilometraje}")
    else:
      st.error("Por favor, corrija los datos ingresados.")
if __name__ == "__main__":
  main()
