import streamlit as st
from src.generator import generate_test_cases
from datetime import date

st.set_page_config(
    page_title="AI Test Generator",
    page_icon="🧪",
    layout="centered"
)

# --- PRO ACCESS CHECK ---
PRO_KEY = "FATIMAQA-PRO-2024"

def is_pro_user():
    return st.session_state.get("pro_unlocked", False)

def get_daily_count():
    today = str(date.today())
    if st.session_state.get("usage_date") != today:
        st.session_state["usage_date"] = today
        st.session_state["daily_count"] = 0
    return st.session_state.get("daily_count", 0)

def increment_daily_count():
    st.session_state["daily_count"] = get_daily_count() + 1

# --- HEADER ---
st.title("🧪 AI Test Case Generator")
st.markdown("Genera casos de prueba en **pytest** automáticamente usando IA.")
st.markdown("---")

# --- PRO UNLOCK SECTION ---
with st.expander("🔑 ¿Tienes una clave Pro? Actívala aquí"):
    pro_input = st.text_input("Introduce tu clave Pro:", type="password")
    if st.button("Activar Pro"):
        if pro_input == PRO_KEY:
            st.session_state["pro_unlocked"] = True
            st.success("✅ ¡Modo Pro activado! Generaciones ilimitadas.")
        else:
            st.error("❌ Clave incorrecta.")

# --- PRO BADGE ---
if is_pro_user():
    st.markdown("🌟 **Modo Pro activo** — Generaciones ilimitadas")
else:
    daily_count = get_daily_count()
    remaining = max(0, 3 - daily_count)
    st.markdown(f"🆓 **Versión gratuita** — Te quedan **{remaining}/3** generaciones hoy")
    if remaining == 0:
        st.warning("⚠️ Has alcanzado el límite diario gratuito. Obtén acceso Pro para generaciones ilimitadas.")
        st.markdown(
            """
            <div style='text-align: center; padding: 10px;'>
                <a href='https://fatimaflare207.gumroad.com/l/iliohe' target='_blank' 
                   style='background: #6B21A8; color: white; padding: 12px 24px; 
                   border-radius: 8px; text-decoration: none; font-weight: bold;'>
                    🌟 Obtener acceso Pro — 9€
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")

# --- MAIN FORM ---
feature_description = st.text_area(
    label="📝 Describe la funcionalidad a testear:",
    placeholder="Ejemplo: El usuario puede hacer login con email y contraseña. Si las credenciales son incorrectas muestra un mensaje de error. El campo email valida el formato correcto.",
    height=150
)

if st.button("🚀 Generar Tests", type="primary"):
    if not feature_description.strip():
        st.warning("⚠️ Por favor, escribe una descripción antes de generar.")
    elif not is_pro_user() and get_daily_count() >= 3:
        st.error("❌ Límite diario alcanzado. Obtén acceso Pro para continuar.")
    else:
        with st.spinner("🤖 Generando tus tests..."):
            try:
                result = generate_test_cases(feature_description)

                if not is_pro_user():
                    increment_daily_count()

                st.success("✅ Tests generados correctamente")
                st.markdown("### 📋 Casos de prueba generados:")
                st.code(result, language="python")

                st.download_button(
                    label="⬇️ Descargar tests.py",
                    data=result,
                    file_name="generated_tests.py",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error al generar tests: {str(e)}")

st.markdown("---")
st.markdown(
    "Desarrollado por **Fátima Ocaña** · QA Engineer · "
    "[GitHub](https://github.com/ivonny88/ai-test-generator)"
)

st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; padding: 20px;'>
        <p style='color: #666; font-size: 14px;'>¿Te ha sido útil esta herramienta?</p>
        <a href='https://buymeacoffee.com/fatimaqa' target='_blank'>
            <img src='https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png' 
                 alt='Buy Me A Coffee' 
                 style='height: 50px; width: 180px;'>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)