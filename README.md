# 🚀 API de Gestión de Actividades

Una API REST simple construida con Flask para gestionar actividades/tareas.

## 📋 Características

- ✅ CRUD completo para actividades
- 📊 Endpoint de estadísticas
- 🧪 Tests automatizados
- 🐳 Listo para deployment en Render
- 📝 Documentación completa

## 🛠️ Instalación Local

1. Clona el repositorio:
\`\`\`bash
git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo
\`\`\`

2. Instala las dependencias:
\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. Ejecuta la aplicación:
\`\`\`bash
python app_mejorada.py
\`\`\`

## 🌐 Endpoints

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/` | Información de la API |
| GET | `/activities` | Obtener todas las actividades |
| POST | `/activities` | Crear nueva actividad |
| GET | `/activities/<id>` | Obtener actividad específica |
| PUT | `/activities/<id>` | Actualizar actividad |
| DELETE | `/activities/<id>` | Eliminar actividad |
| GET | `/stats` | Obtener estadísticas |

## 🧪 Ejecutar Tests

\`\`\`bash
pytest test_mejorado.py -v
\`\`\`

## 🚀 Deployment en Render

1. Sube tu código a GitHub
2. Conecta tu repositorio en Render
3. Configura el servicio web
4. ¡Listo!

## 📱 Cliente de Ejemplo

Usa `client_mejorado.py` para interactuar con la API:

```python
from client_mejorado import ActivityClient

client = ActivityClient("https://tu-app.onrender.com")
activities = client.get_activities()
print(activities)
