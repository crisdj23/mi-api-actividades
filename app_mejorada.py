from flask import Flask, jsonify, request, abort
import os
from datetime import datetime

app = Flask(__name__)

# Ruta de bienvenida personalizada
@app.route("/")
def home():
    return {
        "mensaje": "¡Bienvenido a mi API de Gestión de Actividades!",
        "version": "1.0",
        "autor": "cristian montaño martinez",
        "endpoints": [
            "GET /activities - Obtener todas las actividades",
            "POST /activities - Crear nueva actividad",
            "GET /activities/<id> - Obtener actividad específica",
            "PUT /activities/<id> - Actualizar actividad",
            "DELETE /activities/<id> - Eliminar actividad"
        ]
    }

# Datos en memoria con más información
activities = [
    {
        'id': 1, 
        'titulo': 'Comprar ingredientes para cocinar', 
        'completada': False,
        'prioridad': 'alta',
        'fecha_creacion': '2024-01-15'
    },
    {
        'id': 2, 
        'titulo': 'Estudiar desarrollo web con Flask', 
        'completada': False,
        'prioridad': 'media',
        'fecha_creacion': '2024-01-16'
    },
    {
        'id': 3, 
        'titulo': 'Revisar arquitectura del proyecto', 
        'completada': True,
        'prioridad': 'baja',
        'fecha_creacion': '2024-01-17'
    }
]

# Obtener todas las actividades
@app.route('/activities', methods=['GET'])
def get_activities():
    return jsonify({
        "total": len(activities),
        "actividades": activities
    })

# Obtener actividad por ID
@app.route('/activities/<int:activity_id>', methods=['GET'])
def get_activity(activity_id):
    activity = next((a for a in activities if a['id'] == activity_id), None)
    if not activity:
        return jsonify({"error": "Actividad no encontrada"}), 404
    return jsonify(activity)

# Crear nueva actividad
@app.route('/activities', methods=['POST'])
def create_activity():
    if not request.json or 'titulo' not in request.json:
        return jsonify({"error": "El título es requerido"}), 400
    
    new_activity = {
        'id': activities[-1]['id'] + 1 if activities else 1,
        'titulo': request.json['titulo'],
        'completada': request.json.get('completada', False),
        'prioridad': request.json.get('prioridad', 'media'),
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d')
    }
    activities.append(new_activity)
    return jsonify(new_activity), 201

# Actualizar actividad
@app.route('/activities/<int:activity_id>', methods=['PUT'])
def update_activity(activity_id):
    activity = next((a for a in activities if a['id'] == activity_id), None)
    if not activity:
        return jsonify({"error": "Actividad no encontrada"}), 404
    
    if not request.json:
        return jsonify({"error": "Datos JSON requeridos"}), 400
    
    activity['titulo'] = request.json.get('titulo', activity['titulo'])
    activity['completada'] = request.json.get('completada', activity['completada'])
    activity['prioridad'] = request.json.get('prioridad', activity['prioridad'])
    
    return jsonify(activity)

# Eliminar actividad
@app.route('/activities/<int:activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    global activities
    activity = next((a for a in activities if a['id'] == activity_id), None)
    if not activity:
        return jsonify({"error": "Actividad no encontrada"}), 404
    
    activities = [a for a in activities if a['id'] != activity_id]
    return jsonify({"mensaje": "Actividad eliminada correctamente"}), 200

# Endpoint adicional: obtener estadísticas
@app.route('/stats', methods=['GET'])
def get_stats():
    total = len(activities)
    completadas = len([a for a in activities if a['completada']])
    pendientes = total - completadas
    
    return jsonify({
        "total_actividades": total,
        "completadas": completadas,
        "pendientes": pendientes,
        "porcentaje_completado": round((completadas / total * 100) if total > 0 else 0, 2)
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
