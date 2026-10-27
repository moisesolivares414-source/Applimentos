import math
import customtkinter as ctk

# Configuración global de apariencia
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")


class AppAlimentos(ctk.CTk):

  def __init__(self):
    super().__init__()

    self.title("Suite de Ingeniería de Alimentos - Pro")
    self.geometry("1020x700")
    self.resizable(False, False)

    # --- 1. MENÚ LATERAL MINIMALISTA (SIDEBAR) ---
    self.sidebar_frame = ctk.CTkFrame(
        self, width=240, corner_radius=0, fg_color=("#1f1f1f", "#141414")
    )
    self.sidebar_frame.pack(side="left", fill="y")

    self.logo_label = ctk.CTkLabel(
        self.sidebar_frame,
        text="AGRO-ING SUITE",
        font=ctk.CTkFont(size=20, weight="bold"),
    )
    self.logo_label.pack(pady=(40, 5))

    self.sub_logo = ctk.CTkLabel(
        self.sidebar_frame,
        text="Edición Profesional v2.0",
        font=ctk.CTkFont(size=11, slant="italic"),
        text_color="gray",
    )
    self.sub_logo.pack(pady=(0, 35))

    # Botones de navegación con esquinas muy redondeadas
    self.crear_boton_menu("🏠  Inicio / Presentación", "inicio")
    self.crear_boton_menu("🧪  Acidez Titulable", "acidez")
    self.crear_boton_menu("🍬  Sólidos Solubles (°Brix)", "brix")
    self.crear_boton_menu("🔥  Fatalidad Térmica (F0)", "fatalidad")
    self.crear_boton_menu("⚖️  Balance de Materia", "balance")

    # Crédito institucional en la parte inferior del sidebar
    self.lbl_autor_sidebar = ctk.CTkLabel(
        self.sidebar_frame,
        text="Creado por:\nOlivares",
        font=ctk.CTkFont(size=11, weight="bold"),
        text_color="#666666",
    )
    self.lbl_autor_sidebar.pack(side="bottom", pady=25)

    # --- 2. ÁREA DE CONTENIDO PRINCIPAL ---
    self.content_frame = ctk.CTkFrame(self, fg_color="transparent")
    self.content_frame.pack(
        side="right", fill="both", expand=True, padx=30, pady=30
    )

    self.modulos = {}
    self.inicializar_modulos()
    self.mostrar_modulo("inicio")  # Arranca en la página de presentación

  def crear_boton_menu(self, texto, nombre_modulo):
    btn = ctk.CTkButton(
        self.sidebar_frame,
        text=texto,
        command=lambda: self.mostrar_modulo(nombre_modulo),
        corner_radius=12,
        height=42,
        anchor="w",
        font=ctk.CTkFont(size=13),
        fg_color="transparent",
        hover_color=("#2b2b2b", "#222222"),
    )
    btn.pack(padx=15, pady=6, fill="x")

  def inicializar_modulos(self):
    self.modulos["inicio"] = self.crear_modulo_inicio()
    self.modulos["acidez"] = self.crear_modulo_acidez()
    self.modulos["brix"] = self.crear_modulo_brix()
    self.modulos["fatalidad"] = self.crear_modulo_fatalidad()
    self.modulos["balance"] = self.crear_modulo_balance()

  def mostrar_modulo(self, nombre):
    for mod in self.modulos.values():
      mod.pack_forget()
    self.modulos[nombre].pack(fill="both", expand=True)

  # --- PÁGINA 0: INICIO / PRESENTACIÓN ---
  def crear_modulo_inicio(self):
    frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")

    welcome_card = ctk.CTkFrame(
        frame, fg_color=("#242424", "#1a1a1a"), corner_radius=16
    )
    welcome_card.pack(fill="x", pady=(10, 20), padx=5)

    ctk.CTkLabel(
        welcome_card,
        text="Bienvenido a la Suite de Ingeniería de Alimentos",
        font=ctk.CTkFont(size=22, weight="bold"),
    ).pack(anchor="w", padx=25, pady=(25, 5))

    ctk.CTkLabel(
        welcome_card,
        text=(
            "Plataforma computacional avanzada para el control de operaciones"
            " unitarias, análisis de laboratorio y optimización de procesos"
            " agroindustriales."
        ),
        font=ctk.CTkFont(size=13),
        text_color="#AAAAAA",
        justify="left",
    ).pack(anchor="w", padx=25, pady=(0, 25))

    author_card = ctk.CTkFrame(
        frame, fg_color=("#1e2b22", "#111c15"), corner_radius=16
    )
    author_card.pack(fill="x", pady=10, padx=5)

    ctk.CTkLabel(
        author_card,
        text="✨ Información de Autoría y Desarrollo",
        font=ctk.CTkFont(size=15, weight="bold"),
        text_color="#2ECC71",
    ).pack(anchor="w", padx=25, pady=(20, 5))

    ctk.CTkLabel(
        author_card,
        text=(
            "• Desarrollador Principal y Diseñador de Arquitectura:\n  "
            "Moises David Olivares Vera (Olivares)\n\n• Enfoque Académico y Técnico: "
            "Ingeniería de Alimentos\n• Estándar Visual: Interfaz Minimalista "
            "Industrial con CustomTkinter"
        ),
        font=ctk.CTkFont(size=13),
        text_color="#DDDDDD",
        justify="left",
    ).pack(anchor="w", padx=25, pady=(0, 20))

    modules_card = ctk.CTkFrame(
        frame, fg_color=("#242424", "#1a1a1a"), corner_radius=16
    )
    modules_card.pack(fill="x", pady=10, padx=5)

    ctk.CTkLabel(
        modules_card,
        text="🚀 Módulos Operativos Integrados",
        font=ctk.CTkFont(size=15, weight="bold"),
    ).pack(anchor="w", padx=25, pady=(15, 5))

    ctk.CTkLabel(
        modules_card,
        text=(
            "1. Acidez Titulable: Determinación de porcentajes de ácidos"
            " orgánicos.\n2. Sólidos Solubles (°Brix): Corrección térmica para"
            " refractometría.\n3. Fatalidad Térmica: Cálculo de valor F0 y"
            " esterilidad comercial.\n4. Balance de Materia: Estandarización y"
            " diluciones."
        ),
        font=ctk.CTkFont(size=12),
        text_color="#AAAAAA",
        justify="left",
    ).pack(anchor="w", padx=25, pady=(0, 20))

    return frame

  # --- MÓDULO 1: ACIDEZ TITULABLE ---
  def crear_modulo_acidez(self):
    frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    ctk.CTkLabel(
        frame,
        text="Cálculo de Acidez Titulable (%)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=(0, 15))

    form_card = ctk.CTkFrame(
        frame, fg_color=("#242424", "#1a1a1a"), corner_radius=16
    )
    form_card.pack(fill="x", pady=5)

    self.ent_gasto = ctk.CTkEntry(
        form_card, placeholder_text="Gasto de NaOH (mL)", width=440, height=38
    )
    self.ent_gasto.pack(pady=12, padx=25)

    self.ent_norm = ctk.CTkEntry(
        form_card,
        placeholder_text="Normalidad del NaOH (ej. 0.1)",
        width=440,
        height=38,
    )
    self.ent_norm.pack(pady=12, padx=25)

    self.ent_alicuota = ctk.CTkEntry(
        form_card,
        placeholder_text="Volumen de Alícuota/Muestra (mL o g)",
        width=440,
        height=38,
    )
    self.ent_alicuota.pack(pady=12, padx=25)

    self.cbo_acido = ctk.CTkOptionMenu(
        form_card,
        values=[
            "Ácido Cítrico (0.064)",
            "Ácido Láctico (0.090)",
            "Ácido Tartárico (0.075)",
            "Ácido Acético (0.060)",
        ],
        width=440,
        height=38,
    )
    self.cbo_acido.pack(pady=(12, 22), padx=25)

    ctk.CTkButton(
        frame,
        text="Calcular % de Acidez",
        command=self.calcular_acidez,
        height=40,
        corner_radius=10,
        font=ctk.CTkFont(size=14, weight="bold"),
    ).pack(anchor="w", pady=12)

    self.res_card_acidez = ctk.CTkFrame(
        frame, fg_color=("#1c1c1c", "#121212"), corner_radius=16
    )
    self.res_card_acidez.pack(fill="x", pady=5)

    self.lbl_res_acidez = ctk.CTkLabel(
        self.res_card_acidez,
        text="Resultado: Esperando datos de entrada...",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#888888",
    )
    self.lbl_res_acidez.pack(pady=16, padx=25, anchor="w")
    return frame

  def calcular_acidez(self):
    try:
      v = float(self.ent_gasto.get())
      n = float(self.ent_norm.get())
      m = float(self.ent_alicuota.get())
      seleccion = self.cbo_acido.get()
      meq = float(seleccion.split("(")[1].replace(")", ""))

      acidez = (v * n * meq * 100) / m
      self.res_card_acidez.configure(fg_color=("#1e3d2f", "#112b20"))
      self.lbl_res_acidez.configure(
          text=f"Acidez Titulable: {acidez:.4f} %", text_color="#2ECC71"
      )
    except ValueError:
      self.res_card_acidez.configure(fg_color=("#3d1e1e", "#2b1111"))
      self.lbl_res_acidez.configure(
          text="Error: Ingrese valores numéricos válidos", text_color="#E74C3C"
      )

  # --- MÓDULO 2: SÓLIDOS SOLUBLES (°BRIX) ---
  def crear_modulo_brix(self):
    frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    ctk.CTkLabel(
        frame,
        text="Lectura de Sólidos Solubles (°Brix)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=(0, 15))

    form_card = ctk.CTkFrame(
        frame, fg_color=("#242424", "#1a1a1a"), corner_radius=16
    )
    form_card.pack(fill="x", pady=5)

    self.ent_brix = ctk.CTkEntry(
        form_card,
        placeholder_text="Lectura del Refractómetro (°Brix)",
        width=440,
        height=38,
    )
    self.ent_brix.pack(pady=20, padx=25)

    self.ent_temp = ctk.CTkEntry(
        form_card,
        placeholder_text="Temperatura de Muestra (°C)",
        width=440,
        height=38,
    )
    self.ent_temp.pack(pady=(0, 20), padx=25)

    ctk.CTkButton(
        frame,
        text="Procesar Lectura y Corregir",
        command=self.calcular_brix,
        height=40,
        corner_radius=10,
        font=ctk.CTkFont(size=14, weight="bold"),
    ).pack(anchor="w", pady=12)

    self.res_card_brix = ctk.CTkFrame(
        frame, fg_color=("#1c1c1c", "#121212"), corner_radius=16
    )
    self.res_card_brix.pack(fill="x", pady=5)

    self.lbl_res_brix = ctk.CTkLabel(
        self.res_card_brix,
        text="Estado: Esperando datos...",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#888888",
    )
    self.lbl_res_brix.pack(pady=16, padx=25, anchor="w")
    return frame

  def calcular_brix(self):
    try:
      brix = float(self.ent_brix.get())
      temp = float(self.ent_temp.get())
      factor = (temp - 20) * 0.075
      brix_corregido = brix + factor

      self.res_card_brix.configure(fg_color=("#1e3d2f", "#112b20"))
      self.lbl_res_brix.configure(
          text=f"°Brix Corregidos (a 20°C): {brix_corregido:.2f} °Brix",
          text_color="#2ECC71",
      )
    except ValueError:
      self.res_card_brix.configure(fg_color=("#3d1e1e", "#2b1111"))
      self.lbl_res_brix.configure(
          text="Error: Revise los datos ingresados", text_color="#E74C3C"
      )

  # --- MÓDULO 3: FATALIDAD TÉRMICA ---
  def crear_modulo_fatalidad(self):
    frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    ctk.CTkLabel(
        frame,
        text="Control de Proceso Térmico (Valor F0)",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=(0, 10))

    param_card = ctk.CTkFrame(
        frame, fg_color=("#242424", "#1a1a1a"), corner_radius=16
    )
    param_card.pack(fill="x", pady=5)

    ctk.CTkLabel(
        param_card,
        text="Parámetros del Proceso",
        font=ctk.CTkFont(size=12, weight="bold"),
        text_color="#AAAAAA",
    ).pack(anchor="w", padx=20, pady=(12, 4))

    f_params = ctk.CTkFrame(param_card, fg_color="transparent")
    f_params.pack(fill="x", padx=20, pady=(0, 12))

    ctk.CTkLabel(f_params, text="Temp. Referencia (°C):").pack(
        side="left", padx=(0, 8)
    )
    self.ent_tref = ctk.CTkEntry(f_params, width=90, height=32)
    self.ent_tref.insert(0, "121.1")
    self.ent_tref.pack(side="left", padx=(0, 25))

    ctk.CTkLabel(f_params, text="Valor z (°C):").pack(
        side="left", padx=(0, 8)
    )
    self.ent_z = ctk.CTkEntry(f_params, width=90, height=32)
    self.ent_z.insert(0, "10.0")
    self.ent_z.pack(side="left")

    input_card = ctk.CTkFrame(
        frame, fg_color=("#242424", "#1a1a1a"), corner_radius=16
    )
    input_card.pack(fill="x", pady=6)

    ctk.CTkLabel(
        input_card,
        text="Temperaturas registradas (separadas por comas):",
        font=ctk.CTkFont(size=12),
    ).pack(anchor="w", padx=20, pady=(12, 2))
    self.ent_temps = ctk.CTkEntry(input_card, height=35)
    self.ent_temps.insert(
        0, "105.5, 112.0, 117.5, 120.2, 122.8, 121.5, 119.0, 115.3, 110.1, 106.0"
    )
    self.ent_temps.pack(fill="x", padx=20, pady=(0, 8))

    ctk.CTkLabel(
        input_card,
        text="Intervalos de tiempo en minutos (separados por comas):",
        font=ctk.CTkFont(size=12),
    ).pack(anchor="w", padx=20, pady=(2, 2))
    self.ent_times = ctk.CTkEntry(input_card, height=35)
    self.ent_times.insert(
        0, "1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0"
    )
    self.ent_times.pack(fill="x", padx=20, pady=(0, 14))

    ctk.CTkButton(
        frame,
        text="Procesar y Calcular Letalidad",
        command=self.calcular_fatalidad,
        height=38,
        corner_radius=10,
        font=ctk.CTkFont(size=14, weight="bold"),
    ).pack(anchor="w", pady=8)

    self.txt_tabla = ctk.CTkTextbox(
        frame, height=110, font=ctk.CTkFont(family="Consolas", size=11)
    )
    self.txt_tabla.pack(fill="x", pady=5)
    self.txt_tabla.insert(
        "1.0", " [ Registro de Datos y Letalidades Parciales ]\n"
    )
    self.txt_tabla.configure(state="disabled")

    self.res_card_fat = ctk.CTkFrame(
        frame, fg_color=("#1c1c1c", "#121212"), corner_radius=16
    )
    self.res_card_fat.pack(fill="x", pady=5)

    self.lbl_res_fatalidad = ctk.CTkLabel(
        self.res_card_fat,
        text="Resultado F0 Acumulado: -- min",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#888888",
    )
    self.lbl_res_fatalidad.pack(pady=14, padx=20, anchor="w")
    return frame

  def calcular_fatalidad(self):
    try:
      tref = float(self.ent_tref.get())
      z = float(self.ent_z.get())
      temps = [float(x.strip()) for x in self.ent_temps.get().split(",")]
      times = [float(x.strip()) for x in self.ent_times.get().split(",")]

      if len(temps) != len(times) or len(temps) == 0:
        self.res_card_fat.configure(fg_color=("#3d1e1e", "#2b1111"))
        self.lbl_res_fatalidad.configure(
            text="Error: Cantidad de temperaturas y tiempos no coincide.",
            text_color="#E74C3C",
        )
        return

      letalidades = [10 ** ((T - tref) / z) for T in temps]
      parciales = [l * dt for l, dt in zip(letalidades, times)]
      f0_total = sum(parciales)

      tabla_str = (
          f"{'Paso':<5} | {'Tiempo(min)':<11} | {'Temp(°C)':<9} |"
          f" {'Letalidad Parcial':<16}\n"
      )
      tabla_str += "-" * 50 + "\n"
      for i, (t, T, p) in enumerate(zip(times, temps, parciales), 1):
        tabla_str += (
            f"{i:<5} | {t:<11.1f} | {T:<9.1f} | {p:<16.4f}\n"
        )

      self.txt_tabla.configure(state="normal")
      self.txt_tabla.delete("1.0", "end")
      self.txt_tabla.insert("1.0", tabla_str)
      self.txt_tabla.configure(state="disabled")

      if f0_total >= 3.0:
        self.res_card_fat.configure(fg_color=("#1e3d2f", "#112b20"))
        self.lbl_res_fatalidad.configure(
            text=f"✅ F0 Acumulado: {f0_total:.4f} min — PROCESO SEGURO",
            text_color="#2ECC71",
        )
      else:
        self.res_card_fat.configure(fg_color=("#3d1e1e", "#2b1111"))
        self.lbl_res_fatalidad.configure(
            text=f"⚠️ F0 Acumulado: {f0_total:.4f} min — PROCESO INSECURO",
            text_color="#E74C3C",
        )
    except ValueError:
      self.res_card_fat.configure(fg_color=("#3d1e1e", "#2b1111"))
      self.lbl_res_fatalidad.configure(
          text="Error: Verifique que los campos numéricos sean válidos.",
          text_color="#E74C3C",
      )

  # --- MÓDULO 4: BALANCE DE MATERIA ---
  def crear_modulo_balance(self):
    frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
    ctk.CTkLabel(
        frame,
        text="Balance de Materia: Estandarización / Dilución",
        font=ctk.CTkFont(size=20, weight="bold"),
    ).pack(anchor="w", pady=(0, 10))

    form_card = ctk.CTkFrame(
        frame, fg_color=("#242424", "#1a1a1a"), corner_radius=16
    )
    form_card.pack(fill="x", pady=5)

    self.ent_m1 = ctk.CTkEntry(
        form_card,
        placeholder_text="Masa o Volumen inicial (M1 o V1)",
        width=440,
        height=38,
    )
    self.ent_m1.pack(pady=12, padx=25)

    self.ent_c1 = ctk.CTkEntry(
        form_card,
        placeholder_text="Concentración inicial (% o °Brix C1)",
        width=440,
        height=38,
    )
    self.ent_c1.pack(pady=12, padx=25)

    self.ent_c2 = ctk.CTkEntry(
        form_card,
        placeholder_text="Concentración deseada (% o °Brix C2)",
        width=440,
        height=38,
    )
    self.ent_c2.pack(pady=(12, 22), padx=25)

    ctk.CTkButton(
        frame,
        text="Calcular Balance (M2)",
        command=self.calcular_balance,
        height=40,
        corner_radius=10,
        font=ctk.CTkFont(size=14, weight="bold"),
    ).pack(anchor="w", pady=12)

    self.res_card_bal = ctk.CTkFrame(
        frame, fg_color=("#1c1c1c", "#121212"), corner_radius=16
    )
    self.res_card_bal.pack(fill="x", pady=5)

    self.lbl_res_balance = ctk.CTkLabel(
        self.res_card_bal,
        text="Resultado Final: --",
        font=ctk.CTkFont(size=14, weight="bold"),
        text_color="#888888",
    )
    self.lbl_res_balance.pack(pady=16, padx=25, anchor="w")
    return frame

  def calcular_balance(self):
    try:
      m1 = float(self.ent_m1.get())
      c1 = float(self.ent_c1.get())
      c2 = float(self.ent_c2.get())

      if c2 == 0:
        self.res_card_bal.configure(fg_color=("#3d1e1e", "#2b1111"))
        self.lbl_res_balance.configure(
            text="Error: La concentración final no puede ser cero",
            text_color="#E74C3C",
        )
        return

      m2 = (m1 * c1) / c2
      agua_a_agregar = m2 - m1

      self.res_card_bal.configure(fg_color=("#1e3d2f", "#112b20"))
      self.lbl_res_balance.configure(
          text=(
              f"Masa Final (M2): {m2:.2f} un.  |  Ajuste de Agua:"
              f" {abs(agua_a_agregar):.2f}"
          ),
          text_color="#2ECC71",
      )
    except ValueError:
      self.res_card_bal.configure(fg_color=("#3d1e1e", "#2b1111"))
      self.lbl_res_balance.configure(
          text="Error: Ingrese valores numéricos válidos", text_color="#E74C3C"
      )


if __name__ == "__main__":
  app = AppAlimentos()
  app.mainloop()