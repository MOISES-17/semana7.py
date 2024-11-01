import streamlit as st

def calcular_pagos():
    """Calcula el pago mensual y el total pagado en 20 meses."""

    pago_mensual = 10
    total_pagado = 0

    for i in range(20):
        total_pagado += pago_mensual
        pago_mensual *= 2

    st.write(f"El pago mensual es: S/ {pago_mensual}")
    st.write(f"El total pagado después de 20 meses es: S/ {total_pagado}")

def main():
    """Muestra la interfaz de usuario para el cálculo de pagos."""

    st.title("Cálculo de Pagos")

    calcular_pagos()

if __name__ == "__main__":
    main()