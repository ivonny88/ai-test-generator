import streamlit as st
from src.generator import generate_test_cases

st.set_page_config(
    page_title="AI Test Generator",
    page_icon="🧪",
    layout="centered"
)

st.title("🧪 AI Test Case Generator")
st.markdown("Genera casos de prueba en **pytest** automáticamente usando IA.")
st.markdown("---")

feature_description = st.text_area(
    label="📝 Describe la funcionalidad a testear:",
    placeholder="Ejemplo: El usuario puede hacer login con email y contraseña. Si las credenciales son incorrectas muestra un mensaje de error. El campo email valida el formato correcto.",
    height=150
)

if st.button("🚀 Generar Tests", type="primary"):
    if not feature_description.strip():
        st.warning("⚠️ Por favor, escribe una descripción antes de generar.")
    else:
        with st.spinner("🤖 Claude está generando tus tests..."):
            try:
                result = generate_test_cases(feature_description)
                
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