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

/* ── Fondo oscuro base ── */
.stApp {
    background: #060a06;
    font-family: 'Rajdhani', sans-serif;
    overflow-x: hidden;
}

/* ── Capas de ambiente ── */
.stars-bg {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 0;
    background:
        radial-gradient(circle at 15% 25%, rgba(0,255,100,0.07) 0%, transparent 40%),
        radial-gradient(circle at 85% 70%, rgba(255,215,0,0.06) 0%, transparent 38%),
        radial-gradient(circle at 50% 95%, rgba(0,180,255,0.04) 0%, transparent 30%),
        radial-gradient(circle at 70% 10%, rgba(255,80,0,0.04)  0%, transparent 28%);
}

/* ── Balones flotantes ── */
.balls-bg {
    position: fixed;
    top: 0; left: 0;
    width: 100vw; height: 100vh;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

@keyframes subirBalon {
    0%   { transform: translateY(105vh) rotate(0deg);    opacity: 0;   }
    8%   { opacity: 0.6; }
    92%  { opacity: 0.6; }
    100% { transform: translateY(-10vh) rotate(900deg);  opacity: 0;   }
}
@keyframes subirBalon2 {
    0%   { transform: translateY(105vh) rotate(0deg);    opacity: 0;   }
    12%  { opacity: 0.5; }
    88%  { opacity: 0.5; }
    100% { transform: translateY(-10vh) rotate(-720deg); opacity: 0;   }
}

.ball {
    position: absolute;
    bottom: -80px;
    animation: subirBalon linear infinite;
    filter: drop-shadow(0 0 10px rgba(0,255,100,0.5));
}

.b1  { left:3%;  font-size:2.6rem; animation-duration:13s; animation-delay:0s;  animation-name:subirBalon;  }
.b2  { left:9%;  font-size:1.7rem; animation-duration:18s; animation-delay:2s;  animation-name:subirBalon2; }
.b3  { left:15%; font-size:3.4rem; animation-duration:11s; animation-delay:5s;  animation-name:subirBalon;  }
.b4  { left:22%; font-size:1.9rem; animation-duration:21s; animation-delay:1s;  animation-name:subirBalon2; }
.b5  { left:29%; font-size:2.9rem; animation-duration:15s; animation-delay:8s;  animation-name:subirBalon;  }
.b6  { left:35%; font-size:1.5rem; animation-duration:10s; animation-delay:3s;  animation-name:subirBalon2; }
.b7  { left:42%; font-size:3.9rem; animation-duration:23s; animation-delay:11s; animation-name:subirBalon;  }
.b8  { left:48%; font-size:2.1rem; animation-duration:14s; animation-delay:4s;  animation-name:subirBalon2; }
.b9  { left:55%; font-size:2.7rem; animation-duration:12s; animation-delay:7s;  animation-name:subirBalon;  }
.b10 { left:62%; font-size:1.8rem; animation-duration:19s; animation-delay:9s;  animation-name:subirBalon2; }
.b11 { left:68%; font-size:3.1rem; animation-duration:16s; animation-delay:13s; animation-name:subirBalon;  }
.b12 { left:74%; font-size:2.0rem; animation-duration:22s; animation-delay:6s;  animation-name:subirBalon2; }
.b13 { left:80%; font-size:3.5rem; animation-duration:13s; animation-delay:15s; animation-name:subirBalon;  }
.b14 { left:86%; font-size:1.6rem; animation-duration:20s; animation-delay:10s; animation-name:subirBalon2; }
.b15 { left:92%; font-size:2.8rem; animation-duration:11s; animation-delay:17s; animation-name:subirBalon;  }
.b16 { left:12%; font-size:2.3rem; animation-duration:25s; animation-delay:19s; animation-name:subirBalon2; }
.b17 { left:57%; font-size:1.9rem; animation-duration:16s; animation-delay:22s; animation-name:subirBalon;  }
.b18 { left:38%; font-size:3.7rem; animation-duration:18s; animation-delay:24s; animation-name:subirBalon2; }

/* ── Nombres de cracks flotando ── */
@keyframes subirNombre {
    0%   { transform: translateY(105vh); opacity: 0;    }
    10%  { opacity: 0.13; }
    90%  { opacity: 0.13; }
    100% { transform: translateY(-8vh);  opacity: 0;    }
}
.nombre-crack {
    position: absolute;
    font-family: 'Orbitron', monospace;
    font-weight: 900;
    color: #ffd700;
    text-transform: uppercase;
    letter-spacing: 5px;
    pointer-events: none;
    animation: subirNombre linear infinite;
    white-space: nowrap;
}
.n1 { font-size:1.0rem; left:2%;  animation-duration:28s; animation-delay:0s;  }
.n2 { font-size:0.8rem; left:18%; animation-duration:33s; animation-delay:6s;  }
.n3 { font-size:1.2rem; left:38%; animation-duration:24s; animation-delay:12s; }
.n4 { font-size:0.9rem; left:58%; animation-duration:30s; animation-delay:4s;  }
.n5 { font-size:1.1rem; left:74%; animation-duration:27s; animation-delay:16s; }
.n6 { font-size:0.75rem;left:88%; animation-duration:35s; animation-delay:9s;  }
.n7 { font-size:1.3rem; left:48%; animation-duration:22s; animation-delay:20s; }
.n8 { font-size:0.85rem;left:8%;  animation-duration:29s; animation-delay:14s; }

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


/* ── Divider ── */
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
        "fase"          : "login",   # login | olvide | reto1 | reto2 | reto3 | exito | bloqueado | salir
        "intentos_login": MAX_INTENTOS,
        "intentos_r1"   : MAX_INTENTOS,
        "intentos_r2"   : MAX_INTENTOS,
        "intentos_r3"   : MAX_INTENTOS,
        "msg"           : "",
        "msg_tipo"      : "",
        "usuario"       : "",
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

def reset_todo():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

def boton_salir():
    """Botón de salir disponible en cualquier fase excepto login/salir."""
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🚪 SALIR DEL SISTEMA", key="btn_salir"):
        st.session_state.fase = "salir"
        st.rerun()

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
#  BALONES FLOTANTES + BANNER
# ══════════════════════════════════════════════════════
st.markdown("""
<div class="stars-bg"></div>
<div class="balls-bg">
  <div class="ball b1">⚽</div><div class="ball b2">🏆</div>
  <div class="ball b3">⚽</div><div class="ball b4">🥅</div>
  <div class="ball b5">⚽</div><div class="ball b6">🏅</div>
  <div class="ball b7">⚽</div><div class="ball b8">🥇</div>
  <div class="ball b9">⚽</div><div class="ball b10">🏆</div>
  <div class="ball b11">⚽</div><div class="ball b12">🎽</div>
  <div class="ball b13">⚽</div><div class="ball b14">🏆</div>
  <div class="ball b15">⚽</div><div class="ball b16">🥅</div>
  <div class="ball b17">⚽</div><div class="ball b18">🏅</div>

  <div class="nombre-crack n1">Messi</div>
  <div class="nombre-crack n2">Ronaldo</div>
  <div class="nombre-crack n3">Mbappé</div>
  <div class="nombre-crack n4">Vinicius</div>
  <div class="nombre-crack n5">Haaland</div>
  <div class="nombre-crack n6">Neymar</div>
  <div class="nombre-crack n7">Pedri</div>
  <div class="nombre-crack n8">Bellingham</div>
</div>
<div class="banner">
  <div class="banner-title">⚽ FITXPLOIT</div>
  <div class="banner-sub">Simulador de Seguridad · Hackea el Sistema</div>
  <div style="margin-top:0.6rem;font-family:'Rajdhani',sans-serif;font-size:0.8rem;color:rgba(255,215,0,0.55);letter-spacing:3px;text-transform:uppercase;">
    🟡 Proyecto Coquito Amarillo · Sistema de Autenticación por Niveles
  </div>
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
      <div class="reto-titulo">🔑 Inicio de Sesión — Autenticación</div>
      <div class="reto-texto">Ingresa tus credenciales para comenzar la misión.</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(dots(st.session_state.intentos_login), unsafe_allow_html=True)
    mostrar_msg()

    with st.form(key="form_login", clear_on_submit=False):
        usuario  = st.text_input("Usuario", placeholder="tu usuario...")
        password = st.text_input("Contraseña", placeholder="••••••••", type="password")
        submitted = st.form_submit_button("⚡ INGRESAR AL SISTEMA")

    if submitted:
        if usuario == USUARIO_CORRECTO and password == PASSWORD_CORRECTA:
            st.session_state.usuario  = usuario
            st.session_state.fase     = "reto1"
            st.session_state.msg      = f"Bienvenido, {usuario}. Iniciando retos..."
            st.session_state.msg_tipo = "ok"
            st.rerun()
        else:
            st.session_state.intentos_login -= 1
            restantes = st.session_state.intentos_login
            if restantes <= 0:
                st.session_state.fase = "bloqueado"
                st.session_state.msg  = "Inicio de sesión"
                st.rerun()
            else:
                st.session_state.msg      = f"Credenciales incorrectas. Intentos restantes: {restantes}"
                st.session_state.msg_tipo = "error"
                st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔓 Olvidé mi contraseña"):
        st.session_state.fase     = "olvide"
        st.session_state.msg      = ""
        st.session_state.msg_tipo = ""
        st.rerun()

# ══════════════════════════════════════════════════════
#  FASE: OLVIDÉ MI CONTRASEÑA
# ══════════════════════════════════════════════════════
elif fase == "olvide":
    st.markdown("""
    <div class="reto-card">
      <div class="reto-titulo">🔓 Recuperación de Contraseña</div>
      <div class="reto-texto">Responde la pregunta de seguridad para restablecer tu acceso.</div>
    </div>
    """, unsafe_allow_html=True)

    mostrar_msg()

    with st.form(key="form_olvide", clear_on_submit=False):
        usr      = st.text_input("Usuario", placeholder="tu usuario...")
        respuesta = st.text_input("¿Nombre de tu equipo favorito?", placeholder="Escribe tu respuesta...")
        nueva_pw  = st.text_input("Nueva contraseña", placeholder="mínimo 4 caracteres", type="password")
        submitted = st.form_submit_button("🔄 RESTABLECER CONTRASEÑA")

    if submitted:
        if usr != USUARIO_CORRECTO:
            st.session_state.msg      = "Usuario no encontrado en el sistema."
            st.session_state.msg_tipo = "error"
            st.rerun()
        elif respuesta.strip().lower() != "real madrid":
            st.session_state.msg      = "Respuesta de seguridad incorrecta."
            st.session_state.msg_tipo = "error"
            st.rerun()
        elif len(nueva_pw.strip()) < 4:
            st.session_state.msg      = "La contraseña debe tener mínimo 4 caracteres."
            st.session_state.msg_tipo = "error"
            st.rerun()
        else:
            # En producción real aquí se actualizaría la BD
            st.session_state.msg      = "✅ Contraseña restablecida. Vuelve al inicio de sesión."
            st.session_state.msg_tipo = "ok"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("← Volver al inicio de sesión"):
        st.session_state.fase     = "login"
        st.session_state.msg      = ""
        st.session_state.msg_tipo = ""
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

    st.markdown(dots(st.session_state.intentos_r1), unsafe_allow_html=True)
    mostrar_msg()

    with st.form(key="form_r1", clear_on_submit=False):
        resp      = st.text_input("🔢 Tu respuesta (número)", placeholder="Escribe el número...")
        submitted = st.form_submit_button("⚡ ENVIAR RESPUESTA")

    if submitted:
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

    boton_salir()

# ══════════════════════════════════════════════════════
#  FASE: RETO 2 — CIFRADO CÉSAR
# ══════════════════════════════════════════════════════
elif fase == "reto2":

    # ── Título del reto ──────────────────────────────────
    st.markdown('<div class="reto-card"><div class="reto-titulo">🎯 Reto 2 de 3 — Descifra el Código</div></div>', unsafe_allow_html=True)

    # ── Explicación con componentes nativos ──────────────
    st.markdown("##### 🕵️ El espía envió un mensaje secreto")
    st.markdown(
        "Usó el **Cifrado César**: cada letra del abecedario fue "
        "**movida 3 posiciones hacia adelante**. "
        "Para descifrarla, debes **retroceder 3 posiciones**."
    )

    st.markdown("---")
    st.markdown("##### 🔡 ¿Cómo descifrar letra por letra?")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div style="background:rgba(0,255,100,0.07);border:1px solid rgba(0,255,100,0.3);
                        border-radius:6px;padding:0.8rem;text-align:center;">
              <div style="color:#888;font-size:0.75rem;letter-spacing:2px">CIFRADA</div>
              <div style="color:#ffd700;font-size:1.8rem;font-family:'Orbitron',monospace;font-weight:900">F</div>
              <div style="color:#555;font-size:0.8rem">↓ retrocede 3</div>
              <div style="color:#00ff64;font-size:1.8rem;font-family:'Orbitron',monospace;font-weight:900">C</div>
            </div>
            """, unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <div style="background:rgba(0,255,100,0.07);border:1px solid rgba(0,255,100,0.3);
                        border-radius:6px;padding:0.8rem;text-align:center;">
              <div style="color:#888;font-size:0.75rem;letter-spacing:2px">CIFRADA</div>
              <div style="color:#ffd700;font-size:1.8rem;font-family:'Orbitron',monospace;font-weight:900">U</div>
              <div style="color:#555;font-size:0.8rem">↓ retrocede 3</div>
              <div style="color:#00ff64;font-size:1.8rem;font-family:'Orbitron',monospace;font-weight:900">R</div>
            </div>
            """, unsafe_allow_html=True)
    with col3:
        st.markdown(
            """
            <div style="background:rgba(0,255,100,0.07);border:1px solid rgba(0,255,100,0.3);
                        border-radius:6px;padding:0.8rem;text-align:center;">
              <div style="color:#888;font-size:0.75rem;letter-spacing:2px">CIFRADA</div>
              <div style="color:#ffd700;font-size:1.8rem;font-family:'Orbitron',monospace;font-weight:900">D</div>
              <div style="color:#555;font-size:0.8rem">↓ retrocede 3</div>
              <div style="color:#00ff64;font-size:1.8rem;font-family:'Orbitron',monospace;font-weight:900">A</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("##### 📡 Mensaje completo interceptado:")
    st.markdown(
        '<div class="reto-codigo">F &nbsp;&nbsp; U &nbsp;&nbsp; D &nbsp;&nbsp; F &nbsp;&nbsp; N</div>',
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        "> 💬 **Referencia:** `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`  \n"
        "> Ejemplo: la letra **F** retrocede 3 → **E → D → C**"
    )
    st.markdown("**❓ ¿Cuál es la palabra original de 5 letras?**")

    st.markdown(dots(st.session_state.intentos_r2), unsafe_allow_html=True)
    mostrar_msg()

    with st.form(key="form_r2", clear_on_submit=False):
        resp      = st.text_input("🔤 Tu respuesta (palabra)", placeholder="Escribe la palabra...")
        submitted = st.form_submit_button("⚡ ENVIAR RESPUESTA")

    if submitted:
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

    boton_salir()

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

    with st.form(key="form_r3", clear_on_submit=False):
        resp      = st.text_input("🔢 Tu respuesta (número decimal)", placeholder="Escribe el número...")
        submitted = st.form_submit_button("⚡ ENVIAR RESPUESTA FINAL")

    if submitted:
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

    boton_salir()

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
        🟡 Proyecto Coquito Amarillo — Misión cumplida.
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 AUTENTICARSE NUEVAMENTE"):
            reset_todo()
            st.rerun()
    with col2:
        if st.button("🚪 SALIR DEL SISTEMA"):
            st.session_state.fase = "salir"
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
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔐 AUTENTICARSE NUEVAMENTE"):
            reset_todo()
            st.rerun()
    with col2:
        if st.button("🚪 SALIR DEL SISTEMA"):
            st.session_state.fase = "salir"
            st.rerun()

# ══════════════════════════════════════════════════════
#  FASE: SALIR
# ══════════════════════════════════════════════════════
elif fase == "salir":
    st.markdown("""
    <div class="msg-exito" style="border-color:#ffd700;box-shadow:0 0 30px rgba(255,215,0,0.15);">
      <div class="msg-exito-titulo" style="color:#ffd700;text-shadow:0 0 20px rgba(255,215,0,0.7);">
        🟡 SESIÓN CERRADA
      </div>
      <div class="msg-exito-sub">
        Has salido del sistema FitXploit correctamente.<br>
        Proyecto Coquito Amarillo · Hasta la próxima. ⚽
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔐 VOLVER A AUTENTICARSE"):
        reset_todo()
        st.rerun()
