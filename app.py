import pandas as pd
import streamlit as st

# Configuración de la página en modo ancho
st.set_page_config(
    page_title="Suite de Ingeniería de Alimentos - Pro",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- MENÚ DE NAVEGACIÓN LATERAL ---
st.sidebar.title("AGRO-ING SUITE")
st.sidebar.markdown("*Edición Profesional v2.0*")
st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Navegación",
    [
        "🏠 Inicio / Presentación",
        "🧪 Acidez Titulable",
        "🍬 Sólidos Solubles (°Brix)",
        "🔥 Fatalidad Térmica (F0)",
        "⚖️ Balance de Materia",
    ],
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "**Desarrollado por:**\nMoises Olivares (Olivares)"
)

# ==========================================
# 1. PÁGINA DE INICIO / PRESENTACIÓN
# ==========================================
if menu == "🏠 Inicio / Presentación":
  st.title("Suite de Ingeniería de Alimentos")
  st.subheader(
      "Plataforma computacional avanzada para el control de operaciones"
      " unitarias"
  )

  st.markdown(
      """
    Bienvenido a la herramienta integral diseñada para optimizar cálculos analíticos y de procesos agroindustriales. 
    Navega a través de la barra lateral para acceder a los diferentes módulos operativos.
    """
  )

  st.markdown("---")
  col1, col2 = st.columns(2)

  with col1:
    st.markdown("### ✨ Autoría y Desarrollo")
    st.markdown(
        """
        * **Creador Principal:** Moises Olivares (Olivares)
        * **Área:** Ingeniería de Alimentos
        * **Estándar:** Arquitectura computacional orientada a procesos industriales
        """
    )

  with col2:
    st.markdown("### 🚀 Módulos Disponibles")
    st.markdown(
        """
        1. **Acidez Titulable:** Cálculo de porcentajes de ácidos orgánicos.
        2. **Sólidos Solubles:** Corrección térmica de lecturas de refractómetro.
        3. **Fatalidad Térmica:** Evaluación de esterilidad comercial ($F_0$).
        4. **Balance de Materia:** Estandarización y diluciones.
        """
    )

# ==========================================
# 2. MÓDULO: ACIDEZ TITULABLE
# ==========================================
elif menu == "🧪 Acidez Titulable":
  st.title("Cálculo de Acidez Titulable (%)")
  st.write(
      "Determina el porcentaje de acidez expresado en función del ácido"
      " predominante de la muestra."
  )

  col1, col2 = st.columns(2)
  with col1:
    gasto_naoh = st.number_input(
        "Gasto de NaOH (mL)", min_value=0.0, value=5.5, format="%.2f"
    )
    norm_naoh = st.number_input(
        "Normalidad del NaOH (eq/L)", min_value=0.0, value=0.1, format="%.3f"
    )

  with col2:
    alicuota = st.number_input(
        "Volumen de Alícuota / Muestra (mL o g)",
        min_value=0.1,
        value=10.0,
        format="%.2f",
    )
    tipo_acido = st.selectbox(
        "Ácido Predominante",
        [
            "Ácido Cítrico (MEQ = 0.064)",
            "Ácido Láctico (MEQ = 0.090)",
            "Ácido Tartárico (MEQ = 0.075)",
            "Ácido Acético (MEQ = 0.060)",
        ],
    )

  meq_dict = {
      "Ácido Cítrico (MEQ = 0.064)": 0.064,
      "Ácido Láctico (MEQ = 0.090)": 0.090,
      "Ácido Tartárico (MEQ = 0.075)": 0.075,
      "Ácido Acético (MEQ = 0.060)": 0.060,
  }
  meq = meq_dict[tipo_acido]

  if st.button("Calcular Acidez", type="primary"):
    try:
      acidez = (gasto_naoh * norm_naoh * meq * 100) / alicuota
      st.success(f"### Acidez Titulable: {acidez:.4f} %")
    except Exception as e:
      st.error(f"Error en el cálculo: {e}")

