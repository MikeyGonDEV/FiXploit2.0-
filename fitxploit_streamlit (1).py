import streamlit as st
import time

# ══════════════════════════════════════════════════════
#  CONFIGURACIÓN DE PÁGINA
# ══════════════════════════════════════════════════════
st.set_page_config(
    page_title="FitXploit 🔐⚽",
    page_icon="⚽",
    layout="centered"
)

# ══════════════════════════════════════════════════════
#  CSS — DISEÑO GAMER / FUTBOLÍSTICO
# ══════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Rajdhani:wght@400;600;700&display=swap');

/* ── Fondo campo de fútbol ── */
.stApp {
    background-color: #1a4a1a;
    background-image:
        /* Círculo central */
        radial-gradient(circle at 50% 50%, transparent 8%, rgba(255,255,255,0.06) 8%, rgba(255,255,255,0.06) 9%, transparent 9%),
        /* Punto central */
        radial-gradient(circle at 50% 50%, rgba(255,255,255,0.15) 0.4%, transparent 0.4%),
        /* Línea central horizontal */
        linear-gradient(to bottom, transparent 49.6%, rgba(255,255,255,0.07) 49.6%, rgba(255,255,255,0.07) 50.4%, transparent 50.4%),
        /* Franjas verticales del césped */
        repeating-linear-gradient(
            90deg,
            rgba(0,0,0,0.06) 0px,
            rgba(0,0,0,0.06) 80px,
            transparent 80px,
            transparent 160px
        ),
        /* Degradado profundidad campo */
        radial-gradient(ellipse at 50% 0%,   rgba(0,80,0,0.6) 0%, transparent 60%),
        radial-gradient(ellipse at 50% 100%, rgba(0,60,0,0.6) 0%, transparent 60%),
        radial-gradient(ellipse at 50% 50%,  rgba(20,100,20,0.3) 0%, transparent 80%);
    font-family: 'Rajdhani', sans-serif;
}

