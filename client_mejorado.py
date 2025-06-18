import requests
import json

# Cambia esta URL por la de tu deployment en Render
BASE_URL = "http://localhost:5000"  # Para pruebas locales
# BASE_URL = "https://tu-app.onrender.com"  # Para producción

class ActivityClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
    
    def get_activities(self):
        """Obtener todas las actividades"""
        try:
            response = requests.get(f"{self.base_url}/activities")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Error {response.status_code}: {response.text}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Error de conexión: {str(e)}"}
    
    def create_activity(self, titulo, prioridad="media"):
        """Crear una nueva actividad"""
        data = {
            "titulo": titulo,
            "prioridad": prioridad
        }
        try:
            response = requests.post(f"{self.base_url}/activities", json=data)
            if response.status_code == 201:
                return response.json()
            else:
                return {"error": f"Error {response.status_code}: {response.text}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Error de conexión: {str(e)}"}
    
    def update_activity(self, activity_id, **kwargs):
        """Actualizar una actividad existente"""
        try:
            response = requests.put(f"{self.base_url}/activities/{activity_id}", json=kwargs)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Error {response.status_code}: {response.text}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Error de conexión: {str(e)}"}
    
    def delete_activity(self, activity_id):
        """Eliminar una actividad"""
        try:
            response = requests.delete(f"{self.base_url}/activities/{activity_id}")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Error {response.status_code}: {response.text}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Error de conexión: {str(e)}"}
    
    def get_stats(self):
        """Obtener estadísticas de las actividades"""
        try:
            response = requests.get(f"{self.base_url}/stats")
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"Error {response.status_code}: {response.text}"}
        except requests.exceptions.RequestException as e:
            return {"error": f"Error de conexión: {str(e)}"}

# Ejemplo de uso
if __name__ == "__main__":
    client = ActivityClient()
    
    print("=== DEMO DE LA API ===")
    print("\n1. Obteniendo todas las actividades:")
    print(json.dumps(client.get_activities(), indent=2, ensure_ascii=False))
    
    print("\n2. Creando nueva actividad:")
    nueva = client.create_activity("Aprender a desplegar APIs", "alta")
    print(json.dumps(nueva, indent=2, ensure_ascii=False))
    
    print("\n3. Obteniendo estadísticas:")
    print(json.dumps(client.get_stats(), indent=2, ensure_ascii=False))
