# 🧪 AI Test Case Generator

Herramienta web que genera automáticamente casos de prueba en **pytest** a partir de descripciones de funcionalidades en lenguaje natural, usando **IA** (Groq + LLaMA 3.3).

---

## 🎯 ¿Qué problema resuelve?

Escribir casos de prueba manualmente lleva tiempo. Esta herramienta permite a cualquier QA Engineer describir una funcionalidad en texto plano y obtener en segundos un conjunto completo de tests en pytest listos para usar, cubriendo:

- ✅ Smoke tests
- ✅ Regression tests  
- ✅ Negative cases y edge cases

---

## 🚀 Demo

Escribe esto en la app:

> "El usuario puede hacer login con email y contraseña. Si las credenciales son incorrectas muestra un mensaje de error. El campo email valida el formato correcto."

Y la IA genera automáticamente el código pytest completo.

---

## 🏗️ Tecnologías

![Python](https://img.shields.io/badge/Python-3.12+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-latest-red)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.3-orange)
![pytest](https://img.shields.io/badge/pytest-latest-green)

---

## ⚙️ Estructura
```
ai-test-generator/
│
├── src/
│   ├── generator.py      # Lógica con la API de Groq
│   └── prompts.py        # Prompts para generación de tests
│
├── tests/
│   └── test_generator.py # Tests del generador
│
├── app.py                # Interfaz web con Streamlit
├── requirements.txt
└── .env.example          # Ejemplo de variables de entorno
```

---

## 🚀 Cómo ejecutar

### 1. Clonar el repositorio
```bash
git clone https://github.com/ivonny88/ai-test-generator.git
cd ai-test-generator
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar API key

Crea un archivo `.env` en la raíz:
```
GROQ_API_KEY=tu-api-key-aquí
```

Obtén tu API key gratuita en [console.groq.com](https://console.groq.com)

### 4. Lanzar la app
```bash
streamlit run app.py
```

---

## 💡 Casos de uso

- Generar tests rápidamente para nuevas funcionalidades
- Aprender a escribir buenos casos de prueba
- Acelerar el proceso de QA en proyectos ágiles

---

## 👩‍💻 Autora

**Fátima Ocaña** — QA Engineer | Manual & Automation Testing  
[LinkedIn](https://www.linkedin.com/in/fatimaqa/) · [GitHub](https://github.com/ivonny88)