# ==========================================
# 3. MÓDULO: SÓLIDOS SOLUBLES (°BRIX)
# ==========================================
elif menu == "🍬 Sólidos Solubles (°Brix)":
  st.title("Lectura de Sólidos Solubles (°Brix)")
  st.write("Corrección por temperatura de lecturas refractométricas.")

  col1, col2 = st.columns(2)
  with col1:
    brix_lectura = st.number_input(
        "Lectura del Refractómetro (°Brix)",
        min_value=0.0,
        value=15.0,
        format="%.2f",
    )
  with col2:
    temp_muestra = st.number_input(
        "Temperatura de la Muestra (°C)", value=25.0, format="%.2f"
    )

  if st.button("Corregir °Brix", type="primary"):
    factor = (temp_muestra - 20) * 0.075
    brix_corregido = brix_lectura + factor
    st.success(f"### °Brix Corregidos (a 20°C): {brix_corregido:.2f} °Brix")

# ==========================================
# 4. MÓDULO: FATALIDAD TÉRMICA (F0)
# ==========================================
elif menu == "🔥 Fatalidad Térmica (F0)":
  st.title("Control de Proceso Térmico (Valor F0)")
  st.write(
      "Evaluación de la letalidad acumulada y esterilidad comercial en"
      " tratamientos térmicos."
  )

  col1, col2 = st.columns(2)
  with col1:
    t_ref = st.number_input(
        "Temperatura de Referencia (°C)", value=121.1, format="%.1f"
    )
  with col2:
    z_val = st.number_input("Valor z (°C)", value=10.0, format="%.2f")

  temp_input = st.text_input(
      "Temperaturas registradas (separadas por comas):",
      "105.5, 112.0, 117.5, 120.2, 122.8, 121.5, 119.0, 115.3, 110.1, 106.0",
  )
  time_input = st.text_input(
      "Intervalos de tiempo en minutos (separados por comas):",
      "1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0",
  )

  if st.button("Procesar Letalidad", type="primary"):
    try:
      temperaturas = [float(x.strip()) for x in temp_input.split(",")]
      tiempos = [float(x.strip()) for x in time_input.split(",")]

      if len(temperaturas) == len(tiempos) and len(temperaturas) > 0:
        pasos = list(range(1, len(temperaturas) + 1))
        letalidades = [10 ** ((T - t_ref) / z_val) for T in temperaturas]
        fatalidad_parcial = [l * dt for l, dt in zip(letalidades, tiempos)]
        f0_acumulado = sum(fatalidad_parcial)

        df = pd.DataFrame({
            "Paso": pasos,
            "Tiempo (min)": tiempos,
            "Temp (°C)": temperaturas,
            "Letalidad Parcial": fatalidad_parcial,
        })

        st.markdown("### 📊 Registro de Datos")
        st.dataframe(df, use_container_width=True)

        st.markdown("### 🎯 Resultado del Proceso")
        st.markdown(f"Valor de F0 Acumulado: **{f0_acumulado:.4f} minutos**")

        if f0_acumulado >= 3.0:
          st.success(
              "✅ Estado: PROCESO SEGURO (Esterilidad comercial alcanzada)."
          )
        else:
          st.error(
              "⚠️ Estado: PROCESO INSECURO (No se alcanza el valor F requerido)."
          )
      else:
        st.warning(
            "⚠️ La cantidad de valores de temperatura y tiempo debe coincidir."
        )
    except Exception as e:
      st.error(f"Error al procesar los datos: {e}")

# ==========================================
# 5. MÓDULO: BALANCE DE MATERIA
# ==========================================
elif menu == "⚖️ Balance de Materia":
  st.title("Balance de Materia: Estandarización / Dilución")
  st.write(
      "Cálculo de mezcla y ajuste de concentraciones en operaciones unitarias."
  )

  col1, col2, col3 = st.columns(3)
  with col1:
    m1 = st.number_input(
        "Masa o Volumen inicial (M1 o V1)",
        min_value=0.0,
        value=100.0,
        format="%.2f",
    )
  with col2:
    c1 = st.number_input(
        "Concentración inicial (% o °Brix C1)",
        min_value=0.0,
        value=30.0,
        format="%.2f",
    )
  with col3:
    c2 = st.number_input(
        "Concentración deseada (% o °Brix C2)",
        min_value=0.0,
        value=10.0,
        format="%.2f",
    )

  if st.button("Calcular Balance", type="primary"):
    if c2 == 0:
      st.error("La concentración final no puede ser cero.")
    else:
      m2 = (m1 * c1) / c2
      agua = m2 - m1
      st.success(f"### Masa Final (M2): {m2:.2f} unidades")
      st.info(f"Agua o solvente a agregar: {abs(agua):.2f} unidades")
