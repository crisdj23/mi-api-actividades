from flask import Flask, jsonify, request, abort
import os

app = Flask(__name__)

# Ruta de bienvenida
@app.route("/")
def home():
    return "Bienvenido a la API de usuarios"

# Datos en memoria (lista de dicts)
tasks = [
    {'id': 1, 'title': 'Comprar leche', 'done': False},
    {'id': 2, 'title': 'Estudiar Flask', 'done': False},
    {'id': 3, 'title': 'Estudiar estructura', 'done': False}
]

# Leer todas las tareas
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Leer una tarea por ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        abort(404)
    return jsonify(task)

# Crear tarea
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)
    new_task = {
        'id': tasks[-1]['id'] + 1 if tasks else 1,
        'title': request.json['title'],
        'done': False
    }
    tasks.append(new_task)
    return jsonify(new_task), 201

# Actualizar tarea
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        abort(404)
    if not request.json:
        abort(400)
    task['title'] = request.json.get('title', task['title'])
    task['done'] = request.json.get('done', task['done'])
    return jsonify(task)

# Borrar tarea
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((t for t in tasks if t['id'] == task_id), None)
    if not task:
        abort(404)
    tasks = [t for t in tasks if t['id'] != task_id]
    return '', 204

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Usa el puerto que Render asigna
    app.run(host="0.0.0.0", port=port)