/* ── Ocultar elementos de Streamlit ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem; padding-bottom: 2rem; max-width: 720px; }

/* ── Banner principal ── */
.banner {
    background: linear-gradient(135deg, #0d1f0d 0%, #0a1a0a 50%, #111108 100%);
    border: 1px solid #00ff64;
    border-radius: 4px;
    padding: 2rem 1.5rem 1.5rem;
    text-align: center;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
    box-shadow: 0 0 40px rgba(0,255,100,0.15), inset 0 0 60px rgba(0,0,0,0.5);
}
.banner::before {
    content: '';
    position: absolute;
    top: -2px; left: -2px; right: -2px; bottom: -2px;
    background: linear-gradient(45deg, #00ff64, #ffd700, #00ff64);
    z-index: -1;
    border-radius: 4px;
    opacity: 0.3;
}
.banner-title {
    font-family: 'Orbitron', monospace;
    font-size: 2.2rem;
    font-weight: 900;
    color: #00ff64;
    text-shadow: 0 0 20px rgba(0,255,100,0.8), 0 0 40px rgba(0,255,100,0.4);
    letter-spacing: 4px;
    margin: 0;
    line-height: 1.1;
}
.banner-sub {
    font-family: 'Rajdhani', sans-serif;
    color: #ffd700;
    font-size: 1rem;
    letter-spacing: 3px;
    margin-top: 0.4rem;
    text-transform: uppercase;
    opacity: 0.9;
}

/* ── Tarjetas de reto ── */
.reto-card {
    background: linear-gradient(135deg, #0d1a0d, #0a120a);
    border: 1px solid rgba(0,255,100,0.3);
    border-left: 3px solid #00ff64;
    border-radius: 4px;
    padding: 1.4rem 1.5rem;
    margin-bottom: 1rem;
    box-shadow: 0 4px 20px rgba(0,0,0,0.4);
}
.reto-titulo {
    font-family: 'Orbitron', monospace;
    color: #00ff64;
    font-size: 0.85rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 0.8rem;
}
.reto-texto {
    font-family: 'Rajdhani', sans-serif;
    color: #c8e6c8;
    font-size: 1.05rem;
    line-height: 1.6;
}
.reto-codigo {
    font-family: 'Orbitron', monospace;
    background: rgba(0,255,100,0.08);
    border: 1px solid rgba(0,255,100,0.25);
    color: #ffd700;
    padding: 0.6rem 1.2rem;
    border-radius: 3px;
    font-size: 1.3rem;
    letter-spacing: 6px;
    display: inline-block;
    margin: 0.8rem 0;
    text-shadow: 0 0 10px rgba(255,215,0,0.5);
}

/* ── Intentos ── */
.intentos-bar {
    display: flex;
    gap: 6px;
    margin: 0.6rem 0 1rem;
    align-items: center;
}
.intento-dot {
    width: 14px; height: 14px;
    border-radius: 50%;
    background: #00ff64;
    box-shadow: 0 0 6px rgba(0,255,100,0.8);
}
.intento-dot.usado {
    background: #1a1a1a;
    border: 1px solid #333;
    box-shadow: none;
}
.intentos-label {
    font-family: 'Rajdhani', sans-serif;
    color: #888;
    font-size: 0.85rem;
    letter-spacing: 1px;
    margin-left: 4px;
}

/* ── Pista ── */
.pista-box {
    background: rgba(255,215,0,0.07);
    border: 1px solid rgba(255,215,0,0.3);
    border-radius: 3px;
    padding: 0.6rem 1rem;
    margin: 0.6rem 0;
    color: #ffd700;
    font-family: 'Rajdhani', sans-serif;
    font-size: 0.95rem;
}

/* ── Mensajes ── */
.msg-exito {
    background: linear-gradient(135deg, #0d2d0d, #0a200a);
    border: 1px solid #00ff64;
    border-radius: 4px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 30px rgba(0,255,100,0.2);
}
.msg-exito-titulo {
    font-family: 'Orbitron', monospace;
    color: #00ff64;
    font-size: 1.8rem;
    font-weight: 900;
    text-shadow: 0 0 20px rgba(0,255,100,0.8);
    margin-bottom: 0.5rem;
}
.msg-exito-sub {
    font-family: 'Rajdhani', sans-serif;
    color: #ffd700;
    font-size: 1.1rem;
    letter-spacing: 2px;
}

.msg-bloqueo {
    background: linear-gradient(135deg, #1a0505, #120303);
    border: 1px solid #ff3333;
    border-radius: 4px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 0 30px rgba(255,50,50,0.2);
}
.msg-bloqueo-titulo {
    font-family: 'Orbitron', monospace;
    color: #ff3333;
    font-size: 1.6rem;
    font-weight: 900;
    text-shadow: 0 0 20px rgba(255,50,50,0.6);
    margin-bottom: 0.5rem;
}
.msg-bloqueo-sub {
    font-family: 'Rajdhani', sans-serif;
    color: #ff9999;
    font-size: 1rem;
    letter-spacing: 1px;
}

/* ── Progreso de retos ── */
.progreso {
    display: flex;
    justify-content: center;
    gap: 8px;
    margin: 1rem 0 1.5rem;
    align-items: center;
}
.paso {
    font-family: 'Orbitron', monospace;
    font-size: 0.65rem;
    padding: 4px 12px;
    border-radius: 2px;
    letter-spacing: 1px;
    text-transform: uppercase;
}
.paso-hecho   { background: rgba(0,255,100,0.15); color: #00ff64; border: 1px solid #00ff64; }
.paso-actual  { background: rgba(255,215,0,0.15);  color: #ffd700; border: 1px solid #ffd700; }
.paso-pend    { background: rgba(255,255,255,0.03); color: #444;   border: 1px solid #222; }
.flecha       { color: #333; font-size: 0.7rem; }

/* ── Inputs ── */
.stTextInput > div > div > input {
    background: #0d1a0d !important;
    border: 1px solid rgba(0,255,100,0.4) !important;
    border-radius: 3px !important;
    color: #00ff64 !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 1rem !important;
    letter-spacing: 2px !important;
    padding: 0.6rem 1rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: #00ff64 !important;
    box-shadow: 0 0 12px rgba(0,255,100,0.3) !important;
}
.stTextInput > label {
    color: #888 !important;
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 0.85rem !important;
    letter-spacing: 2px !important;
    text-transform: uppercase !important;
}

/* ── Botón principal ── */
.stButton > button {
    background: linear-gradient(135deg, #003d1a, #005522) !important;
    color: #00ff64 !important;
    border: 1px solid #00ff64 !important;
    border-radius: 3px !important;
    font-family: 'Orbitron', monospace !important;
    font-size: 0.85rem !important;
    font-weight: 700 !important;
    letter-spacing: 3px !important;
    padding: 0.7rem 2rem !important;
    width: 100% !important;
    text-transform: uppercase !important;
    transition: all 0.2s !important;
    box-shadow: 0 0 15px rgba(0,255,100,0.1) !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, #005522, #007733) !important;
    box-shadow: 0 0 25px rgba(0,255,100,0.3) !important;
    transform: translateY(-1px) !important;
}

/* ── Divider ── */
hr { border-color: rgba(0,255,100,0.1) !important; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  DATOS DEL SISTEMA
# ══════════════════════════════════════════════════════
USUARIO_CORRECTO  = "admin1"
PASSWORD_CORRECTA = "fit99123"
MAX_INTENTOS      = 3

# ── Estado de sesión ──────────────────────────────────
def init_state():
    defaults = {
        "fase"          : "login",   # login | reto1 | reto2 | reto3 | exito | bloqueado
        "intentos_login": MAX_INTENTOS,
        "intentos_r1"   : MAX_INTENTOS,
        "intentos_r2"   : MAX_INTENTOS,
        "intentos_r3"   : MAX_INTENTOS,
        "msg"           : "",
        "msg_tipo"      : "",   # ok | error | pista
        "usuario"       : "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_state()

# ══════════════════════════════════════════════════════
#  HELPERS
# ══════════════════════════════════════════════════════
def mostrar_msg():
    m = st.session_state.msg
    t = st.session_state.msg_tipo
    if not m:
        return
    if t == "ok":
        st.markdown(f'<div style="color:#00ff64;font-family:Rajdhani,sans-serif;font-size:1rem;padding:0.5rem 0">✅ {m}</div>', unsafe_allow_html=True)
    elif t == "error":
        st.markdown(f'<div style="color:#ff4444;font-family:Rajdhani,sans-serif;font-size:1rem;padding:0.5rem 0">❌ {m}</div>', unsafe_allow_html=True)
    elif t == "pista":
        st.markdown(f'<div class="pista-box">💡 {m}</div>', unsafe_allow_html=True)

def dots(restantes):
    html = '<div class="intentos-bar">'
    for i in range(MAX_INTENTOS):
        cls = "intento-dot" if i < restantes else "intento-dot usado"
        html += f'<div class="{cls}"></div>'
    html += f'<span class="intentos-label">intentos restantes</span></div>'
    return html

def barra_progreso():
    fase = st.session_state.fase
    pasos = [
        ("LOGIN",  "login"),
        ("RETO 1", "reto1"),
        ("RETO 2", "reto2"),
        ("RETO 3", "reto3"),
    ]
    orden = ["login","reto1","reto2","reto3","exito","bloqueado"]
    idx_actual = orden.index(fase) if fase in orden else 0

    html = '<div class="progreso">'
    for i, (label, key) in enumerate(pasos):
        idx = orden.index(key)
        if idx < idx_actual:
            cls = "paso paso-hecho"
        elif idx == idx_actual:
            cls = "paso paso-actual"
        else:
            cls = "paso paso-pend"
        html += f'<span class="{cls}">{label}</span>'
        if i < len(pasos) - 1:
            html += '<span class="flecha">▶</span>'
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
#  BANNER
# ══════════════════════════════════════════════════════
st.markdown("""
<div class="banner">
  <div class="banner-title">⚽ FITXPLOIT</div>
  <div class="banner-sub">Simulador de Seguridad · Hackea el Sistema</div>
</div>
""", unsafe_allow_html=True)

barra_progreso()

fase = st.session_state.fase

# ══════════════════════════════════════════════════════
#  FASE: LOGIN
# ══════════════════════════════════════════════════════
if fase == "login":
    st.markdown("""
    <div class="reto-card">
      <div class="reto-titulo">🔑 Inicio de Sesión</div>
      <div class="reto-texto">Ingresa tus credenciales para comenzar la misión.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(dots(st.session_state.intentos_login), unsafe_allow_html=True)
    mostrar_msg()

    usuario  = st.text_input("Usuario", placeholder="tu usuario...", key="inp_usuario")
    password = st.text_input("Contraseña", placeholder="••••••••", type="password", key="inp_password")

    if st.button("⚡ INGRESAR AL SISTEMA"):
        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTA:
            st.session_state.usuario   = usuario
            st.session_state.fase      = "reto1"
            st.session_state.msg       = f"Bienvenido, {usuario}. Iniciando retos..."
            st.session_state.msg_tipo  = "ok"
            st.rerun()
        else:
            st.session_state.intentos_login -= 1
            restantes = st.session_state.intentos_login
            if restantes <= 0:
                st.session_state.fase     = "bloqueado"
                st.session_state.msg      = "Inicio de sesión"
                st.rerun()
            else:
                st.session_state.msg      = f"Credenciales incorrectas. Intentos restantes: {restantes}"
                st.session_state.msg_tipo = "error"
                st.rerun()

# ══════════════════════════════════════════════════════
#  FASE: RETO 1 — LÓGICA Y MATEMÁTICAS
# ══════════════════════════════════════════════════════
elif fase == "reto1":
    st.markdown("""
    <div class="reto-card">
      <div class="reto-titulo">⚽ Reto 1 de 3 — Lógica y Matemáticas</div>
      <div class="reto-texto">
        Un delantero marcó <b style="color:#ffd700">4 goles por partido</b> durante <b style="color:#ffd700">5 partidos</b>.<br>
        El portero anuló la mitad <b style="color:#ffd700">(÷ 2)</b>.<br>
        Luego el equipo sumó <b style="color:#ffd700">3 goles más</b>.<br><br>
        ❓ <b style="color:#00ff64">¿Cuántos goles quedaron en la tabla final?</b><br>
        <span style="opacity:0.6;font-size:0.9rem">(4 × 5) ÷ 2 + 3 = ?</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    restantes = st.session_state.intentos_r1
    st.markdown(dots(restantes), unsafe_allow_html=True)

    if restantes == 2:
        st.session_state.msg      = "El resultado es mayor que 10."
        st.session_state.msg_tipo = "pista"
    elif restantes == 1:
        st.session_state.msg      = "Está entre 12 y 14. ¡Último intento!"
        st.session_state.msg_tipo = "pista"

    mostrar_msg()

    resp = st.text_input("🔢 Tu respuesta (número)", placeholder="Escribe el número...", key="inp_r1")

    if st.button("⚡ ENVIAR RESPUESTA"):
        try:
            numero = int(resp.strip())
        except ValueError:
            st.session_state.msg      = "Solo números enteros, por favor."
            st.session_state.msg_tipo = "error"
            st.rerun()
        else:
            if numero == 13:
                st.session_state.fase     = "reto2"
                st.session_state.msg      = "¡GOL! Reto 1 superado."
                st.session_state.msg_tipo = "ok"
                st.rerun()
            else:
                st.session_state.intentos_r1 -= 1
                if st.session_state.intentos_r1 <= 0:
                    st.session_state.fase = "bloqueado"
                    st.session_state.msg  = "Reto 1 — Lógica y Matemáticas"
                    st.rerun()
                else:
                    st.session_state.msg      = f"Incorrecto. Intentos restantes: {st.session_state.intentos_r1}"
                    st.session_state.msg_tipo = "error"
                    st.rerun()

# ══════════════════════════════════════════════════════
#  FASE: RETO 2 — CIFRADO CÉSAR
# ══════════════════════════════════════════════════════
elif fase == "reto2":
    st.markdown("""
    <div class="reto-card">
      <div class="reto-titulo">🎯 Reto 2 de 3 — Descifra el Código</div>
      <div class="reto-texto">
        Interceptamos una comunicación cifrada con<br>
        <b style="color:#ffd700">Cifrado César desplazamiento +3</b>.<br>
        Cada letra fue movida 3 posiciones hacia adelante.<br>
        Ejemplo: <b style="color:#ffd700">A→D &nbsp; B→E &nbsp; C→F</b><br><br>
        Mensaje cifrado:
      </div>
      <div class="reto-codigo">F U D F N</div><br>
      <div class="reto-texto">❓ <b style="color:#00ff64">¿Cuál es la palabra original?</b></div>
    </div>
    """, unsafe_allow_html=True)

    restantes = st.session_state.intentos_r2
    st.markdown(dots(restantes), unsafe_allow_html=True)

    if restantes == 2:
        st.session_state.msg      = 'La palabra empieza con la letra "C".'
        st.session_state.msg_tipo = "pista"
    elif restantes == 1:
        st.session_state.msg      = "Tiene 5 letras. ¡Último intento!"
        st.session_state.msg_tipo = "pista"

    mostrar_msg()

    resp = st.text_input("🔤 Tu respuesta (palabra)", placeholder="Escribe la palabra...", key="inp_r2")

    if st.button("⚡ ENVIAR RESPUESTA"):
        if resp.strip().upper() == "CRACK":
            st.session_state.fase     = "reto3"
            st.session_state.msg      = "¡Interceptado! Reto 2 superado."
            st.session_state.msg_tipo = "ok"
            st.rerun()
        else:
            st.session_state.intentos_r2 -= 1
            if st.session_state.intentos_r2 <= 0:
                st.session_state.fase = "bloqueado"
                st.session_state.msg  = "Reto 2 — Cifrado César"
                st.rerun()
            else:
                st.session_state.msg      = f"Incorrecto. Intentos restantes: {st.session_state.intentos_r2}"
                st.session_state.msg_tipo = "error"
                st.rerun()

# ══════════════════════════════════════════════════════
#  FASE: RETO 3 — BINARIO
# ══════════════════════════════════════════════════════
elif fase == "reto3":
    st.markdown("""
    <div class="reto-card">
      <div class="reto-titulo">🧩 Reto 3 de 3 — Puzzle Binario (Final)</div>
      <div class="reto-texto">
        La base de datos del estadio guarda el número de camiseta<br>
        del infiltrado en <b style="color:#ffd700">código BINARIO</b>.<br><br>
        Código:
      </div>
      <div class="reto-codigo">0 1 0 0 1 0 1 0</div><br>
      <div class="reto-texto">
        Posiciones (derecha → izquierda):<br>
        <span style="color:#ffd700;font-family:'Orbitron',monospace;font-size:0.85rem">
          128 · 64 · 32 · 16 · 8 · 4 · 2 · 1
        </span><br><br>
        ❓ <b style="color:#00ff64">¿A qué número decimal corresponde?</b>
      </div>
    </div>
    """, unsafe_allow_html=True)

    restantes = st.session_state.intentos_r3
    st.markdown(dots(restantes), unsafe_allow_html=True)
    mostrar_msg()

    resp = st.text_input("🔢 Tu respuesta (número decimal)", placeholder="Escribe el número...", key="inp_r3")

    if st.button("⚡ ENVIAR RESPUESTA FINAL"):
        try:
            numero = int(resp.strip())
        except ValueError:
            st.session_state.msg      = "Solo números enteros, por favor."
            st.session_state.msg_tipo = "error"
            st.rerun()
        else:
            if numero == 74:
                st.session_state.fase     = "exito"
                st.session_state.msg      = ""
                st.rerun()
            else:
                st.session_state.intentos_r3 -= 1
                if st.session_state.intentos_r3 <= 0:
                    st.session_state.fase = "bloqueado"
                    st.session_state.msg  = "Reto 3 — Puzzle Binario"
                    st.rerun()
                else:
                    st.session_state.msg      = f"Incorrecto. Intentos restantes: {st.session_state.intentos_r3}"
                    st.session_state.msg_tipo = "error"
                    st.rerun()

# ══════════════════════════════════════════════════════
#  FASE: ÉXITO
# ══════════════════════════════════════════════════════
elif fase == "exito":
    st.markdown("""
    <div class="msg-exito">
      <div class="msg-exito-titulo">✅ ACCESO CONCEDIDO</div>
      <div class="msg-exito-sub">🏆 Superaste los 3 retos · Eres el mejor crack ⚽</div>
      <br>
      <div style="font-family:'Rajdhani',sans-serif;color:#c8e6c8;font-size:1rem">
        Bienvenido al sistema FitXploit.<br>
        El estadio es tuyo. Misión cumplida.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 JUGAR DE NUEVO"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

# ══════════════════════════════════════════════════════
#  FASE: BLOQUEADO
# ══════════════════════════════════════════════════════
elif fase == "bloqueado":
    donde = st.session_state.msg
    st.markdown(f"""
    <div class="msg-bloqueo">
      <div class="msg-bloqueo-titulo">🔒 SISTEMA BLOQUEADO</div>
      <div class="msg-bloqueo-sub">
        Fallaste en: <b>{donde}</b><br>
        Demasiados intentos incorrectos.<br>
        El acceso ha sido denegado permanentemente.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 INTENTAR DE NUEVO"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
