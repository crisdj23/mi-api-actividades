import requests

# URL de tu API en Render
BASE_URL = "https://servicio-web-1.onrender.com"

# Obtener todas las tareas
def get_tasks():
    response = requests.get(f"{BASE_URL}/tasks")
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"

# Crear una nueva tarea
def create_task(title):
    data = {"title": title}
    response = requests.post(f"{BASE_URL}/tasks", json=data)
    if response.status_code == 201:
        return response.json()
    else:
        return f"Error: {response.status_code}"

# Prueba el script
print("Lista de tareas:", get_tasks())
print("Creando tarea:", create_task("Aprender a consumir APIs"))
