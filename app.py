import streamlit as st

def motor_de_inferencia(sintomas):
    # Base de conocimientos (Reglas lógicas)
    if "Pérdida de olfato/gusto" in sintomas and "Fiebre" in sintomas:
        return "COVID-19. Se requiere prueba confirmatoria y aislamiento preventivo."
    elif "Picor en los ojos" in sintomas and "Estornudos" in sintomas and "Fiebre" not in sintomas:
        return "Rinitis Alérgica."
    elif "Fiebre" in sintomas and "Dolor muscular severo" in sintomas:
        return "Influenza (Gripe)."
    elif "Tos" in sintomas and "Congestión nasal" in sintomas:
        return "Resfriado Común."
    else:
        return "Cuadro inespecífico o combinación no concluyente. Requiere evaluación médica presencial."

def main():
    st.title("SE: Triage de Enfermedades Respiratorias")
    st.write("Seleccione los síntomas que presenta el paciente para generar una hipótesis diagnóstica.")

    # Interfaz de usuario para la entrada de hechos
    base_sintomas = [
        "Fiebre",
        "Tos",
        "Congestión nasal",
        "Estornudos",
        "Picor en los ojos",
        "Dolor muscular severo",
        "Pérdida de olfato/gusto"
    ]

    sintomas_seleccionados = st.multiselect("Registro de Síntomas", base_sintomas)

    if st.button("Ejecutar Motor de Inferencia"):
        if not sintomas_seleccionados:
            st.warning("Debe ingresar al menos un síntoma en el sistema.")
        else:
            diagnostico = motor_de_inferencia(sintomas_seleccionados)
            st.success(f"**Resultado:** {diagnostico}")

if __name__ == "__main__":
    main()
