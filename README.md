🏧 Simulador de Cajero Automático con Streamlit
Un sencillo pero funcional simulador de un cajero automático (ATM) construido con Python y presentado como una aplicación web interactiva usando la librería Streamlit.

## ✨ Características

Autenticación Segura: Acceso a la cuenta mediante un PIN.

Consulta de Saldo: Visualiza tu saldo actual en cualquier momento.

Retiro de Efectivo: Retira fondos de tu cuenta con validación para evitar sobregiros.

Depósito de Efectivo: Añade fondos a tu cuenta de forma segura.

Interfaz Web Interactiva: Construido con Streamlit para una experiencia de usuario amigable y moderna.

🛠️ Tecnologías Utilizadas
Python 3: El lenguaje de programación principal.

Streamlit: El framework utilizado para construir la interfaz de la aplicación web.

🚀 Instalación y Puesta en Marcha
Sigue estos pasos para ejecutar el proyecto en tu máquina local.

1. Clona el repositorio
Abre tu terminal y clona este repositorio usando Git. Reemplaza tu-usuario y tu-repositorio con tu nombre de usuario y el nombre de tu repositorio.

Bash

git clone https://github.com/tu-usuario/tu-repositorio.git
cd tu-repositorio
2. Crea un Entorno Virtual
Es una buena práctica crear un entorno virtual para aislar las dependencias del proyecto.

Bash

python3 -m venv .venv
3. Activa el Entorno Virtual
En Linux o macOS:

Bash

source .venv/bin/activate
En Windows:

Bash

.venv\Scripts\activate
4. Instala las dependencias
Para que otros puedan instalar las librerías fácilmente, es una excelente práctica crear un archivo requirements.txt.

Si no tienes el archivo requirements.txt, créalo con este comando:

Bash

pip freeze > requirements.txt
(Esto guardará Streamlit y sus otras dependencias en un archivo de texto).

Instala las dependencias desde el archivo:

Bash

pip install -r requirements.txt
▶️ Cómo Ejecutar la Aplicación
Una vez que el entorno esté activado y las dependencias instaladas, ejecuta la aplicación con el siguiente comando:

Bash

streamlit run cajero_web.py
Tu navegador web se abrirá automáticamente en la dirección http://localhost:8501, donde podrás interactuar con el cajero automático.

📄 Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
