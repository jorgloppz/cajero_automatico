import streamlit as st

# --- Lógica del Cajero (la clase original sin cambios) ---
class CajeroAutomatico:
    def __init__(self, saldo_inicial=1000, pin="1234"):
        self.saldo = saldo_inicial
        self.pin = pin

    def autenticar(self, pin_ingresado):
        return pin_ingresado == self.pin

    def consultar_saldo(self):
        return f"Su saldo actual es: ${self.saldo:.2f}"

    def retirar_dinero(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return f"Retiro exitoso. {self.consultar_saldo()}"
        elif cantidad > self.saldo:
            return "Error: Fondos insuficientes."
        else:
            return "Error: Cantidad no válida."

    def depositar_dinero(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. {self.consultar_saldo()}"
        else:
            return "Error: Cantidad no válida."

# --- Interfaz de la App Web con Streamlit ---

st.title("Simulador de Cajero Automático 🏧")

# Inicializar el estado de la sesión si no existe
if 'cajero' not in st.session_state:
    st.session_state.cajero = CajeroAutomatico()
    st.session_state.autenticado = False
    st.session_state.mensajes = []

# Atajo para acceder al cajero y a los mensajes
cajero = st.session_state.cajero
mensajes = st.session_state.mensajes

# --- Pantalla de Autenticación ---
if not st.session_state.autenticado:
    st.header("Login")
    pin_ingresado = st.text_input("Por favor, ingrese su PIN:", type="password", key="pin_input")

    if st.button("Ingresar"):
        if cajero.autenticar(pin_ingresado):
            st.session_state.autenticado = True
            st.success("Autenticación exitosa.")
            st.rerun() # Recarga la app para mostrar el menú principal
        else:
            st.error("PIN incorrecto. Intente de nuevo.")

# --- Pantalla Principal del Cajero ---
else:
    st.header("Menú Principal")

    # Mostrar saldo actual
    st.info(cajero.consultar_saldo())
    
    # Opciones del menú
    opcion = st.radio("Seleccione una opción:", ["Retirar", "Depositar", "Salir"])

    if opcion == "Retirar":
        with st.form("retiro_form"):
            cantidad_retiro = st.number_input("Cantidad a retirar:", min_value=0.0, step=10.0)
            if st.form_submit_button("Confirmar Retiro"):
                resultado = cajero.retirar_dinero(cantidad_retiro)
                st.write(resultado)

    elif opcion == "Depositar":
        with st.form("deposito_form"):
            cantidad_deposito = st.number_input("Cantidad a depositar:", min_value=0.0, step=10.0)
            if st.form_submit_button("Confirmar Depósito"):
                resultado = cajero.depositar_dinero(cantidad_deposito)
                st.write(resultado)
                
    elif opcion == "Salir":
        if st.button("Cerrar Sesión"):
            # Reiniciar el estado para la próxima visita
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.info("Gracias por usar el Cajero Automático. Sesión cerrada.")
            st.rerun()